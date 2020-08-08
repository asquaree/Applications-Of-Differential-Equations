# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:26:28 2020

@author: AAKASH
"""


from sympy import *

R = int(input("Enter the number of rows in matrix"))
C=  int(input('enter the number of columns in matrix'))   
# Initialize matrix 
matrix = [] 
print("Enter the coefficients of variables entries row wise(press enter after each entry) :") 

# For user input 
for i in range(R):           
    a =[] 
    for j in range(R):       
         a.append(int(input())) 
    matrix.append(a) 
  
A=Matrix(matrix)
n=len(A)
print("Matrix : {} ".format(A))
P, D = A.diagonalize(A)         
print("Diagonal of a matrix : {}".format(D))
