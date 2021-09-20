import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
API_KEY = os.getenv("API_KEY")

def get_article_data(keyword):
    params = {
        "q": keyword,
        "api-key": API_KEY
    }

    response = requests.get(
        BASE_URL,
        params=params,
    )

    response_json = response.json()

    headlines = []
    snippets = []
    dates = []
    links = []
    try:
        articles = response_json["response"]["docs"]
        for article in articles:
            headlines.append(article["headline"]["main"])
            snippets.append(article["snippet"])
            dates.append(article["pub_date"])
            links.append(article["web_url"])
    except KeyError:
        print("Couldn't fetch articles!")

    return {
        "headlines": headlines,
        "snippets": snippets,
        "dates": dates,
        "links": links,
    }
