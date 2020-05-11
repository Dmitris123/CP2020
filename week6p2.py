from math import log
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

def f(x):
    return x**2 * log(x)
    
def fder(x):
    return x * (2.*log(x) + 1)

x=1

def der_two_point_forward(f,x,h):
    numerator=f(x+h)-f(x)
    denominator=h
    return numerator/denominator

def der_three_point_forward(f,x,h):
    numerator=-1.5*f(x)+2*f(x+h)-0.5*f(x+2*h)
    denumerator=h
    return numerator/denumerator

h_arr=np.logspace(-13,-1,num=100)

df_two_point_forward_arr=np.array([])
df_three_point_forward_arr=np.array([])

for h in h_arr:
    df_two_point_forward_arr=np.append(df_two_point_forward_arr,np.abs(der_two_point_forward(f,x,h)-fder(x)))
    df_three_point_forward_arr=np.append(df_three_point_forward_arr,np.abs(der_three_point_forward(f,x,h)-fder(x)))
    
index_1=h_arr>1e-6
index_2=h_arr>1e-4

p_two_point_forward=np.polyfit(np.log10(h_arr[index_1]),np.log10(df_two_point_forward_arr[index_1]),1)
p_three_point_forward=np.polyfit(np.log10(h_arr[index_2]),np.log10(df_three_point_forward_arr[index_2]),1)    
    
plt.figure(figsize=(15,10))    
plt.loglog(h_arr,df_two_point_forward_arr,'b-',label='two-point, a={}'.format(p_two_point_forward[0]))
plt.loglog(h_arr,df_three_point_forward_arr,'r-',label='three-point, a={}'.format(p_three_point_forward[0]))
plt.xlabel('h')
plt.ylabel('|Df-f\'|')
plt.legend();        

print("h для двухточечной схемы:", h_arr[df_two_point_forward_arr.argmin()])
print("h для трёхточечной схемы:", h_arr[df_three_point_forward_arr.argmin()])

# по графику видно, что порядки примерно такие, какие мы посчитали 