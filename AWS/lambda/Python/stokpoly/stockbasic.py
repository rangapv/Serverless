#!/usr/bin/env python
#author:rangapv@yahoo.com
#14-11-24

import os
import re
import subprocess
from polygon import RESTClient
import time
#from polygon.rest import models
from numerize import numerize
import datetime
from dotenv import load_dotenv
from decimal import *

load_dotenv()



#def imagels():
API_KEY = os.getenv('API_POLYGON')
    #API_KEY = "insert-api-key"
client = RESTClient(API_KEY)

ticker = "META"

    #ticker = input("Enter the Ticker for which you need the Marketcap:")
aggs = client.get_aggs(
        ticker,
        1,
        "day",
        "2025-03-28",
        "2025-03-28",
)   
print(f'printing aggs {aggs}')
#cloprice = (aggs.close)
#   p4 = "awk \'{split($0,a,\"=\"); print a[2]}\'"
print("prev aggs")
aggs1 = client.get_previous_close_agg(ticker)
print(f'printing aggs1 {aggs1}')
#print(f'printing aggs1 {aggs1.status}')

#print(f'printgd aggs1of0 {aggs1[0].stderr}')
p4 = "awk \'{split($0,a,\",\");print (a[2])}\'"
l23 = subprocess.run(['echo "{}" | {}'.format(aggs1[0],p4)], capture_output=True, shell=True, text=True, check=False)
print(l23)
p5 = l23.stdout
p53 = l23.stderr
print(f'printing stdout {p5}')
print(f'printing error {p53}')

r4 = "awk \'{split($0,a,\"=\");print (a[2])}\'"
l24 = subprocess.run(['echo "{}" | {}'.format(p5,r4)], capture_output=True, shell=True, text=True, check=False)
print(l24)
p6 = l24.stdout
print(p6)

outstand1 = client.get_ticker_details(ticker)
print(f'tickr details aggs are {outstand1}')

share_outstand1 = outstand1.share_class_shares_outstanding
share_outstand = outstand1.weighted_shares_outstanding

print(f'weighted shares are {share_outstand}, class shares outstand are {share_outstand1}') 
num1 = float(p6)
num2 = float(share_outstand)
num3 = float(share_outstand1)
print("outstand output is")
print(num2)

cap3 = numerize.numerize(3000000000000,4)
cap32 = float(3000000000000)
cap31 = float(cap32)
marketcap = ( num1 * num2 )
marketcap2 = ( num1 * num3 )
sharediff = ( num2 - num3 )
mcapdiff = ( marketcap - marketcap2 )
reqprice = ( cap31 / num2 )
getcontext().prec = 3
reqprice1 = Decimal(reqprice)
reqprice2 = format(reqprice1,'.7')
print(f'mcap with weighted shares is {marketcap} , mcap with class shares outstand is {marketcap2}')
print(f'the difference of shares are {sharediff}')
print(f'the difference of mcap is {mcapdiff}')

print(f'The Stock prices for {ticker} to remain at a $ {cap3} club is $ {reqprice2}')
aggs2 = aggs1[0]
print(f'aggs2 is {aggs1}')
pl = subprocess.run(['echo "{}" | grep timestamp'.format(aggs2)], capture_output=True, shell=True, text=True, check=False)
l21 = pl.stdout
p3 = "awk \'{split($0,a,\",\"); print a[6]}\'"
l22 = subprocess.run(['echo "{}" | {}'.format(l21,p3)], capture_output=True, shell=True, text=True, check=False)
l23 = l22.stdout
p4 = "awk \'{split($0,a,\"=\"); print a[2]}\'"
l23 = subprocess.run(['echo "{}" | {}'.format(l23,p4)], capture_output=True, shell=True, text=True, check=False)
p5 = l23.stdout
print(f'p5 is {p5}')
now1 = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
now2 = datetime.datetime.now().strftime('%d-%m-%y')
#stock_dict2 = { **stock_dict2, x : [ detailcap , now2 ] }
print(f'now1 is {now1} and now2 is {now2}')

t21 = p5[:10]
t1 = int(t21)
print(f't1 is {t1}')
t2 = time.ctime(t1)
#clostime = datetime.datetime.fromtimestamp(t1).strftime('%c')
#print(f'closttime is {clostime}')
print(f't2 is {t2}')
print('')
print("")
print(None)
print('\n')
print('hi')
    #return marketcap
#outstanding = details.share_class_shares_outstanding
list4 = [1]
list4.append(2)
print(list4)
#print (details)
#detailcap = details.market_cap
#print (detailcap)

detailcap1 = outstand1.market_cap
detailcap = marketcap
print(f'detailcap1 is {detailcap1} , marketcap is {marketcap} , detailcap is {detailcap}')
diffcap1 = ( detailcap1 - detailcap )
diffcap2 = numerize.numerize(diffcap1)

if detailcap1 > marketcap:
   print('insode details')
   detailcap = marketcap 
   print(f'diffcap1 is {diffcap2}')
else:
   detailcap = detailcap1
   print('insode else')
   print(f'diffcap1 is {diffcap2}')
#if __name__ == "main":
    #r1 = imagels()
    #print(f'the market cap is {r1}')
