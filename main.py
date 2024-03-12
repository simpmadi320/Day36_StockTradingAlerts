import requests
from datetime import datetime, timedelta

from datetime import datetime
STOCK_NAME = "XRP"
COMPANY_NAME = "Ripple Labs"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "B2XBZKCX8EGHTHN6"
NEWS_API_KEY = "1bddf2fcb4b748c0a15085a642301f94"


def get_news():

    news_params = {
        "q": "XRP",
        "from": datetime.today() - timedelta(days=2),
        "to": datetime.today() - timedelta(days=1),
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 3,
        "apikey": "1bddf2fcb4b748c0a15085a642301f94"
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    data = response.json()["articles"]
    articles = (f"Headline: {article['title']}. \nBrief: {article['description']}" for article in data)

    for a in articles:
        print("\n"+a)


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": STOCK_NAME,
    "market": "CAD",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Digital Currency Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4a. close (CAD)']
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4a. close (CAD)']
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

#TODO 1 -> 5
if diff_percent > 1:
    get_news()

