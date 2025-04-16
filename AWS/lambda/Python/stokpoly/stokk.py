#!/usr/bin/env python3
#author:rangapv@yahoo.com
#14-11-24

import os
import re
import subprocess
from polygon import RESTClient 
import time
#from subprocess import PIPE
import datetime
from dotenv import load_dotenv
from numerize import numerize
from operator import itemgetter

load_dotenv()

class fetch:
        #apple = yf.Ticker("AAPL")
    def polyget(self,API):
       client = RESTClient(API)
       print("inside polyget")
       return client

    def printout(self):
       print(f'client is {p1}')   
       print(f'aggs is {aggs}')
       print(f"timesstap numeral is {p5}")
       print (f"pl is {pl}")
       print (f"l21 is {l21}")
       print (f"l22 is {l23}")
       print(f"aggs for \"{x}\" s {aggs}")
       print(f"now2 is {now2}")
       #print(myList)
       #print(myList1)
       print(uplist)
       print(revlist)
       print (f"the stock with ticker symbol \"{x}\" has a market cap of {detailcap} as of {now1}")

    def ascend(self,stock_dict1):
       #print(stock_dict1)
       #print((stock_dict1.values()))
       #print(list(stock_dict1.values())[1])
       myList = [stock_dict1 [i][0] for i in sorted(stock_dict1.keys()) ]
       myList1 = [(i,stock_dict1 [i][0]) for i in sorted(stock_dict1.keys()) ]
       #print(myList1)
       datelist = (list(stock_dict1.values())[1])
       uplist = sorted(myList1,key=lambda x: x[1])
       revlist = sorted(myList1,key=lambda x: x[1], reverse=True)
       
       # uplist = sorted(myList1,key=itemgetter(1))
       # revlist = sorted(myList1,key=itemgetter(1), reverse=True)
       
       myList.sort()
       myList1.sort()

       print('inside stocks')
       cap0 = numerize.numerize(500000000000,4)
       cap4 = numerize.numerize(4000000000000,4)
       cap3 = numerize.numerize(3000000000000,4)
       cap2 = numerize.numerize(2000000000000,4)
       cap1 = numerize.numerize(1000000000000,4)
       print(f'cap3 is {cap3}')
       onetlist = []
       twotlist = []
       threetlist = []
       bblist = []
       btlist = []
       for x,y in stock_dict1.items():
           if 1000000000000 <= y[0] <= 2000000000000:
            #print (f"The company with tickr {x} are in the  ${cap1} Club")
            onetlist.append(x)
            #print (f"{i}. {x} with the value ${y}")
         #valueprev = value
           if 2000000000000 <= y[0] <= 3000000000000:
            #print (f"The company with tickr {x} are in the  ${cap2} Club")
            twotlist.append(x)
           if 500000000000 <= y[0] <= 1000000000000:
            #print (f"The company with tickr {x} are in the  ${cap0} Club")
            bblist.append(x)
           if 0 <= y[0] <= 500000000000:
            #print (f"The company with tickr {x} are in the  SUB ${cap0} Club")
            btlist.append(x)
           if 3000000000000 < y[0]:
            #print (f"The company with tickr {x} are in the  SUB ${cap3} Club")
            threetlist.append(x)

       print(f'{len(onetlist)} companies in the $ {cap1} Club & they are', onetlist)
       print(f'{len(twotlist)} companies in the $ {cap2} Club & they are', twotlist)
       print(f'{len(threetlist)} companies in the $ {cap3} Club & they are', threetlist)
       print(f'{len(bblist)}  companies in the $ {cap0} Club & they are ', bblist)
       print(f'{len(btlist)} companies in the SUB $ {cap0} Club & they are ', btlist)
       #print(f'The companies in the $ {cap1} Club are ', onelist)


       print(f'TOP most-valuable-company from the list as of {datelist[1]}\n')
       i = 1
       newlist = []
       newlist.append(f'TOP most-valuable-company from the list as of {datelist[1]}')
       for key,value in revlist:
         print (f"{i}. {key} with the value $ {numerize.numerize(value,4)}")
         newlist.append(f'{i}. {key} with the value $ {numerize.numerize(value,4)}')
         valueprev = value
         i = i + 1  
      
       print(f'Ascending order most-valuable-company from the list\n')
       i = len(uplist) 
       for key,value in uplist:
         print (f"{i}. {key} with the value $ {numerize.numerize(value,4)}")
         valueprev = value
         i = i - 1 
       #p1.diff(revlist)
       #newlist.append(None)
       #newlist.append(None)
       now1 = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
       now2 = datetime.datetime.now().strftime('%d-%m-%y')
       newlist.append('')
       newlist.append('')
       newlist.append('')
       newlist.append(f'The Market Capitalization as of {now2}')
       newlist.append('')
       newlist.append('')
       newlist.append(f'{len(threetlist)} companies in the $ {cap3} Club & they are {threetlist}')
       newlist.append(f'{len(twotlist)} companies in the $ {cap2} Club & they are {twotlist}')
       newlist.append(f'{len(onetlist)} companies in the $ {cap1} Club & they are {onetlist}')
       newlist.append(f'{len(bblist)}  companies in the $ {cap0} Club & they are {bblist}')
       newlist.append(f'{len(btlist)} companies in the SUB $ {cap0} Club & they are {btlist}')

       return newlist

    def diff(self,dict2):
       print(dict2)
       i = 1
       for key,value in dict2:
         print (f"{i}. {key} with the value ${numerize.numerize(value,3)}")  
         valueprev = value
         i = i + 1

    def getit(self,client11,list21,stock_dict2,apicount):
       #list2 = ["SNOW","BRK.B"]
       #self.list2 = list21
       print('inside getit')
       #print(stock_dict2)
       for x in list21:
         print(f'getting quote for {x}')
         aggs = client11.get_previous_close_agg(x)
         apicount += 1
         #details = client11.get_ticker_details(x)
         outstand1 = client11.get_ticker_details(x)
         apicount += 1
         detailcap = outstand1.market_cap
         print(f'{x} marketcap is{detailcap}')
         if (apicount % 5 == 0):
            time.sleep(60)
         if detailcap==None:
            print('insode details')
            p4 = "awk \'{split($0,a,\",\");print (a[2])}\'"
            l23 = subprocess.run(['echo "{}" | {}'.format(aggs[0],p4)], capture_output=True, shell=True, text=True, check=False)
            print(l23)
            p5 = l23.stdout
            print(p5)
            r4 = "awk \'{split($0,a,\"=\");print (a[2])}\'"
            l24 = subprocess.run(['echo "{}" | {}'.format(p5,r4)], capture_output=True, shell=True, text=True, check=False)
            print(l24)
            p6 = l24.stdout
            print(p6)
            share_outstand = outstand1.share_class_shares_outstanding
            num1 = float(p6)
            num2 = float(share_outstand)
            marketcap = ( num1 * num2 )
            print(marketcap)
            detailcap = marketcap

         aggs1 = aggs[0]
         print(f'aggs1 is {aggs1}')
         pl = subprocess.run(['echo "{}" | grep timestamp'.format(aggs1)], capture_output=True, shell=True, text=True, check=False)
         l21 = pl.stdout
         p3 = "awk \'{split($0,a,\",\"); print a[6]}\'"
         l22 = subprocess.run(['echo "{}" | {}'.format(l21,p3)], capture_output=True, shell=True, text=True, check=False)
         l23 = l22.stdout
         p4 = "awk \'{split($0,a,\"=\"); print a[2]}\'"
         l23 = subprocess.run(['echo "{}" | {}'.format(l23,p4)], capture_output=True, shell=True, text=True, check=False)
         p5 = l23.stdout
         now1 = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
         now2 = datetime.datetime.now().strftime('%d-%m-%y')
         t21 = p5[:10]
         t1 = int(t21)
         print(f't1 is {t1}')
         t2 = time.ctime(t1)
         stock_dict2 = { **stock_dict2, x : [ detailcap , t2 ] }
         #p1.printout()
         #print(stock_dict2)
       return stock_dict2

#main BEGINS
#if __name__ == "__main__":
def handler(event, context):
 #r2 = imagels()
 #return r2
 print('inside handler')
 p1 = fetch()
 print (f'client is {p1}')
 apicount = 0
 API_KEY = os.getenv('API_POLYGON') 
 #API_KEY = "insert-api-key"
 client1 = p1.polyget(API_KEY)
 apicount += 1
 aggs = []
 #list1 = ["META", "NVDA","AAPL","GOOG", "AMZN"]
 list1 = ["META", "NVDA","AAPL","GOOG", "AMZN","TSLA","BRK.B","MSFT","AVGO","NFLX","SNOW","DE","CTSH","ACN","CRWV"]
 stock_dict = {}
 new24_dict = p1.getit(client1,list1,stock_dict,apicount)
 rt = p1.ascend(new24_dict)
# p1.printout()
 return rt
