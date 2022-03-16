import requests
import datetime

def google_search(coin):
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

if __name__ == '__main__':
    articles = google_search("ethereum")
