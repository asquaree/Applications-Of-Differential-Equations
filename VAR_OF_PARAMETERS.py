# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:27:41 2020

@author: AAKASH
"""


import scipy.linalg as la
from sympy import *
u,v,w=symbols('u v w')

a=int(input('Enter the coefficient of x1^2:'))
b=int(input('Enter the coefficient of x2^2:'))
c=int(input('Enter the coefficient of x3^2:'))
p=int(input('Enter the coefficient of x1*x2:'))
q=int(input('Enter the coefficient of x1*x3:'))
r=int(input('Enter the coefficient of x2*x3:'))

A=[[a,p/2,q/2],[p/2,b,r/2],[q/2,r/2,c]]
print('matrix A',A)

results = la.eig(A)
#print('eigenvalues',results[0])
#print('eigen vectors',results[1])
eigvals, eigvecs = la.eig(A)
print('eigenvalues',eigvals)
print('eigen vectors',eigvecs)
eigvals = eigvals.real
print('eigen values with only real part:',eigvals)

#print(results[0][0])
canonical_form=(eigvals[0])*(u**2) + (eigvals[1])*(v**2) + (eigvals[2])*(w**2)
print('canonical form:',canonical_form)
