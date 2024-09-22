import numpy as np
from scipy import integrate
import math
from scipy.stats import norm
from scipy.integrate import quad
import blackscholes_version2


def sigma_adjust(S):
    global n
    s = math.log(S)
    i = 1
    D_t = 0
    while i <=n:
        D_t = D_t + z[2*i-1]*math.exp(-r*z[2*(i-1)])
        i = i+1
    x = math.log((K + D_t)*math.exp(-r*T))
    z1 = ((s-x)/float(sigma*math.sqrt(T)))+ ((sigma*math.sqrt(T))/float(2))
    z2 = z1 + ((sigma*math.sqrt(T))/float(2))
    sum1 = 0
    sum2 = 0
    i = 1
    while i <= n:
        sum1 = sum1 + z[2*i-1]*math.exp(-r*z[2*(i-1)])*(norm.cdf(z1)-norm.cdf(z1-sigma*z[2*(i-1)]/float(math.sqrt(T))))
        j = 1
        while j <= n:
            sum2 = sum2 + z[2*i-1]*z[2*j-1]*math.exp(-r*(z[2*(i-1)] + z[2*(j-1)]))*(norm.cdf(z2)-norm.cdf(z2 - (2*sigma*min(z[2*(i-1)],z[2*(j-1)]))/float(math.sqrt(T))))
            j = j +1
        i = i+1                                                       
    return math.sqrt(sigma**2 + sigma*math.sqrt(math.pi/float(2*T))*(4*math.exp((((z1)**2)/float(2))-s)*sum1 + math.exp((((z2)**2)/float(2))-2*s)*sum2))

def BSM_call(S_0, K, T, r, sigma):       
    d_1 = (math.log(float(S_0)/float(K)) + (r + float(sigma**2)/2)*T)/float(sigma*math.sqrt(T))   
    d_2 = d_1 - sigma*math.sqrt(T)    
    phi_1 = norm.cdf(d_1)    
    phi_2 = norm.cdf(d_2)     
    c=S_0*phi_1 - K*math.exp(-r*T)*phi_2    
    return c

def european_call(S_0,r,sigma):
    c = []
    i = 1
    while i <=n:
        t = z[2*(n-i)]-z[2*(n-i-1)]        
        S = S_0*math.exp((r-(sigma**2)/float(2))*t + 0.5*sigma*math.sqrt(t))
        sigma = sigma_adjust(S)
        K_adj = K + z[2*(n-i)+1]*math.exp(-r*(z[2*(n-i)]-T))
        call = integrate.quad(lambda x: BSM_call(S -z[2*(n-i)+1], K_adj, T-z[2*(n-i-1)], r, sigma),z[2*(n-i)+1],np.Inf)[0]           
        c.append(call)
        i = i+1
    return c[n-1]
                                                        
def take_input():
    global n
    n = input('Number of dividends:\n')
    i = 0
    z = []
    while i < n:
        x = input('Insert time t%d:\n'%(i+1))        
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
n,z = take_input()
K_adj = K + z[2*n-1]*math.exp(-r*(z[2*(n-1)]-T))
c = european_call(S_0,r,sigma)
print 'The price of European call is:',c

