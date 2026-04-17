from .key_sentence import is_key
from .actions import get_person_action
from .clean_article_text import clean_article
from .clean_people_names import create_ppl_table
from .scrape_people import get_raw_names
from .scrape_articles import scrape_vol
from .scrape_articles import get_article_content
from .pothDataStructure import Encyclopedia, Volume, Article, Sentence, Action
from .tree_funcs import print_ecg
from .__main__ import main

if __name__ == "__main__":
    main()