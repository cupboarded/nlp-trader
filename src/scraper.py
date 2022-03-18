import requests
import datetime
import spacy
from bs4 import BeautifulSoup
nlp = spacy.load("en_core_web_sm")

def google_news_search(coin):
    """
    Searches the specific coin on google news

    Arguments:
        - coin: Coin given to be searched

    Return Value:
        - articles: List of dictionaries, each dictionary contains info about
                    an article
    """
    newsapi_key = "f65bfd47eb6e443885fc92bdeb39f860"

    curr_date = datetime.datetime.now()
    from_date = curr_date - datetime.timedelta(days = 3)

    url = (
        "https://newsapi.org/v2/everything?"
        f"q={coin}"
        "&searchIn=title,description"
        f"&from={from_date.year}-{from_date.month}-{from_date.day}"
        f"&to={curr_date.year}-{curr_date.month}-{curr_date.day}"
        "&language=en"
        "&sortBy=popularity"
        f"&apiKey={newsapi_key}"
    )

    response = requests.get(url)
    response = response.json()
    articles = response["articles"]

    return articles

def site_scrape(url):
    """
    Scrapes the article from the url of a website given

    Arguments:
        - url: The url of the article

    Return Value:
        - article_sentences: List of sentences in the article given
    """
    response = requests.get(url)
    response.encoding = "utf-8"

    html = response.text
    html = BeautifulSoup(html)
    html_text = html.get_text()

    text_clean = html_text.replace('n', ' ')
    text_clean = text_clean.replace('/', ' ')
    text_clean = ''.join([i for i in text_clean if i != "'"])

    article_sentences = []
    tokens = nlp(text_clean)
    for sentence in tokens.sents:
        article_sentences.append(sentence.text.strip())

    return article_sentences

if __name__ == '__main__':
    articles = google_news_search("ethereum")

