import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "2P8VZ5M9GM5XZFGB"
NEWS_API_KEY = "133cbf112ce2414ab1f350bae6e7335c"
TWILIO_SID = "ACd1dc0688e45f7f53e9fcdda464d9f1e2"
AUTH_TOKEN = "e16610529cedf7fac0c156a99ec3492e"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY

}

news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "searchIn": "title"
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]
stock_dictionary = [value for (key, value) in stock_data.items()]
yesterday_closing_price = stock_dictionary[0]["4. close"]
# Get the day before yesterday's closing stock price
day_before_closing_price = stock_dictionary[1]["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_difference = abs(float(yesterday_closing_price) - float(day_before_closing_price))
# Work out the percentage difference in price between closing price yesterday and closing price
# the day before yesterday.
percentage_difference = round(price_difference / float(yesterday_closing_price)) * 100
# If TODO4 percentage is greater than 5 then print("Get News").
up_down = None
if percentage_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if percentage_difference > 0:
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    news_articles = news_response.json()["articles"]
    # Use Python slice operator to create a list that contains the first 3 articles.
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = news_articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

# Create a new list of the first 3 article's headline and description using list comprehension.
    structured_articles = [f"{STOCK_NAME}: {up_down}{percentage_difference}%{article['title']}\nBrief: {article['description']}"for article in three_articles]
# Send each article as a separate message via Twilio.

    client = Client(TWILIO_SID, AUTH_TOKEN)
    for article in structured_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+17402364345',
            to='+23408069226824'
            )

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

