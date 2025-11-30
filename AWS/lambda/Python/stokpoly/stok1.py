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
from decimal import *

load_dotenv()

class fetch:
    cap0 = numerize.numerize(500000000000,4)
    cap7 = numerize.numerize(7000000000000,4)
    cap6 = numerize.numerize(6000000000000,4)
    cap5 = numerize.numerize(5000000000000,4)
    cap4 = numerize.numerize(4000000000000,4)
    cap3 = numerize.numerize(3000000000000,4)
    cap2 = numerize.numerize(2000000000000,4)
    cap1 = numerize.numerize(1000000000000,4)
    cap31 = float(1000000000000)
    cap32 = float(2000000000000)
    cap33 = float(3000000000000)
    cap34 = float(4000000000000)
    cap35 = float(5000000000000)
    cap36 = float(6000000000000)
    cap37 = float(7000000000000)
    cap30 = float(500000000000)
   #print(f'cap3 is {cap3}')
    onetlist = []
    twotlist = []
    threetlist = []
    fourlist = []
    fivelist = []
    sixlist = []
    sevenlist = []
    bblist = []
    btlist = []
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
       
       print('The Leadership Board of the Most-Valuable companies are (f-Floor price; c-Ceiling price)')
       print(f'{len(onetlist)} companies in the $ {cap1} Club & they are', onetlist)
       print(f'{len(twotlist)} companies in the $ {cap2} Club & they are', twotlist)
       print(f'{len(threetlist)} companies in the $ {cap3} Club & they are', threetlist)
       print(f'{len(fourlist)} companies in the $ {cap4} Club & they are', fourlist)
       print(f'{len(bblist)}  companies in the $ {cap0} Club & they are ', bblist)
       print(f'{len(btlist)} companies in the SUB $ {cap0} Club & they are ', btlist)
       #print(f'The companies in the $ {cap1} Club are ', onelist)
    
    def newlistprint(self,*args):
        newlist0 = args[0]
        print(f'in newslistprint {args}')
        print(f'')
        if (len(args)) == 1:
           newlist0.append('')
           newlist0.append('')
        else:
            if (len(args[1])) > 0:
             newlist0.append(f'{len(args[1])} companies in the $ {args[2]} Club & they are {args[1]}')   
        return newlist0     

    def ascend(self,stock_dict1):
       print(f'stock disct is {stock_dict1}')
       print(f'stock dict1 values is {stock_dict1.values()}')
       print(list(stock_dict1.values())[1])
       myList = [stock_dict1 [i][0] for i in sorted(stock_dict1.keys()) ]
       myList1 = [(i,stock_dict1 [i][0],stock_dict1 [i][2], stock_dict1 [i][3]) for i in sorted(stock_dict1.keys()) ]
       print(f'mylist1 is {myList1}')
       datelist = (list(stock_dict1.values())[1])
       uplist = sorted(myList1,key=lambda x: x[1])
       print(f'uplist is {uplist}')
       uplist1 = sorted(myList1,key=lambda x: x[0])
       uplist2 = sorted(myList1,key=lambda x: x[2])
       print(f'uplist1 is {uplist1}')
       print(f'uplist2 is {uplist2}')
       revlist = sorted(myList1,key=lambda x: x[1], reverse=True)
      
       # uplist = sorted(myList1,key=itemgetter(1))
       # revlist = sorted(myList1,key=itemgetter(1), reverse=True)
      
       print(f'revlist is {revlist}')
       myList.sort()
       myList1.sort()
       cin = 0
       c1 = 0
       for t in revlist:
           total1 = float(c1 + t[1])
           c1 = total1
           cin = cin + 1
           if cin >= 10:
               total2 = numerize.numerize(total1,4)
               break
           if cin == 7:
               cin7 = 7
               total3 = numerize.numerize(total1,4) 
           if cin == 3:
               cin3 = 3
               total4 = numerize.numerize(total1,4)

       #print(f'the total Market cap of the Top {cin} companies in the US is {total2}')

       for x in revlist:
           a1 = float(x[2])
           fp1 = float(x[3])
           if 1000000000000 <= x[1] < 2000000000000:
            reqprice = ( self.cap31 / fp1 )
            cprice = ( self.cap32 / fp1 )
            reqprice1 = Decimal(reqprice)
            reqprice2 = format(reqprice1,'.7')
            cprice1 = Decimal(cprice)
            cprice2 = format(cprice1,'.7')
            res = [i for i in self.onetlist if x[0] in i]
            if res:
              print(f'already added to list')
            else:
              self.onetlist.append(f'{x[0]} f/c - $ {reqprice2} / $ {cprice2}')
           if 2000000000000 <= x[1] < 3000000000000:
            reqprice = ( self.cap32 / fp1 )
            cprice = ( self.cap33 / fp1 )
            reqprice1 = Decimal(reqprice)
            reqprice2 = format(reqprice1,'.7')
            cprice1 = Decimal(cprice)
            cprice2 = format(cprice1,'.7')
            res = [i for i in self.twotlist if x[0] in i]
            if res: 
              print(f'already added to list')
            else:
              self.twotlist.append(f'{x[0]} f/c - $ {reqprice2} / $ {cprice2}')
           if 500000000000 <= x[1] < 1000000000000:
            reqprice = ( self.cap30 / fp1 )
            cprice = ( self.cap31 / fp1 )
            reqprice1 = Decimal(reqprice)
            reqprice2 = format(reqprice1,'.7')
            cprice1 = Decimal(cprice)
            cprice2 = format(cprice1,'.7')
            res = [i for i in self.bblist if x[0] in i]
            if res:
              print(f'already added to list')
            else:
              self.bblist.append(f'{x[0]} f/c - $ {reqprice2} / $ {cprice2}')
           if 0 <= x[1] < 500000000000:
            cprice = ( self.cap30 / fp1 )
            cprice1 = Decimal(cprice)
            cprice2 = format(cprice1,'.7')
            res = [i for i in self.btlist if x[0] in i]
            if res:
              print(f'already added to list')
            else:
              self.btlist.append(f'{x[0]} Ceiling - $ {cprice2}')
           if 3000000000000 <= x[1] < 4000000000000:
            reqprice = ( self.cap33 / fp1 )
            cprice = ( self.cap34 / fp1 )
            reqprice1 = Decimal(reqprice)
            reqprice2 = format(reqprice1,'.7')
            cprice1 = Decimal(cprice)
            cprice2 = format(cprice1,'.7')
            res = [i for i in self.threetlist if x[0] in i]
            if res:
              print(f'already added to list')
            else:
              self.threetlist.append(f'{x[0]} f/c - $ {reqprice2}/$ {cprice2}')
           if 4000000000000 <= x[1] < 5000000000000:
            reqprice = ( self.cap34 / fp1 )
            cprice = ( self.cap35 / fp1 )
            reqprice1 = Decimal(reqprice)
            reqprice2 = format(reqprice1,'.7')
            cprice1 = Decimal(cprice)
            cprice2 = format(cprice1,'.7')
            res = [i for i in self.fourlist if x[0] in i]
            if res:
              print(f'already added to list')
            else:
              self.fourlist.append(f'{x[0]} f/c - $ {reqprice2}/$ {cprice2}')

           if 5000000000000 <= x[1] < 6000000000000:
            reqprice = ( self.cap35 / fp1 )
            cprice = ( self.cap36 / fp1 )
            reqprice1 = Decimal(reqprice)
            reqprice2 = format(reqprice1,'.7')
            cprice1 = Decimal(cprice)
            cprice2 = format(cprice1,'.7')
            res = [i for i in self.fivelist if x[0] in i]
            if res:
              print(f'already added to list')
            else:
              self.fivelist.append(f'{x[0]} f/c - $ {reqprice2}/$ {cprice2}')

           if 6000000000000 <= x[1] < 7000000000000:
            reqprice = ( self.cap36 / fp1 )
            cprice = ( self.cap37 / fp1 )
            reqprice1 = Decimal(reqprice)
            reqprice2 = format(reqprice1,'.7')
            cprice1 = Decimal(cprice)
            cprice2 = format(cprice1,'.7')
            res = [i for i in self.sixlist if x[0] in i]
            if res:
              print(f'already added to list')
            else:
              self.sixlist.append(f'{x[0]} f/c - $ {reqprice2}/$ {cprice2}')


       print(f'TOP most-valuable-company from the list as of {datelist[1]}\n')
       i = 1
       newlist = []
       newlist.append(f'TOP most-valuable-company from the list as of {datelist[1]}')
       for x in revlist:
         print (f"{i}. {x[0]} @ {x[2]} with the value $ {numerize.numerize(x[1],4)}")
         newlist.append(f'{i}. {x[0]} @ {x[2]} closing with the value $ {numerize.numerize(x[1],4)}')
         i = i + 1  
       now1 = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
       now2 = datetime.datetime.now().strftime('%d-%m-%y')
       newlist.append(f'')
       if cin >= 10:
          newlist.append(f'the total Market cap of the Top {cin} companies in the US is $ {total2}' )
       if cin >= 7:   
          newlist.append(f'the total Market cap of the Top {cin7} companies in the US is $ {total3}')
       if cin >= 3:
          newlist.append(f'the total Market cap of the Top {cin3} companies in the US is $ {total4}')
       #print(f'Ascending order most-valuable-company from the list\n')
       #i = len(uplist) 
       #for key,value in uplist:format(cprice1,'.7')
       #  print (f"{i}. {key} with the value $ {numerize.numerize(value,4)}")
       #@  valueprev = value
       #  i = i - 1 
       #p1.diff(revlist)
       #newlist.append(None)
       #newlist.append(None)
      # print(newlist)
       return newlist


    def diff(self,dict2):
       print(dict2)
       i = 1
       for key,value in dict2:
         print (f"{i}. {key} with the value ${numerize.numerize(value,3)}")  
         valueprev = value
         i = i + 1

    def companylist(self,listc):
       print(listc) 


    def getit(self,client11,list21,stock_dict2,apicount):
       #list2 = ["SNOW","BRK.B"]
       #self.list2 = list21
       print('inside getit')
       print(list21)
       for x in list21:
        print(f'getting quote for {x}')
        try:
          aggs = client11.get_previous_close_agg(x)
          p4 = "awk \'{split($0,a,\",\");print (a[2])}\'"
          l23 = subprocess.run(['echo "{}" | {}'.format(aggs[0],p4)], capture_output=True, shell=True, text=True, check=False)
          print(f'the aggs of 0  is {aggs[0]}')
          print(f'the aggs is {l23}')
          p5 = l23.stdout
          p53 = l23.stderr
        except: 
          print(f'error in ticker {x}')   
        else: 
         apicount += 1
         #details = client11.get_ticker_details(x)
         outstand1 = client11.get_ticker_details(x)
         #print(f'outstand values {outstand1}')
         apicount += 1
         detailcap1 = outstand1.market_cap
         print(f'{x} marketcap is{detailcap1}')
         p4 = "awk \'{split($0,a,\",\");print (a[2])}\'"
         l23 = subprocess.run(['echo "{}" | {}'.format(aggs[0],p4)], capture_output=True, shell=True, text=True, check=False)
         print(l23)
         p5 = l23.stdout
         #print(p5)
         r4 = "awk \'{split($0,a,\"=\");print (a[2])}\'"
         l24 = subprocess.run(['echo "{}" | {}'.format(p5,r4)], capture_output=True, shell=True, text=True, check=False)
         #print(l24)
         p6 = l24.stdout
         #print(f'tickr is {p6}')
         #share_outstand = outstand1.share_class_shares_outstanding
         share_outstand = outstand1.weighted_shares_outstanding
         num1 = float(p6)
         num2 = float(share_outstand)
         marketcap = ( num1 * num2 )
         detailcap = marketcap
         print(f'marketcap is {marketcap}')
         if detailcap > 0:
            diff1 = float(detailcap1 - marketcap)
            print(f'the diff1 is $ {numerize.numerize(diff1,4)}')
         else:
            diff2 = float(marketcap - detailcap1)
            detailcap = detailcap1
            print(f'the diff2 is $ {numerize.numerize(diff2,4)}')

         if (apicount % 5 == 0):
            time.sleep(60)
         aggs1 = aggs[0]
         #print(f'aggs1 is {aggs1}')
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
         t2 = time.ctime(t1)
         stock_dict2 = { **stock_dict2, x : [ detailcap , t2 , num1, share_outstand] }
         #p1.printout()
         #print(stock_dict2)
       return stock_dict2

#main BEGINS
if __name__ == "__main__":
#def handler(event, context):
 #print('inside handler')
 p1 = fetch()
 #print (f'client is {p1}')
 apicount = 0
 API_KEY = os.getenv('API_POLYGON') 
 #API_KEY = "insert-api-key"
 try:
  client1 = p1.polyget(API_KEY)
  print(f'printing client is {client1}')
 except:
  print(f'looks like the Polygon API is down try after sometime')   
 else:
  apicount += 1
  aggs = []
  #list1 = ["META","NVDA","ORCL"]
  #list1 = ["PLTR","META","NVDA","AAPL","NVDA"]
  list1 = ["META", "NVDA","AAPL","GOOG", "AMZN","TSLA","BRK.B","MSFT","AVGO","NFLX","SNOW","DE","CTSH","ACN","CRWV", "PLTR", "ORCL", "JPM", "WMT","LLY","CAT"]
  stock_dict = {}
  new24_dict = p1.getit(client1,list1,stock_dict,apicount)
  rt = p1.ascend(new24_dict)
# p1.printout()
  rt = p1.newlistprint(rt)
  rt.append('The Leadership Board of the Most-Valuable companies are (f-Floor price; c-Ceiling price)')
  rt = p1.newlistprint(rt)
       #print(f'the newlist1 is {newlist}')
  rt = p1.newlistprint(rt,fetch.sevenlist,fetch.cap7)
  rt = p1.newlistprint(rt,fetch.sixlist,fetch.cap6)
  rt = p1.newlistprint(rt,fetch.fivelist,fetch.cap5)
  rt = p1.newlistprint(rt,fetch.fourlist,fetch.cap4)
  rt = p1.newlistprint(rt,fetch.threetlist,fetch.cap3)
  rt = p1.newlistprint(rt,fetch.twotlist,fetch.cap2)
  rt = p1.newlistprint(rt,fetch.onetlist,fetch.cap1)
  rt = p1.newlistprint(rt,fetch.bblist,fetch.cap0)
  rt = p1.newlistprint(rt,fetch.btlist,fetch.cap0)
  rt.append('The companies list that are considered in this ranking are **')
  rt.append(list1)
 print(f'rt is {rt}')
# return rt
