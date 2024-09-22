import numpy as np
import math


def inputs(r, T, sigma, k):
    delta_t = float(T)/k
    u = math.exp(sigma*math.sqrt(delta_t))
    d = 1/float(u)
    p = float(math.exp(r*delta_t)-d)/(u-d)
    return delta_t, u, d, p
    
def put(S_0, K, r, q, T, sigma, n, k):
    delta_t, u, d, p = inputs(r, T, sigma, k)    
    m=np.zeros((1,k+1))   #Forms (1)x(k+1) matrix
    i=k
    j=0
    while j<=k:
        m[0][j]=max(K-(u**(k-2*j))*((1-q)**n)*S_0,0)
        j=j+1
    i=k-1
    while i >= 0:
        j=0
        while j<=i:            
            m[0][j]=math.exp(-r*delta_t)*(p*m[0][j]+(1-p)*m[0][j+1])
            j=j+1
        i=i-1
    return m[0][0]

def call(S_0, K, r, q, T, sigma, n, k):
    delta_t, u, d, p = inputs(r, T, sigma, k)
    m=np.zeros((1,k+1))
    i=k
    j=0
    while j<=k:
        m[0][j] = max((u**(k-2*j))*((1-q)**n)*S_0 - K,0)
        j=j+1
    i=k-1
    while i >= 0:
        j=0
        while j<=i:
            m[0][j]= math.exp(-r*delta_t)*(p*m[0][j]+(1-p)*m[0][j+1])
            j=j+1
        i=i-1
    return m[0][0]




