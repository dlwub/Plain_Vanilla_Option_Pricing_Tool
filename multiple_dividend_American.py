import numpy as np
import math

def american_put(delta_t,u,d,p,S_0,K,r,sigma,k):
    global n,m
    m=np.zeros((1,k+1))   #Forms (1)x(k+1) matrix
    i=k
    j=0
    while j<=k:
        m[0][j]=max(K-(u**(k-2*j))*S_0,0)
        j=j+1
    i=k-1
    while i >= 0:
        j=0
        while j<=i:            
            m[0][j]=max(K-(u**(i-2*j))*S_0, math.exp(-r*delta_t)*(p*m[0][j]+(1-p)*m[0][j+1]))
            j=j+1            
        if i==z[2*(n-1)]:            
            row_replace(i)                  
        i=i-1        
    return m[0][0]

def american_call(delta_t,u,d,p,S_0,K,r,sigma,k):
    global n,m   
    m=np.zeros((1,k+1))
    i=k
    j=0
    while j<=k:
        m[0][j] = max((u**(k-2*j))*S_0 - K,0)
        j=j+1
    i=k-1
    while i >= 0:
        j=0
        while j<=i:
            m[0][j]=max((u**(i-2*j))*S_0 - K, math.exp(-r*delta_t)*(p*m[0][j]+(1-p)*m[0][j+1]))
            j=j+1
        if i==z[2*(n-1)]: #Ex-dividend date
            row_replace(i)          
        i=i-1       
    return m[0][0]

def row_replace(i):
    global n,m      
    j=0
    while j< i:
        slope = (m[0][j+1] - m[0][j])/float(S_0*(u**(i-2*j))*(u**(-2)-1))
        S = S_0*(u**(i-2*j)) - z[(2*n)-1]
        m[0][j] = slope*(S-S_0*(u**(i-2*j))) + m[0][j]        
        j=j+1
    m[0][i] = slope*(S_0*(u**(-i)) - z[(2*n)-1]) + m[0][i]
    if n > 1:
        n = n-1
    return 

def take_input(delta_t):
    global n
    n = input('Number of dividends:\n')
    i = 0
    z = []
    while i < n:
        x = input('Insert time t%d:\n'%(i+1))        
        x = math.floor(float(x)/delta_t) 
        z.append(x)
        y = input('Insert dividend D%d:\n'%(i+1))
        z.append(y)
        i = i+1    
    return n,z

S_0 = input('Current stock price:\n')
K = input('Strike price:\n')
r = input('Risk free interest rate in percentage:\n')
r = r/float(100)
sigma = input('Volatility:\n')
T = input('Length of option life:\n')
k = input('Number of binomial steps:\n')
delta_t = float(T)/k
n,z = take_input(delta_t)
u = math.exp(sigma*math.sqrt(delta_t))
d = 1/float(u)
p = float(math.exp(r*delta_t)-d)/(u-d)
option_type = raw_input("Press 'c' for call and 'p' for put:\n")
if option_type=='c':
    C = american_call(delta_t,u,d,p,S_0,K,r,sigma,k)
    print 'The price of American call is:\n',C
elif option_type=='p':
    P = american_put(delta_t,u,d,p,S_0,K,r,sigma,k)
    print 'The price of American put is:\n',P
