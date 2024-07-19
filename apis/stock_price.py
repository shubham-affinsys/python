import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
"""
    Informational responses (100  - 199)
    Successful responses (200 - 299)
    Redirection messages (300 - 399)
    Client error responses (400 - 499)
    Server error responses (500 - 599)

"""

def get_stock_data(symbol):
    key=os.getenv("STOCK_KEY")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&outputsize=full&apikey={key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        price = data["Time Series (5min)"][last_refreshed]["1. open"]
        return price
    else :
        return None

stock_price = {}
symbols = {"IBM","ABL","AAPL"}

for symbol in symbols:
    price = get_stock_data(symbol)

    if price is not None:
        stock_price[symbol]=price
    print(f"{symbol}: {price}")