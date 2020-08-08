# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:33:05 2020

@author: AAKASH
"""


#valid for constant functions only

from symfit import parameters, variables, sin, cos, Fit
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
x,n=symbols('x n')

def fourier_series(x, f, n=0):
    """
    Returns a symbolic fourier series of order `n`.

    :param n: Order of the fourier series.
    :param x: Independent variable
    :param f: Frequency of the fourier series
    """
    # Make the parameter objects for all the terms
    a0, *cos_a = parameters(','.join(['a{}'.format(i) for i in range(0, n + 1)]))
    sin_b = parameters(','.join(['b{}'.format(i) for i in range(1, n + 1)]))
    
    print('a0',a0)
    print('cos a wali:',*cos_a)
    print('sin_b wali:',sin_b)
    
    # Construct the series
    series = a0 + sum(ai * cos(i * f * x) + bi * sin(i * f * x)
                     for i, (ai, bi) in enumerate(zip(cos_a, sin_b), start=1))
    return series

x, y = variables('x, y')
w, = parameters('w')

no_of_functions=int(input('enter the number of functions:'))

f=[]
lower_limit=[]
upper_limit=[]

for i in range(no_of_functions):
    f.append(input(f'enter functions {i} :'))
    lower_limit.append(float(input(f'Enter the lower limit of function(in float type) {i} :')))
    upper_limit.append(float(input(f'Enter the upper limit of function(in float type) {i} :')))
    
terms=int(input('Enter the number of terms'))
model_dict = {y: fourier_series(x, f=w, n=terms)}
print('series',model_dict)
print('lower_limit[0]',lower_limit[0])
print('upper_limit[0]',upper_limit[no_of_functions-1])
l_l=lower_limit[0]
u_l=upper_limit[no_of_functions-1]
# Make step function data
xdata = np.linspace(l_l,u_l)
print('xdaata',xdata)
ydata = np.zeros_like(xdata)
print('ydaata',ydata)
#ydata[xdata > 0] = 1
for i in range(no_of_functions):
    l1=lower_limit[i]
    l2=upper_limit[i]
    ff=f[i]
    ydata[np.logical_and( xdata>=l1 , xdata<l2)]=ff
# Define a Fit object for this model and data
fit = Fit(model_dict, x=xdata, y=ydata)
fit_result = fit.execute()
#print('result:',fit_result)

# Plot the result
plt.plot(xdata, ydata)
plt.plot(xdata, fit.model(x=xdata, **fit_result.params).y, ls=':')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
