# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:33:50 2020

@author: AAKASH
"""


import matplotlib.pyplot as plt 
import numpy as np 
from sympy import *
n ,k1 ,k2 ,c_1 ,c_2 ,c_3 ,c_4 ,c_5 ,s=symbols('n k1 k2 c_1 c_2 c_3 c_4 c_5 s')
a=int(input('Enter the coefficient of y_(n+2):'))
b=int(input('Enter the coefficient of y_(n+1):'))
c=int(input('Enter the coefficient ofy_n:'))
expr=a*(s**2)+b*s+c
sol=solve(expr,s)
print(sol)

q=im(sol[0])
if len(sol)==1:
    y1=sol[0]**n
    y2=n*sol[0]**n
elif(q!=0):
    p=[re(sol[0]),re(sol[1])]
    q=[im(sol[0]),im(sol[1])]
 #   
    b=p[1]**2 + q[1]**2
    rho=sqrt(b)
    theta=np.arctan( abs( q[1]/p[1] ) )
    y1=(rho**n)*cos(n*theta)
    y2=(rho**n)*sin(n*theta)
else:
    y1=sol[0]*n
    y2=sol[1]*n
        
print('y1 =',y1)
print('y2 =',y2)

y_0=int(input('y(0) :')) 
y_1=int(input('y(1):')) 

yc=y1*k1+y2*k2
yc=simplify(yc)
print('yc',yc)
yc0=yc.subs(n,0); 
#print('yc0;',yc0)
yc1=yc.subs(n,1); 
#print('yc1;',yc1)

eq0=yc0-y_0; 
eq1=yc1-y_1; 

res=solve([eq0,eq1],(k1,k2))
#print('res',res)

k1_1=res[k1]
k2_1=res[k2]
#print('k1',k1)
y_s=yc.subs(k1,k1_1)
y_s=y_s.subs(k2,k2_1)
#print('y_s',y_s) 

def createList(r1, r2): 
    return np.arange(r1, r2+1, 1) 
      
# Driver Code 
r1=0
r2=int(input('enter the number of points(exanple 10):'))

m=createList(r1, r2)
#print(m) 

y_ss=[]
for i in range(r2+1):
    y_ss.append( y_s.subs(n,m[i]))
    
print(y_ss)
plt.stem(m,y_ss) 
plt.show()
