import re
from bs4 import BeautifulSoup

def clean_article(soup):
    # get article title and body text
    title = soup.title.text
    body_tags = soup.select("div#body")
    # clean text to return
    clean = ""
    # loop over body tags
    for body in body_tags:
        text = body.get_text()
        # remove footnote markers
        text = re.sub(r'\.\d+', '.', text)
        text = re.sub(r'\.”\d+', '.”', text)
        # remove unnecessary UI text and new lines
        text = re.sub(r'Click for larger view', '', text, flags=re.IGNORECASE)
        text = re.sub(r'View full resolution', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\[End Page \d+\]', '', text, flags = re.IGNORECASE)
        text = re.sub(r'\n+', '\n', text)
        # remove image credit lines
        text = re.sub(r'^.*USHMM.*$', '', text, flags=re.MULTILINE)
        # add cleaned body text to string that will be returned
        clean += text
    # return tuple with article title and clean text
    return (title, clean)