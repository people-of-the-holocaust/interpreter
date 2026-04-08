import requests
from bs4 import BeautifulSoup
import pandas as pd

from ecg_interpreter import clean_article

# THIS VERSION GOES THROUGH THE ARTICLES IN THE PEOPLE INDEX SEARCH
# NEED TO CHANGE TO JUST GO THROUGH ARTICLES VOLUME BY VOLUME
# ENSURE THAT ANY PAGE SCRAPED IS ACTUAL CONTENT

# helper function - get dict of lid and article url (including base url)
def get_vol_article_links(vol_soup, plc_df):
    articles = {}
    # look at each entry, check if name is in plc_df, save lid and url into dict

    # old code
    # h3 = person_soup.find("h3")
    # h4 = person_soup.find("h4")
    # entries = person_soup.select("ol li a")
    # articles = {}
    # if h3 and h4 and entries:
    #     for e in entries:
    #         articles[e.text] = base_article_url + e["href"] 
    return articles

# get urls for all of the content articles in a volume
def scrape_vol(vol_url, plc_df, session):
    vol_response = session.get(vol_url)
    vol_response.raise_for_status()
    vol_soup = BeautifulSoup(vol_response.text, 'lxml')
    article_links = get_vol_article_links(vol_soup, plc_df)
    return article_links


# get the content of an article given the full url
def get_article_content(url, session):
    article_response = session.get(url)
    article_response.raise_for_status()
    article_soup = BeautifulSoup(article_response.text, 'lxml')
    article_body = article_soup.find_all(id="body")
    # CALL clean_article
    # return (place, clean_body)
    return article_body