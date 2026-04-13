import requests
import pandas as pd
from ecg_interpreter import get_raw_names, create_ppl_table, scrape_vol, get_article_content, is_key, get_person_action
from ecg_interpreter import Encyclopedia, Volume, Article, Sentences
from nltk.tokenize import sent_tokenize

def main():
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

    # set up place_table
    plc_df = pd.read_csv("./tables/place_table.csv")

    # create encyclopedia node
    ecg_node = Encyclopedia()

    for vnum, vurl in vol_urls.items():
        # create volume node
        curr_vol = Volume()
        ecg_node.volumesList.append(curr_vol)
        # get content articles from volume
        article_links = scrape_vol(vurl, plc_df, session, vnum)
        # loop over each article
        for lid, link in article_links.items():
            place, body = get_article_content((base_article_url + link), session)
            # create article node
            curr_article = Article()
            curr_article.paragraphText = body
            curr_vol.articlesList.append(curr_article)
            # get sentences in article
            sentences = sent_tokenize(body)
            # loop over each sentence
            for sent in sentences:
                pids = is_key(sent, ppl_df)
                if type(pids) == list:
                    # create sentence node
                    curr_sent = Sentences()
                    # curr_sent.pids = pids
                    curr_article.sentsList.append(curr_sent)
                    # loop over each pid found in key sentence
                    for pid in pids:
                        # create action node
                        action = get_person_action(sent, pid, ppl_df, lid)
                        curr_sent.actionsList.append(action)


    return 0