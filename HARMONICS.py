# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 23:44:09 2020

@author: AAKASH
"""
from array import array 
import numpy as np
import math
from sympy import *
import matplotlib.pyplot as plt
x=symbols('x')

p=float(input('Enter the period length(in integer or float type only):'))
l=p/2

n = int(input("Enter number of elements in vectors : ")) 
  
# Below line read inputs from user using map() function  
X = list(map(float,input("\nEnter the X-vector : ").strip().split()))[:n] 
Y= list(map(float,input("\nEnter the Y-vector : ").strip().split()))[:n] 
  
#print("\nList is - ", X)
#print(Y) 
N=len(X)
print(N)
r=int(input('Enter the number of terms in series:'))

a_0=(2/N)*sum(Y); 

a=[]
b=[]
H=[]
add1=[]
add2=[]

for i in range(1,r+1):
    sum1=0
    sum2=0
    for j in range(N):
        sum1=sum1+(Y[j]*math.cos(i*math.pi*X[j]/l))
        sum2=sum2+(Y[j]*math.sin(i*math.pi*X[j]/l))
    
    add1.append(sum1)
    add2.append(sum2)
    

#print('add1',add1)
#print('add1',add2)

for i in range(r):
    a.append((2/N)*add1[i])
    b.append((2/N)*add2[i])

#print('a',a)
#print('b',b)

for i in range(r):
    H.append(a[i]*cos((i+1)*math.pi*x/l) + b[i]*sin((i+1)*math.pi*x/l))

print('H',H)

HS=(a_0)/2+sum(H); 

#print('Harmonic series is given by',HS) 

HS=simplify(HS) 
print('Harmonic series is given by',HS)

u = np.arange(0, p+1,0.1) 

v=[]
for i in range(len(u)):
    
    v.append(HS.subs(x,u[i]))

    
plt.plot(u,v) 

plt.plot(X,Y,'ro')
plt.xlim([0, p])

plt.show()
  