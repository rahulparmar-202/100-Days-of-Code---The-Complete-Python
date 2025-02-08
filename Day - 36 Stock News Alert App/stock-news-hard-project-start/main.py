# import random
import requests
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv

# TWILIO
account_sid = "AC5473d59d7ebbac0eb90aa96530ed506c"
auth_token = os.getenv("AUTH_TOKEN")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = os.getenv("STOCK_API")
NEWS_API = os.getenv("NEWS_API")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

today = dt.datetime.today().date()
# Get yesterday's date
yesterday = today - dt.timedelta(days=3)
# Get the date of the day before yesterday
day_before_yesterday = today - dt.timedelta(days=4)


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
    "datatype": "json",
}
response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
stock_data = response.json()["Time Series (Daily)"]
# print(stock_data    )

yesterday_stock = stock_data[str(yesterday)]
day_before_stock = stock_data[str(day_before_yesterday)]

print(yesterday_stock)
print(day_before_stock)

# get the stock close for yesterday and day before that
yesterday_stock_close = yesterday_stock["4. close"]
day_before_stock_close = day_before_stock["4. close"]

# calculate the price change and the percent change
price_change = float(yesterday_stock_close) - float(day_before_stock_close)
percentage_change = round((price_change/float(day_before_stock_close)) * 100, 2)

up_down = None
if price_change > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator

news_params = {
    "apikey": NEWS_API,
    "q": COMPANY_NAME,
    "sortBy": "popularity",
}

def get_news():
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_articles = news_response.json()["articles"]
    print(news_articles)
    three_articles = news_articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK}: {up_down} {percentage_change}% \nHEADLINE: {article['title']}. \nBrief: {article['description']}." for article in three_articles]
    print(formatted_articles)
    return formatted_articles

# ----------- Checks if the stock is increased or decreased -----------
if percentage_change >= 1:
    articles_formatted = get_news()
    # Sends the message Notification
    client = Client(account_sid, auth_token)
    for article in articles_formatted:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=article,
            to='whatsapp:+916367906870'
        )
        print(message.status)
else:
    print(f"Stock Price Change: {percentage_change}%.")



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

