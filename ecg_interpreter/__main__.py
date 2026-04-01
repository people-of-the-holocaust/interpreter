import pandas as pd
from ecg_interpreter import get_raw_names, create_ppl_table, scrape, is_key, get_person_action, clean_article

# get raw names
raw_names = get_raw_names()

# clean raw names and create people table
ppl_df = create_ppl_table(raw_names)

# scrape, clean
# is_key, get_person_action