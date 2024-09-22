import numpy as np
import math

def boundary_put(delta_t,u,d,p,S_0,K,r,sigma,k):
    global n,m
    m=np.zeros((1,k+1))   #Forms (1)x(k+1) matrix
    i=k
    j=0
    S=[]
    B=[]
    P=[]
    while j<=k:
        m[0][j] = max(K-(u**(k-2*j))*S_0,0)
        j = j+1
    i = k-1
    while i >= 0:
        j=0
        while j<=i:
            FV = math.exp(-r*delta_t)*(p*m[0][j]+(1-p)*m[0][j+1])
            m[0][j] = max(K-(u**(i-2*j))*S_0,FV)
            if m[0][j]==K-(u**(i-2*j))*S_0:
                S.append(j)
                P.append(FV)
            j=j+1
        if len(S)>0:
            t = min(S)
            FV = P[S.index(t)]
            w_1 = (m[0][t-1] + S_0*(u**(i-2*t+2))-K)/float(m[0][t-1]-FV + S_0*(u**(i-2*t))*(u**2-1))
            w_2 = (-FV + K - S_0*(u**(i-2*t)))/float(m[0][t-1]-FV + S_0*(u**(i-2*t))*(u**2-1))
            b = w_1*(S_0*(u**(i-2*t)))+ w_2*(S_0*(u**(i-2*t+2)))
            B.append(b)
        i=i-1
    B = B[::-1] 
    l=1
    while l < len(B)-2:
        B[l]= (B[l-1]/float(4)) + (B[l]/float(2)) + (B[l+1]/float(4))
        l=l+1
    if len(B)>2:
        B[len(B)-2]= (B[len(B)-3]/float(4)) + (B[len(B)-2]/float(2)) + (K/float(4))
        B[len(B)-1]= K
    return B 
      

def boundary_call(delta_t,u,d,p,S_0,K,r,sigma,k):
    global n,m
    m=np.zeros((1,k+1))   #Forms (1)x(k+1) matrix
    i=k
    j=0
    S=[]
    B=[]
    P=[]
    while j<=k:
        m[0][j] = max((u**(k-2*j))*S_0 - K,0)
        j = j+1
    i = k-1
    while i >= 0:
        j=0
        while j<=i:
            FV = math.exp(-r*delta_t)*(p*m[0][j]+(1-p)*m[0][j+1])
            m[0][j] = max((u**(i-2*j))*S_0 - K,FV)
            if m[0][j]==(u**(i-2*j))*S_0 - K:
                S.append(j)
                P.append(FV)
            j=j+1        
        if len(S)>0:
            t = max(S)
            FV = P[S.index(t)]
            w_1 = (m[0][t+1] + K - S_0*(u**(i-2*t-2)))/float(m[0][t+1] - FV + S_0*(u**(i-2*t))*(u**(-2)-1))
            w_2 = (-FV + S_0*(u**(i-2*t))-K)/float(m[0][t+1] - FV + S_0*(u**(i-2*t))*(u**(-2)-1))
            b = w_1*(S_0*(u**(i-2*t)))+ w_2*(S_0*(u**(i-2*t+2)))
            B.append(b)            
        i=i-1
    B = B[::-1] 
    l=1
    while l < len(B)-2:
        B[l]= (B[l-1]/float(4)) + (B[l]/float(2)) + (B[l+1]/float(4))
        l=l+1
    if len(B)>2:
        B[len(B)-2]= (B[len(B)-3]/float(4)) + (B[len(B)-2]/float(2)) + (K/float(4))
        B[len(B)-1]= K
    return B


def take_input(delta_t):
    global n
    n = input('Number of dividends:\n')
    i = 0
    z = []
    while i < n:
        x = input('Insert time t%d:\n'%(i+1))
        x = float(x)/delta_t
        x = math.ceil(x) #Takes the smallest integer greater than x
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
    boundary_call(delta_t,u,d,p,S_0,K,r,sigma,k)    
elif option_type=='p':
    boundary_put(delta_t,u,d,p,S_0,K,r,sigma,k)
    

