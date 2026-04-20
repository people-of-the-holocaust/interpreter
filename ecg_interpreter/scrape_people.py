from bs4 import BeautifulSoup
import pandas as pd
from importlib.resources import files


# get list of names from people index search
# return list of raw names
def get_raw_names(session, base_name_index_url):
    # get content of the index search page
    index_search_response = session.get(base_name_index_url)
    index_search_soup = BeautifulSoup(index_search_response.text, 'lxml')
    # list of all people entries
    people_entries = index_search_soup.find_all(class_="entry")
    # list of all people names
    people_names = [person.text.strip() for person in people_entries]

    # save people names into df, save to csv
    people_df = pd.DataFrame(people_names, columns = ['Name'])
    raw_names_path = files("ecg_interpreter").joinpath("tables/raw_names.csv")
    people_df.to_csv(raw_names_path)
    return people_names
