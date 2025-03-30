#!/usr/bin/env python3
#author:rangapv@yahoo.com
#14-11-24

import os
import re
import subprocess
from polygon import RESTClient
from polygon.rest import models

import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_POLYGON')
#API_KEY = "insert-api-key"
client = RESTClient(API_KEY)
ticker = input("Enter the Ticker for which you need the Marketcap:")

aggs = client.get_aggs(
    ticker,
    1,
    "day",
    "2025-03-28",
    "2025-03-28",
)
print(aggs)
#cloprice = (aggs.close)
#   p4 = "awk \'{split($0,a,\"=\"); print a[2]}\'"

print("prev aggs")
aggs1 = client.get_previous_close_agg(ticker)
print(aggs1)


p4 = "awk \'{split($0,a,\",\");print (a[2])}\'"
l23 = subprocess.run(['echo "{}" | {}'.format(aggs1[0],p4)], capture_output=True, shell=True, text=True, check=False)
print(l23)
p5 = l23.stdout
print(p5)

r4 = "awk \'{split($0,a,\"=\");print (a[2])}\'"
l24 = subprocess.run(['echo "{}" | {}'.format(p5,r4)], capture_output=True, shell=True, text=True, check=False)
print(l24)
p6 = l24.stdout
print(p6)

outstand1 = client.get_ticker_details(ticker)
print("outstand output is")
print(outstand1)

share_outstand = outstand1.share_class_shares_outstanding

num1 = float(p6)
num2 = float(share_outstand)

marketcap = ( num1 * num2 )

print(marketcap)
#outstanding = details.share_class_shares_outstanding

#print (details)
#detailcap = details.market_cap
#print (detailcap)

