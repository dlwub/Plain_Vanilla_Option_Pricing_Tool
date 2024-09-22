import datetime, time
import math
from scipy.stats import norm


def price_calc_call(S_0, K, T, r, sigma):       
    d_1 = (math.log(float(S_0)/float(K)) + (r + float(sigma**2)/2)*T)/float(sigma*math.sqrt(T))    
    d_2 = d_1 - sigma*math.sqrt(T)    
    phi_1 = norm.cdf(d_1)    
    phi_2 = norm.cdf(d_2)     
    c=S_0*phi_1 - K*math.exp(-r*T)*phi_2    
    return c

def price_calc_put(S_0, K, T, r, sigma):       
    d_1 = (math.log(float(S_0)/float(K)) + (r + float(sigma**2)/2)*T)/float(sigma*math.sqrt(T))    
    d_2 = d_1 - sigma*math.sqrt(T)   
    phi_3 = norm.cdf(-d_1)    
    phi_4 = norm.cdf(-d_2)   
    p=K*math.exp(-r*T)*phi_4 - S_0*phi_3
    return p 
    








    


    


        
        
