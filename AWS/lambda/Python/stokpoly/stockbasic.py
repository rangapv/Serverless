#!/usr/bin/env python3
#author:rangapv@yahoo.com
#14-11-24

import os
from polygon import RESTClient
from polygon.rest import models

import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_POLYGON')
#API_KEY = "insert-api-key"
client = RESTClient(API_KEY)

aggs = client.get_aggs(
    "TSLA",
    1,
    "day",
    "2024-11-14",
    "2024-11-14",
)
print(aggs)
ticker = input("Enter the Ticker for which you need the Marketcap:")
details = client.get_ticker_details(ticker)
#print (details)
detailcap = details.market_cap
print (detailcap)
