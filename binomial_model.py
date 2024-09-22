import numpy as np
import datetime, time
import webscraper
import work_days
import math
from scipy.stats import norm

global symbol,n

K=input('Strike price:\n')
r=input('Risk free interest rate in percentage:\n')
r=float(r)/100
m=raw_input("Maturity date as'YYYYMMDD':\n")
key_press=raw_input("Source of data, press 'Y' for Yahoo and 'G' for Google:\n")
symbol = raw_input("Insert the company's symbol:\n")
n = input("Number of days of data you want to consider? Insert '1' for time equal to the duration of the option:\n")
k=input('Number of binomial steps:\n')

def change_input():
    t_1 = datetime.datetime(int(time.strftime("%Y")),int(time.strftime("%m")),int(time.strftime("%d")))
    t_1 = time.mktime(t_1.timetuple())
    if n== 1:
        t_2 = datetime.datetime(int(m[0:4]),int(m[4:6]),int(m[6:8]))
        t_2 = time.mktime(t_2.timetuple())
        t =(t_2-t_1)        
    elif isinstance(n,int):
        t = n*24*3600
    t_0 = t_1-t
    start_date = time.strftime('%Y%m%d', time.localtime(t_0))
    end_date = time.strftime('%Y%m%d', time.localtime(t_1))   
    return symbol,start_date,end_date

def volatility_calc():
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
    print ' '*60,'Volatility Calculation'
    print '-'*167
    print '\t','Date','\t'*2,'Closing Stock Price','\t','Price Relative','\t'*2,'Daily return','\t'*3,'(u_i)^2'
    print '\t'*3,' '*3,'(in dollars)',' '*4,'\t',' ','S_i/S_(i-1)',' ','\t','u_i=ln(S_i/S_(i-1))'
    print '-'*167
    if key_press=='Y':        
        if len(data[0])==12:
            print ' '*4,data[0],'\t'*2,data[1]
        elif len(data[0])==11:
            print ' '*5,data[0],'\t'*2,data[1]            
        i=2
        while i < len(data):
            if len(data[i])==12:
                print ' '*4, data[i], '\t'*2, data[i+1],'\t'*2, "%.12f"%list_1[int(i/2)-1], '\t'*2,"%.13f"%list_2[int(i/2)-1],'\t'*2,"%.15f"%list_3[int(i/2)-1]
            elif len(data[i])==11:
               print ' '*5, data[i], '\t'*2, data[i+1],'\t'*2, "%.12f"%list_1[int(i/2)-1], '\t'*2, "%.13f"%list_2[int(i/2)-1],'\t'*2,"%.15f"%list_3[int(i/2)-1] 
            i=i+2
    elif key_press=='G':
        if len(data[0])==13:
            print ' '*4,data[0][0:-1],'\t'*2,data[1][0:-1]
        elif len(data[0])==12:
            print ' '*5,data[0][0:-1],'\t'*2,data[1][0:-1]            
        i=2
        while i < len(data):
            if len(data[i])==13:
                print ' '*4, data[i][0:-1], '\t'*2, data[i+1][0:-1],'\t'*2, "%.12f"%list_1[int(i/2)-1], '\t'*2, "%.13f"%list_2[int(i/2)-1],'\t'*2,"%.15f"%list_3[int(i/2)-1]
            elif len(data[i])==12:
                print ' '*5, data[i][0:-1], '\t'*2, data[i+1][0:-1],'\t'*2, "%.12f"%list_1[int(i/2)-1], '\t'*2, "%.13f"%list_2[int(i/2)-1],'\t'*2,"%.15f"%list_3[int(i/2)-1]
            i=i+2        
    print '-'*167
    print '\t'*9, sum_0,' '*16, sq_sum        
    n = len(data)/2
    x = (1/float(n-1))*(sq_sum -(1/float(n))*((sum_0)**2))
    s = math.sqrt(x)
    sigma = s*math.sqrt(252)    
    print 'The standard deviation of daily price changes is:',s*100,'%'
    price_calc(sigma)

def american_put(delta_t,u,d,p,S_0,K,r,sigma,k):
    m=np.zeros((1,k+1))   #Forms 1xk+1 matrix
    i=k
    j=0
    while j<=k:
        m[0][j]=max(K-(u**(k-2*j))*S_0,0)
        j=j+1
    i=k-1
    while i >= 0:
        j=0
        while j<=i:
            m[0][j]=max(K-(u**(i-2*j))*S_0,math.exp((-r*delta_t)/float(100))*(p*m[0][j]+(1-p)*m[0][j+1]),0)
            j=j+1
        i=i-1
    return m[0][0]

def american_call(delta_t,u,d,p,S_0,K,r,sigma,k):
    m=np.zeros((1,k+1))
    i=k
    j=0
    while j<=k:
        m[0][j]=max((u**(k-2*j))*S_0 - K,0)
        j=j+1
    i=k-1
    while i >= 0:
        j=0
        while j<=i:            
            m[0][j]=max((u**(i-2*j))*S_0 - K,math.exp((-r*delta_t)/float(100))*(p*m[0][j]+(1-p)*m[0][j+1]),0)
            j=j+1
        i=i-1
    return m[0][0]

def price_calc(sigma):
    t_int = datetime.datetime(int(time.strftime("%Y")),int(time.strftime("%m")),int(time.strftime("%d")))
    t_int = time.mktime(t_int.timetuple())
    t_int = time.strftime('%Y%m%d', time.localtime(t_int))
    t = work_days.work_days(t_int,m)
    T = t/252 
    print 'The life of the option is T:', T, 'years'
    S_0 = webscraper.yahoo_stock_quote(symbol)
    S_0 = float(S_0)    
    delta_t = float(T)/k
    u = math.exp(sigma*math.sqrt(delta_t))
    d = 1/float(u)
    p = float(math.exp(r*delta_t)-d)/(u-d)
    C = american_call(delta_t,u,d,p,S_0,K,r,sigma,k)
    P = american_put(delta_t,u,d,p,S_0,K,r,sigma,k)
    print 'The price of American call is:\n',C
    print 'The price of American put is:\n',P
    
if key_press=='Y':
    symbol,start_date,end_date=change_input()    
    data=webscraper.yahoo_historical_data(symbol,start_date,end_date)    
    volatility_calc()
elif key_press=='G':
    symbol,start_date,end_date=change_input()    
    data=webscraper.google_historical_data(symbol,start_date,end_date)    
    volatility_calc()
else:
    print 'Invalid input.'
    


        
       
    
