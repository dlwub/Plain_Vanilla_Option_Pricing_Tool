import numpy as np
from scipy import integrate
from scipy.stats import norm
import math
from scipy.integrate import dblquad


def bivar(b_1, b_2, rho):
    return (1/float(2*math.pi*math.sqrt(1-rho**2)))*dblquad(lambda x, y: math.exp(-float(x**2-2*x*y*rho + y**2)/(2*(1-rho**2))), -np.Inf, b_1, lambda x: -np.Inf, lambda x: b_2)[0]
def american_call(S_0, K, T, r, b, sigma):
    t=(float(math.sqrt(5)-1)/2)*T
    beta=(0.5-(float(b)/(sigma**2)))+ math.sqrt(((float(b)/(sigma**2))-0.5)**2 + 2*float(r)/(sigma**2))
    B_1=(float(beta)/(beta-1))*K
    B_0=max(K,(float(r)/(r-b))*K)
    def h(t):
        return -(b*t+2*sigma*math.sqrt(t))*(float(K**2)/((B_1-B_0)*B_0))
    def k(t):
        return -(b*t+2*sigma*math.sqrt(t))*(float(B_0)/(B_1-B_0))#for the 1993 Bjerksund-Stensland model
    Y=B_0 +(B_1-B_0)*(1-math.exp(k(T))) #for the 1993 Bjerksund-Stensland model
    X=B_0 +(B_1-B_0)*(1-math.exp(h(T)))
    x=B_0 +(B_1-B_0)*(1-math.exp(h(T-t)))
    alpha_Y=(Y-K)*(Y**(-beta)) #for the 1993 Bjerksund-Stensland model
    alpha_X=(X-K)*(X**(-beta))
    alpha_x=(x-K)*(x**(-beta))
    rho=math.sqrt(float(t)/T)
    
    def phi(S_0,T,g,H,X):
        l=-r+g*b+0.5*g*(g-1)*(sigma**2)
        k=(float(2*b)/(sigma**2))+(2*g-1)
        phi_1=math.exp(l*T)*((S_0)**g)*(norm.cdf(-float(math.log(float(S_0)/H)+(b+(g-0.5)*(sigma**2))*T)/(sigma*math.sqrt(T)))-((float(X)/(S_0))**k)*norm.cdf(-float(math.log(float(X**2)/((S_0)*H))+(b+(g-0.5)*(sigma**2))*T)/(sigma*math.sqrt(T))))
        return phi_1
    def psi(S_0,T,g,H,X,x,t):
        l=-r+g*b+0.5*g*(g-1)*(sigma**2)
        k=(float(2*b)/(sigma**2))+(2*g-1)
        d_1=-float(math.log(float(S_0)/x)+(b+(g-0.5)*(sigma**2))*t)/(sigma*math.sqrt(t))
        d_2=-float(math.log(float(X**2)/((S_0)*x))+(b+(g-0.5)*(sigma**2))*t)/(sigma*math.sqrt(t))
        d_3=-float(math.log(float(S_0)/x)-(b+(g-0.5)*(sigma**2))*t)/(sigma*math.sqrt(t))
        d_4=-float(math.log(float(X**2)/((S_0)*x))-(b+(g-0.5)*(sigma**2))*t)/(sigma*math.sqrt(t))
        D_1=-float(math.log(float(S_0)/H)+(b+(g-0.5)*(sigma**2))*T)/(sigma*math.sqrt(T))
        D_2=-float(math.log(float(X**2)/((S_0)*H))+(b+(g-0.5)*(sigma**2))*T)/(sigma*math.sqrt(T))
        D_3=-float(math.log(float(x**2)/((S_0)*H))+(b+(g-0.5)*(sigma**2))*T)/(sigma*math.sqrt(T))
        D_4=-float(math.log(float((S_0)*(x**2))/(H*(X**2)))+(b+(g-0.5)*(sigma**2))*T)/(sigma*math.sqrt(T))
        psi_1=math.exp(l*T)*((S_0)**g)*(bivar(d_1,D_1,rho)-((float(X)/(S_0))**k)*bivar(d_2,D_2,rho)-((float(x)/(S_0))**k)*bivar(d_3,D_3,-rho)+((float(x)/X)**k)*bivar(d_4,D_4,-rho))
        return psi_1    
    C_1 = alpha_X*((S_0)**beta)-alpha_X*phi(S_0,t,beta,X,X)+ phi(S_0,t,1,X,X)- phi(S_0,t,1,x,X)-K*phi(S_0,t,0,X,X)+K*phi(S_0,t,0,x,X)+alpha_x*phi(S_0,t,beta,x,X)-alpha_x*psi(S_0,T,beta,x,X,x,t)+ psi(S_0,T,1,x,X,x,t)-psi(S_0,T,1,K,X,x,t)-K*psi(S_0,T,0,x,X,x,t)+K*psi(S_0,T,0,K,X,x,t)
    C_0 = alpha_Y*((S_0)**beta)-alpha_Y*phi(S_0,T,beta,Y,Y)+phi(S_0,T,1,Y,Y)- phi(S_0,T,1,K,Y)-K*phi(S_0,T,0,Y,Y)+ K*phi(S_0,T,0,K,Y) #for the 1993 Bjerksund-Stensland model
    return C_1


S_0 = input('Current stock price:\n')
K = input('Strike price:\n')
T = input('Length of option life:\n')
r = input('Risk free interest rate in percentage:\n')
r=r/float(100)
q = input('Dividend yield in percentage:\n')
q = q/float(100)
sigma = input('Volatility:\n')
b = r-q
if q==0:
    print 'Please use Binomial model for non-dividend paying stocks.'
else:
    C = american_call(S_0, K, T, r, b, sigma)
    P = american_call(K, S_0, T, q, -b, sigma)    
    print 'The price of the American call is:',C
    print 'The price of the American put is:',P




