import requests
import pandas as pd
from ecg_interpreter import get_raw_names, create_ppl_table, scrape, get_article_content, is_key, get_person_action

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

    for url in vol_urls:
        article_links = scrape(url, plc_df, session)
        for lid, link in article_links.items():
            place, body = get_article_content(link, session)
            # tokenize body into sentences
            sentences = body
            for sent in sentences:
                pids = is_key(sent, ppl_df)
                for pid in pids:
                    action = get_person_action(sent, pid, ppl_df, lid)


    return 0