import requests
import pandas as pd
from ecg_interpreter import get_raw_names, create_ppl_table, scrape_vol, get_article_content, is_key, get_person_action, print_ecg
from ecg_interpreter import Encyclopedia, Volume, Article, Sentence
from nltk.tokenize import sent_tokenize
from importlib.resources import files

def main():
    # LEVEL: ENCYCLOPEDIA

    # SET UP URLS
    base_article_url = "https://muse.jhu.edu"
    vol_urls = {
        1: "https://muse.jhu.edu/resource_group/13",
        2: "https://muse.jhu.edu/resource_group/59",
        3: "https://muse.jhu.edu/resource_group/91",
        4: "https://muse.jhu.edu/resource_group/111"
    }
    # necessary for get_raw_names function
    # name_index_url = 'https://muse.jhu.edu/ushmm/index/names'

    # create session to save cookies
    session = requests.Session()

    # SET UP people_table
    # option 1: scrape ECG people index, clean names, sort into table
    # raw_ppl_names = get_raw_names(session, name_index_url)
    # ppl_df = create_ppl_table(raw_ppl_names)
    # option 2: load in table with first column as index
    ppl_csv_path = files("ecg_interpreter").joinpath("tables/people_table.csv")
    ppl_df = pd.read_csv(ppl_csv_path, index_col=0)

    # SET UP place_table
    # necessary for scrape_vol function
    # place_csv_path = files("ecg_interpreter").joinpath("tables/place_table.csv")
    # plc_df = pd.read_csv(place_csv_path)

    # SET UP activity dataframe
    # activity_df = pd.DataFrame()

    # SET UP error log
    with open("error_log.txt", "w") as f:
        f.write("Exceptions occured while processing the following articles:\n")

    print("Completed initial set up")

    # CREATE encyclopedia node
    ecg_node = Encyclopedia()

    for vnum, vurl in vol_urls.items():
        # CREATE volume node
        curr_vol = Volume(vnum, vurl)
        ecg_node.addVolume(curr_vol)

        # get links for content articles
        # option 1: scrape volume page, save into df
        # article_links = scrape_vol(vurl, plc_df, session, vnum)
        # option 2: load in table with first column as index
        file_name = "tables/vol" + str(vnum) + "_article_links.csv"
        article_links_csv_path = files("ecg_interpreter").joinpath(file_name)
        article_links = pd.read_csv(article_links_csv_path, index_col=0)

        for row in article_links.itertuples():
            lid = row.LID
            link = row.doc_link
            # link is formatted as '/document/####'
            doc_num = int(link.split("/")[-1])
            try:
                # scrape article content
                place, body = get_article_content((base_article_url + link), session)
                # CREATE article node
                curr_article = Article(place, body, doc_num)
                curr_vol.addArticle(curr_article)

                # split article body into sentences
                sentences = sent_tokenize(body)
                for sent in sentences:
                    # check if sent is KEY, get pids from sent
                    pids = is_key(sent, ppl_df)
                    if type(pids) == list and len(pids) > 0:
                        # CREATE sentence node
                        curr_sent = Sentence(sent, pids)
                        curr_article.addSent(curr_sent)
                        for pid in pids:
                            # CREATE action node
                            curr_sent.addAction(get_person_action(sent, pid, ppl_df, lid))
            except:
                with open("error_log.txt", "a") as f:
                    f.write(f"{doc_num}\n")
                continue
        # get all actions for this volume, save into activity_df
        # vol_actions = curr_vol.getActions()
        # vol_acts_as_dicts = [vars(act) for act in vol_actions]
        # activity_df = pd.concat([activity_df, pd.DataFrame(vol_acts_as_dicts)], ignore_index=True)
        # activity_csv_path = files("ecg_interpreter").joinpath("tables/activity_table.csv")
        # activity_df.to_csv(activity_csv_path)
        # get all actions for this volume into the database
        # curr_vol.insertIntoDatabase()
        print("Updated activities for volume", vnum)

    ecg_node.insertIntoDatabase()
    # export activity_df to csv
    # activity_csv_path = files("ecg_interpreter").joinpath("tables/activity_table.csv")
    # activity_df.to_csv(activity_csv_path)

    # final_tree = print_ecg(ecg_node)
    # with open("tree_output.txt", "w") as f:
        # f.write(final_tree)
    return 0
