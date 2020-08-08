# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:28:26 2020

@author: AAKASH
"""


e=[] #Empty List
y=expand(y1*(x**sol[0]))
dy=diff(y,x)
d2y=diff(dy,x)
ode1=p1x*d2y+p2x*dy+p3x*y
ode=ode1/x**sol[0]
ode=simplify(ode)
ps=collect(ode,x)
for i in range(0,6):
    d=ps.coeff(x,i)
    e.append(d)
print('d=',e)
print('Relation between coefficients.Substitute c_0 with a value to find the values of all the variables')
for i in range(0,6):
    Sol1=solve_linear(e[i])
    print(Sol1)
print('Linearly Independent Solution:',y)
f=[] # Empty List
y=expand(y1*(x**sol[1]))
dy=diff(y,x)
d2y=diff(dy,x)
ode1=p1x*d2y+p2x*dy+p3x*y
ode=ode1/x**sol[1]
ode=simplify(ode)
ps=collect(ode,x)
for i in range(0,6):
    d=ps.coeff(x,i)
    f.append(d)
print('Relation between coefficients.Substitute c_0 with a value to find the values of all the variables')
print('d=',f)
for i in range(0,6):
    Sol2=solve_linear(f[i])
    print(Sol2)
print('Linearly Independent Solution:',y)

