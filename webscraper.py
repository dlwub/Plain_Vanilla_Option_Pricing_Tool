import urllib
from bs4 import BeautifulSoup
import datetime,time
from time import strptime
import work_days

global n
#Stock quotes from Google
def google_stock_quote(symbol):
    url = 'http://www.google.com/finance?q=%s'%symbol
    source=urllib.urlopen(url).read()
    soup=BeautifulSoup(source)
    return soup.findAll('span',{'class':'pr'})[0].text

#Historical data from Google
def google_historical_data(symbol,start,end):
    n = work_days.work_days(start,end)
    start = datetime.date(int(start[0:4]),int(start[4:6]), int(start[6:8]))
    end = datetime.date(int(end[0:4]),int(end[4:6]), int(end[6:8]))
    data = []
    data = google_url(data,n,symbol,start,end)
    return data

def google_url(data,n,symbol,start,end):    
    url = 'http://www.google.com/finance/historical?q=%s&'%symbol +\
          urllib.urlencode({'startdate': start.strftime('%b %d, ' '%Y'),
                            'enddate':end.strftime('%b %d, ' '%Y')})
    source=urllib.urlopen(url).read()
    soup=BeautifulSoup(source)
    tr=soup.findAll('tr')
    i=0
    while i<len(tr)-5:
        x=soup.findAll('td',{'class':'lm'})[i].text
        data.append(x)
        y=soup.findAll('td',{'class':'rgt rm'})[i].previous_sibling.text
        data.append(y)
        i=i+1    
    while n-2 > len(data)/2:   #Data of the last one or two dates may not be available
        mo=str(data[-2])       # Taking the last date in the list 'data'        
        if len(mo)==12:
            t = datetime.datetime(int(mo[7:11]), strptime(mo[0:3],'%b').tm_mon, int(mo[4]))        
        else:
            t = datetime.datetime(int(mo[8:12]), strptime(mo[0:3],'%b').tm_mon, int(mo[4:6])) 
        #Converting the last date in the list to seconds and subtracting 1 day        
        t = time.mktime(t.timetuple())-24*3600
        #Converting the number of seconds to date and assigning it to end
        end = time.strftime('%Y%m%d', time.localtime(t))
        end = datetime.date(int(end[0:4]),int(end[4:6]), int(end[6:8]))
        google_url(data,n,symbol,start,end)
    return data          
  
  
#Stock quotes from Yahoo
def yahoo_stock_quote(symbol):
    url = 'http://finance.yahoo.com/q?s=%s'%symbol
    source=urllib.urlopen(url).read()
    soup=BeautifulSoup(source)
    return soup.findAll('span',{'class':'time_rtq_ticker'})[0].text

#Historical data from Yahoo
def yahoo_historical_data(symbol,start,end):
    n = work_days.work_days(start,end)
    data=[]
    data = yahoo_url(data,n,symbol,start,end)
    return data

def yahoo_url(data,n,symbol,start,end):
    url = 'http://finance.yahoo.com/q/hp?s=%s&'%symbol +\
          'a=%s&' % str(int(start[4:6]) - 1) + \
          'b=%s&' % str(int(start[6:8])) + \
          'c=%s&' % str(int(start[0:4])) + \
          'd=%s&' % str(int(end[4:6]) - 1) + \
          'e=%s&' % str(int(end[6:8])) + \
          'f=%s&' % str(int(end[0:4])) + \
          'g=d'
    source=urllib.urlopen(url).read()
    soup=BeautifulSoup(source)
    td=soup.findAll('td',{'class':'yfnc_tabledata1'})    
    i=0
    j=0
    while i< 2*((len(td)-1)/7):
        x=soup.findAll('td',{'class':'yfnc_tabledata1'})[j].text
        data.append(x)
        i=i+1
        if i%2==0:
            j=j+3
        else:
            j=j+4   
    
    while n-2 > len(data)/2:     #Data of the last one or two dates may not be available
        mo = str(data[-2])       # Taking the last date in the list 'data'        
        if len(mo)==11:
            t = datetime.datetime(int(mo[7:]), strptime(mo[0:3],'%b').tm_mon, int(mo[4]))       
        else:
            t = datetime.datetime(int(mo[8:]), strptime(mo[0:3],'%b').tm_mon, int(mo[4:6]))
        #Converting the last date in the list to seconds and subtracting 1 day
        t = time.mktime(t.timetuple())-24*3600
        #Converting the number of seconds to date and assigning it to end
        end = time.strftime('%Y%m%d', time.localtime(t))        
        yahoo_url(data,n,symbol,start,end)
    return data



            
       
   


