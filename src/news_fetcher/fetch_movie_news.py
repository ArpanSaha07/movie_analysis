import requests
import datetime as Date

NEWS_QUERY_STRING_TEMPLATE = "https://newsapi.org/v2/teverything?category=entertainment&q={}&from={}&sortBy=popularity&apiKey={}&language=en"

API_KEY = "39c9bdc004d9478796169d90f905889f"

def fetch_latest_news(news_keywords : list, lookback_days=30) -> dict:
    """
    Returns a json object from the newsapi based on the inputs

    :param api_key: API key for getting access to the newsapi
    :param news_keywords: queries NewsAPI and returns articles containing these keywords
    :param lookback_days: (optional) the previous number of days from today from which the news articles should be searched for

    :raises ValueError: if the input does not contain any keywords or the lookback_day < 0 or if keywords contain any non-alphabetic characters or if the API value is wrong
    
    :raises Exception: if response.status_code != 200

    Examples:
    >>> fetch_latest_news("Your_API_KEY", ["Trump", "riots"], 20)
    >>> fetch_latest_news("Your_API_KEY", ["taylor", "swift", "movie"])
    """

    if (len(news_keywords) == 0):
        raise ValueError("News keywords cannot be empty")
    
    if (lookback_days < 0):
        raise ValueError("Lookback days cannot be negative")
    
    for value in news_keywords:
        if value.isalpha() == False:
            raise ValueError("Keywords cannot contain non-alphabetic character")

    news_entries = "+".join(news_keywords)
    lookback_date = Date.datetime.today() - Date.timedelta(days=lookback_days)

    query_string = NEWS_QUERY_STRING_TEMPLATE.format(news_entries, str(lookback_date), API_KEY)

    response = requests.get(query_string)

    if response.status_code != 200:
        raise Exception(f"Unable to fetch news api for {news_entries}")
    
    # raise an exception for api_key error
    if response.status_code == 401:
        raise ValueError("API_KEY is not valid")

    return response.json()
