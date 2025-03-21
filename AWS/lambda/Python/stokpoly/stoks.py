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
import streamlit as st
import pandas as pd
import numpy as np

load_dotenv()

class fetch:
        #apple = yf.Ticker("AAPL")
    def polyget(self,API):
       client = RESTClient(API)
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
       #print(myList)

       uplist = sorted(myList1,key=lambda x: x[1])
       revlist = sorted(myList1,key=lambda x: x[1], reverse=True)
       
       myList.sort()
       myList1.sort()

       print(f'TOP most-valuable-company from the list\n')
       i = 1
       for key,value in revlist:
         print (f"{i}. {key} with the value $ {numerize.numerize(value,4)}")
         valueprev = value
         i = i + 1  
       p1.strmlit(revlist)
 
       print(f'Ascending order most-valuable-company from the list\n')
       i = len(uplist) 
       for key,value in uplist:
         print (f"{i}. {key} with the value $ {numerize.numerize(value,4)}")
         valueprev = value
         i = i - 1 
       #p1.diff(revlist)

    def diff(self,dict2):
       print(dict2)
       i = 1
       for key,value in dict2:
         print (f"{i}. {key} with the value ${numerize.numerize(value,3)}")  
         valueprev = value
         i = i + 1

    def getit(self,client11,list21,stock_dict2):
       #list2 = ["SNOW","BRK.B"]
       #self.list2 = list21
       #print(stock_dict2)
       for x in list21:
         aggs = client11.get_previous_close_agg(x)
         details = client11.get_ticker_details(x)
         detailcap = details.market_cap
         aggs1 = aggs[0]
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
         stock_dict2 = { **stock_dict2, x : [ detailcap , now2 ] }
  #p1.printout()
       #print(stock_dict2)
       return stock_dict2

    def strmlit(self,dict_s):
       print(f'TOP most-valuable-company from the list\n')
       i = 1
       serial = []
       tikr = []
       ations = []
       placeholder1 = st.empty()
       my_table = st.empty() 
       for key,value in dict_s:
         value2 = numerize.numerize(value,4)
         serial.append(i)
         tikr.append(key)
         ations.append(value)
         i = i + 1
       df1 = pd.DataFrame({"serial": serial,"ticker": tikr,"ations": ations})
       print(f"df1 is {df1}")
       #my_table.add_rows(df1)
         # print (f"{i}. {key} with the value $ {numerize.numerize(value,4)}")
       valueprev = value
       st.dataframe(df1,hide_index=True)
    
    def pbar(self): 
       # Add a placeholder
       placeholder1 = st.empty()
       placeholder1.markdown("Fetching ticker valuations...")
       bar = st.progress(1)
       for i in range(61):
          # Update the progress bar with each iteration.
          time.sleep(1)
          prog1 = i/61
          prog1cent = prog1 * 100
          prog2cent = round(prog1cent)
          bar.progress(prog2cent)
       placeholder1.markdown("...and now we\'re done!")
       time.sleep(1) 
       placeholder1.empty()
       bar.empty()
       

#main BEGINS
if __name__ == "__main__":
 p1 = fetch()
 #print (f'client is {p1}')
 API_KEY = os.getenv('API_POLYGON') 
 #API_KEY = "insert-api-key"
 client1 = p1.polyget(API_KEY)

 aggs = []
 #list1 = ["META", "NVDA","AAPL"]
 stock_dict = {}
 list1 = ["AAPL", "NVDA", "META", "AMZN", "GOOG" ]
 new24_dict = p1.getit(client1,list1,stock_dict)
 list2 = ["SNOW","BRK.B","LLY","AVGO","DE"]
 #time.sleep(60)
 p1.pbar()
 new25_dict = p1.getit(client1,list2,new24_dict)
 p1.ascend(new25_dict)
# p1.strmlit(new25_dict)
