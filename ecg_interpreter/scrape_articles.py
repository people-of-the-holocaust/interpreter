import requests
from bs4 import BeautifulSoup
import pandas as pd
from importlib.resources import files


from ecg_interpreter import clean_article

# helper function - get df containing lids and article urls (NOT including base url)
def get_vol_article_links(vol_soup, plc_df, vol_num):
    filtered_plc_df = plc_df[plc_df["Volume"] == vol_num]
    # articles = {}
    articles_df = pd.DataFrame(columns=["LID", "doc_link"])
    article_cards = vol_soup.find_all(class_="card_text")
    # look at each article entry on the page
    for card in article_cards:
        title = card.find(class_="title").text
        # check if place name is in plc_df
        row = filtered_plc_df[filtered_plc_df["Name"].str.lower() == title.lower()]
        row = row.reset_index(drop=True)
        # case 1: article is a place
        if len(row) == 1:
            doc_num = card.find(class_="action_btns")
            entries = card.select("ol li a")
            # document url is always the first list item
            if entries:
                # save lid and url ending into dict
                # articles[int(row["LID"][0])] = entries[0]["href"]
                # save lid and url ending into df
                articles_df.loc[len(articles_df)] = [int(row["LID"][0]), entries[0]["href"]]
        # case 2: article is not a place / other error - do nothing for now
        # else:
        #     print("NUMBER OF ROWS FOUND WITH", title, ":", len(row))
    # return articles
    return articles_df

# get urls (NOT including base url) for all of the content articles in a volume
def scrape_vol(vol_url, plc_df, session, vol_num):
    vol_response = session.get(vol_url)
    vol_response.raise_for_status()
    vol_soup = BeautifulSoup(vol_response.text, 'lxml')
    article_links = get_vol_article_links(vol_soup, plc_df, vol_num)
    # export article_links to csv
    file_name = "tables/vol" + str(vol_num) + "_article_links.csv"
    article_links_csv_path = files("ecg_interpreter").joinpath(file_name)
    article_links.to_csv(article_links_csv_path)
    return article_links

# get the content of an article given the full url
def get_article_content(url, session):
    article_response = session.get(url)
    article_response.raise_for_status()
    article_soup = BeautifulSoup(article_response.text, 'lxml')
    return clean_article(article_soup)
