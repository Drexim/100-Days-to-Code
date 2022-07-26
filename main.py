import requests
from twilio.rest import Client

TWILIO_SID = "SID here"
TWILIO_AUTH = "auth here"
TWILIO_PHONE_NUM = "num here"


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla, Inc"
ALPHA_API_KEY = "api key here"

ENDPOINT = "https://www.alphavantage.co/query"


# TODO 1. - Get yesterday's closing stock price.
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY,
}

response = requests.get(ENDPOINT, params=STOCK_PARAMS)
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# TODO 3. - Find the positive difference
price_difference = abs(float(day_before_yesterday_closing_price) - float(yesterday_closing_price))

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
percentage_difference = (price_difference / float(yesterday_closing_price)) * 100


# TODO 5. - Use the News API to get articles related to the COMPANY_NAME.

NEWS_PARAMS = {
    "function": "NEWS_SENTIMENT",
    "tickers": STOCK_NAME,
    "sort": "LATEST",
    "limit": 1,
    "apikey": ALPHA_API_KEY
}

news_request = requests.get(ENDPOINT, params=NEWS_PARAMS)
news_data = news_request.json()["feed"]
tesla_news = []

if percentage_difference > 5:
    for item in news_data:
        if COMPANY_NAME in item["title"]:
            tesla_news.append(item)

# TODO 6. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
first_3_articles = tesla_news[:3]

# TODO 7. - Create a new list of the first 3 article's headline and description using list comprehension.
articles = [f"Headline: \n{article['title']}. \n\n Summary: \n{article['summary']}" for article in first_3_articles]

# TODO 8. - Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH)
for article in articles:
    message = client.messages \
                .create(
                     body=article,
                     from_=TWILIO_PHONE_NUM,
                     to='receipt number here'
                 )
