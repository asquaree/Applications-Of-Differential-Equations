# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:32:24 2020

@author: AAKASH
"""


from sympy import *
import scipy.linalg as la
import numpy as np 

x,c1,c2,c3,c4=symbols('x c1 c2 c3 c4')
c=[c1,c2,c3,c4]

R = int(input("Enter the number of equations")) 
 
# Initialize matrix 
matrix = [] 
print("Enter the coefficients of variables entries row wise:") # eq1=6x1-x2 ; eq2=x1+x2  => 6(enter) -1(enter) 1(enter) 1(enter) 
  
# For user input 
for i in range(R):           
    a =[] 
    for j in range(R):       
         a.append(int(input())) 
    matrix.append(a) 
  
A=matrix
n=len(A)
#print('n',n)
eigvals, eigvecs = la.eig(A)
eigvals = eigvals.real
print('eigen values',eigvals)
print('eigen vectors',eigvecs)
#C = int(input("Enter the number of equations")) 
 
# Initialize matrix 
matrix2 = [] 
print("Enter the function entries rowwise:") # eq1=6x1-x2 ; eq2=x1+x2  => 6(enter) -1(enter) 1(enter) 1(enter) 
  
# For user input 
for i in range(R):           
    a =[] 
    for j in range(1):       
         a.append((input())) 
    matrix2.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(1): 
        matrix2[i][j]=sympify(matrix2[i][j])
        print(matrix2[i][j], end = " ") 
    print() 

f=matrix2
inv_eig=np.linalg.inv(eigvecs)

# Program to multiply two matrices (vectorized implementation) 
P=np.zeros([R,1])  
P = np.dot(inv_eig,f) 
y=[]
p=[]

for i in range(0,n):
    p.append(   c[i]*exp( eigvals[i]*x) + exp( eigvals[i]*x )*integrate( exp(-1*eigvals[i]*x)*P[i]) )
     
y.append(p)
print('y matrix:',y)

trans_y=np.transpose(y)
result=np.zeros([R,1])
result = np.dot(eigvecs,trans_y)

X=result 

print(" ")
ANSWER=simplify(X)
print('ANSWER:',ANSWER)

