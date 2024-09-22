import math
from scipy.stats import norm
import blackscholes

    
def price_strike(r, T, n, z):      
    S_n = 0
    K_n = 0
    i = 1
    while i <=n:
        S_n = S_n + ((T - z[2*(i-1)])/float(T))*z[2*i-1]*math.exp(-r*z[2*(i-1)])
        K_n = K_n + (z[2*(i-1)]/float(T))*z[2*i-1]*math.exp(-r*z[2*(i-1)])
        i=i+1
    return S_n, K_n

def append_z(i,x):
    global z
    if i == 1:
        z = []
        z.append(x)
    else:
        z.append(x)
    return

def modify_z(i):
    global z
    if i > 1:
        del(z[-1])
    else:
        pass
    return

def call(S_0, K, r, T, sigma, n):
    S_n,K_n = price_strike(r, T, n, z)
    return blackscholes.price_calc_call(S_0 - S_n, K + K_n*math.exp(r*T), T, r, sigma)

def put(S_0, K, r, T, sigma, n):
    S_n,K_n = price_strike(r, T, n, z)
    return blackscholes.price_calc_put(S_0 - S_n, K + K_n*math.exp(r*T), T, r, sigma)
    
    


