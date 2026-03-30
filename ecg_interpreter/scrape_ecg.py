import requests
from bs4 import BeautifulSoup
import pandas as pd

# THIS VERSION GOES THROUGH THE ARTICLES IN THE PEOPLE INDEX SEARCH
# NEED TO CHANGE TO JUST GO THROUGH ARTICLES VOLUME BY VOLUME
# ENSURE THAT ANY PAGE SCRAPED IS ACTUAL CONTENT

# set up base url for article pages and for index search
base_article_url = "https://muse.jhu.edu"
base_name_index_url = 'https://muse.jhu.edu/ushmm/index/names'
# create session to save cookies
session = requests.Session()
session.get(base_name_index_url)

# get list of names from people index search
# return list of raw names
def get_raw_names():
    # get content of the index search page
    index_search_response = requests.get(base_name_index_url)
    index_search_soup = BeautifulSoup(index_search_response.text, 'lxml')
    # list of all people entries
    people_entries = index_search_soup.find_all(class_="entry")
    # list of all people names
    people_names = [person.text.strip() for person in people_entries]

    # save people names into df, save to csv
    people_df = pd.DataFrame(people_names, columns = ['Name'])
    people_df.to_csv('./tables/raw_names.csv')
    return people_names

# helper function - get soup of the results of a person search
def get_person_search_results(name):
    # params for AJAX request
    params = {
        "action": "get_links",
        "v": "",
        "search_term": name
    }
    # headers for AJAX request
    headers = {
        "Referer": "https://muse.jhu.edu/ushmm/index/names",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    # get results of the person search
    person_response = requests.get(base_name_index_url, params=params, headers=headers)
    person_response.raise_for_status()
    person_result = BeautifulSoup(person_response.text, 'lxml')
    return person_result

# helper function - get dict of article name (place name) with its url (including base url)
def get_associated_article_links(person_soup):
    h3 = person_soup.find("h3")
    h4 = person_soup.find("h4")
    entries = person_soup.select("ol li a")
    articles = {}
    if h3 and h4 and entries:
        for e in entries:
            articles[e.text] = base_article_url + e["href"] 
    return articles

# helper function - get the content of an article given the full url
def get_article_content(url):
    article_response = requests.get(url)
    article_response.raise_for_status()
    article_soup = BeautifulSoup(article_response.text, 'lxml')
    article_body = article_soup.find_all(id="body")
    return article_body

# CHANGE BELOW CODE
# test all associated articles for first 3 people in the index search
# i = 0
# for person in people_names:
#     if i >= 3:
#         break
#     # use helper functions to get the articles associated with that person and print out results
#     person_soup = get_person_search_results(person)
#     article_links = get_associated_article_links(person_soup)
#     print(person, article_links)
#     # for each article associated, use helper function to get content and print out results
#     for place, link in article_links.items():
#         article_body = get_article_content(link)
#         print(place)
#         print(article_body)
#         print()
#     i += 1

def scrape():
    return