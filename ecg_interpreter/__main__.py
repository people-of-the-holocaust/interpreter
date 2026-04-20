import requests
import pandas as pd
from ecg_interpreter import get_raw_names, create_ppl_table, scrape_vol, get_article_content, is_key, get_person_action, print_ecg
from ecg_interpreter import Encyclopedia, Volume, Article, Sentence
from nltk.tokenize import sent_tokenize
from importlib.resources import files

def main():
    print("IN MAIN")

    # urls
    base_article_url = "https://muse.jhu.edu"
    name_index_url = 'https://muse.jhu.edu/ushmm/index/names'
    vol_urls = {
        1: "https://muse.jhu.edu/resource_group/13",
        2: "https://muse.jhu.edu/resource_group/59",
        3: "https://muse.jhu.edu/resource_group/91",
        4: "https://muse.jhu.edu/resource_group/111"
    }

    # create session to save cookies
    session = requests.Session()

    # set up people_table
    raw_ppl_names = get_raw_names(session, name_index_url)
    ppl_df = create_ppl_table(raw_ppl_names)
    # print(ppl_df.head())

    # set up place_table
    place_csv_path = files("ecg_interpreter").joinpath("tables/place_table.csv")
    plc_df = pd.read_csv(place_csv_path)
    # print(plc_df.head())

    # set up activity dataframe
    activity_df = pd.DataFrame()

    # set up error log
    with open("error_log.txt", "w") as f:
        f.write("Exceptions occured while processing the following articles:\n")

    # create encyclopedia node
    ecg_node = Encyclopedia()

    print("STARTING VOLUME SCRAPING")

    for vnum, vurl in vol_urls.items():
        print("VOLUME:", vnum)

        # create volume node
        curr_vol = Volume(vnum, vurl)
        ecg_node.addVolume(curr_vol)
        # get links for content articles from volume page
        article_links = scrape_vol(vurl, plc_df, session, vnum)
        print("NUMBER OF ARTICLES:", len(article_links))
        # loop over each article
        i = 0
        for lid, link in article_links.items():
            # TESTING - ONLY LOOK AT FIRST 10 ARTICLES
            if i >= 10:
                break
            # link is formatted as '/document/####'
            doc_num = int(link.split("/")[-1])
            try:
                # scrape article content
                place, body = get_article_content((base_article_url + link), session)
                print("Scraped", doc_num)

                # create article node
                curr_article = Article(place, body, doc_num)
                curr_vol.addArticle(curr_article)
                # get sentences in article
                sentences = sent_tokenize(body)
                # loop over each sentence
                for sent in sentences:
                    # check if sent is KEY, get pids from sent
                    pids = is_key(sent, ppl_df)
                    if type(pids) == list and len(pids) > 0:
                        print("Sentence is key:", sent)
                        # create sentence node
                        curr_sent = Sentence(sent, pids)
                        curr_article.addSent(curr_sent)
                        # loop over each pid found in key sentence
                        for pid in pids:
                            # get action node
                            curr_sent.addAction(get_person_action(sent, pid, ppl_df, lid))
            except:
                print("Exception occured - skipped article", link)
                with open("error_log.txt", "a") as f:
                    f.write(f"{doc_num}\n")
                continue
            i += 1
        # get all actions for this volume, save into activity_df
        vol_actions = curr_vol.getActions()
        vol_acts_as_dicts = [vars(act) for act in vol_actions]
        activity_df = pd.concat([activity_df, pd.DataFrame(vol_acts_as_dicts)], ignore_index=True)

    # export activity_df to csv
    activity_csv_path = files("ecg_interpreter").joinpath("tables/activity_table.csv")
    activity_df.to_csv(activity_csv_path)

    # final_tree = print_ecg(ecg_node)
    # with open("tree_output.txt", "w") as f:
        # f.write(final_tree)
    # print(final_tree)
    return 0
