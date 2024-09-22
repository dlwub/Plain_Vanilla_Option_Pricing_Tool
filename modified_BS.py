import datetime, time
import math
from scipy.stats import norm


def call(S_0, K, T, r, q, n, sigma):
    F = S_0*((1-q)**n)*math.exp(r*T)
    d_1 = (math.log(float(F)/float(K)) + (float(sigma**2)/2)*T)/float(sigma*math.sqrt(T))   
    d_2 = d_1 - sigma*math.sqrt(T)    
    phi_1 = norm.cdf(d_1)    
    phi_2 = norm.cdf(d_2)     
    c = math.exp(-r*T)*(F*phi_1 - K*phi_2)    
    return c

def put(S_0, K, T, r, q, n, sigma):
    F = S_0*((1-q)**n)*math.exp(r*T)
    d_1 = (math.log(float(F)/float(K)) + (float(sigma**2)/2)*T)/float(sigma*math.sqrt(T))   
    d_2 = d_1 - sigma*math.sqrt(T)    
    phi_3 = norm.cdf(-d_1)    
    phi_4 = norm.cdf(-d_2)     
    p = math.exp(-r*T)*(K*phi_4 - F*phi_3)    
    return p


