import datetime, time
import webscraper
import work_days
import math
from scipy.stats import norm

global symbol

def change_input(m,n_1):
    t_1 = datetime.datetime(int(time.strftime("%Y")),int(time.strftime("%m")),int(time.strftime("%d")))
    t_1 = time.mktime(t_1.timetuple())
    if n_1 == 1:
        t_2 = datetime.datetime(int(m[0:4]),int(m[4:6]),int(m[6:8]))
        t_2 = time.mktime(t_2.timetuple())
        t =(t_2-t_1)        
    elif isinstance(n_1,int):
        t = n_1*24*3600
    t_0 = t_1-t
    start_date = time.strftime('%Y%m%d', time.localtime(t_0))
    end_date = time.strftime('%Y%m%d', time.localtime(t_1))   
    return start_date,end_date

def volatility(source, symbol, m, n_1):
    if source == 1:
        start_date,end_date=change_input(m,n_1)
        data = webscraper.yahoo_historical_data(symbol,start_date,end_date)
        S_0 = webscraper.yahoo_stock_quote(symbol)
        S_0 = float(S_0)
    else:
        start_date,end_date=change_input(m,n_1)
        data=webscraper.google_historical_data(symbol,start_date,end_date)
        S_0 = webscraper.google_stock_quote(symbol)
        S_0 = float(S_0)
        
    list_1 = []
    list_2 = []
    list_3 = []
    sum_0 = 0
    sq_sum = 0
    i=0
    while i < len(data)-2:
        x = float(data[i+1])/float(data[i+3])
        y = math.log(float(data[i+1])/float(data[i+3]))
        z = (math.log(float(data[i+1])/float(data[i+3])))**2
        list_1.append(x)
        list_2.append(y)
        list_3.append(z)
        sum_0 = sum_0 + list_2[int(i/2)]
        sq_sum = sq_sum + list_3[int(i/2)]       
        i=i+2
            
    n = len(data)/2
    x = (1/float(n-1))*(sq_sum -(1/float(n))*((sum_0)**2))
    s = math.sqrt(x)
    sigma = s*math.sqrt(252)
    t_int = datetime.datetime(int(time.strftime("%Y")),int(time.strftime("%m")),int(time.strftime("%d")))
    t_int = time.mktime(t_int.timetuple())
    t_int = time.strftime('%Y%m%d', time.localtime(t_int))
    t = work_days.work_days(t_int,m)
    T = t/252   
    return S_0, T, sigma

 
    
