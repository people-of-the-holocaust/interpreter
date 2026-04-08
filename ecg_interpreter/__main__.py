import pandas as pd
from ecg_interpreter import get_raw_names, create_ppl_table, scrape, get_article_content, is_key, get_person_action

def main():
    # set up people_table
    raw_ppl_names = get_raw_names()
    ppl_df = create_ppl_table(raw_ppl_names)

    # set up place_table
    plc_df = pd.read_csv("./tables/place_table.csv")

    # volume base urls
    vol_base_urls = ["1", "2", "3", "4"]

    for url in vol_base_urls:
        article_links = scrape(url, plc_df)
        for lid, link in article_links.items():
            place, body = get_article_content(link)
            # tokenize body into sentences
            sentences = body
            for sent in sentences:
                pids = is_key(sent, ppl_df)
                for pid in pids:
                    action = get_person_action(sent, pid, ppl_df, lid)


    return 0