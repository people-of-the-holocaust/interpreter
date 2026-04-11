import requests
import pandas as pd
from ecg_interpreter import get_raw_names, create_ppl_table, scrape_vol, get_article_content, is_key, get_person_action
from ecg_interpreter import Encyclopedia, Volume, Article, Sentences
from nltk.tokenize import sent_tokenize

def main():
    # urls
    base_article_url = "https://muse.jhu.edu"
    name_index_url = 'https://muse.jhu.edu/ushmm/index/names'
    vol_urls = ["1", "2", "3", "4"]

    # create session to save cookies
    session = requests.Session()

    # set up people_table
    raw_ppl_names = get_raw_names(session, name_index_url)
    ppl_df = create_ppl_table(raw_ppl_names)

    # set up place_table
    plc_df = pd.read_csv("./tables/place_table.csv")

    # create encyclopedia node
    ecg_node = Encyclopedia()

    for url in vol_urls:
        # create volume node
        curr_vol = Volume()
        ecg_node.volumesList.append(curr_vol)
        # get content articles from volume
        article_links = scrape_vol(url, plc_df, session)
        # loop over each article
        for lid, link in article_links.items():
            place, body = get_article_content(link, session)
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