# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:42:50 2020

@author: AAKASH
"""


from sympy import *
from sympy import symbols
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform

y,y1,y2,s,t,Y=symbols('y y1 y2 s t Y')

y=sympify('y(t)')
#y1=diff(y,t)
#print('y1:',y1)

a=int(input('enter the coefficient of second deri of y:'))
b=int(input('enter the coefficient of first deri of y:'))
c=int(input('enter the coefficient  of y:'))
f=(input('enter the RHS function:'))
d=int(input('enter the value of y(0):'))
e=int(input('enter the value of Dy(0):'))
f=sympify(f)

y1=diff(y,t)
y2=diff(y1,t)
eq=a*y2 + b*y1 + c*y - f;
print('equation:',eq)
print(' ')
eqn=laplace_transform(eq, t, s)
print('after laplace equation:',eqn)
print(' ')
eqn=sympify(eqn)

#eqn=eqn.subs(t,0)
#eqn=eqn.subs(y(0),d)

print('after replacing:',eqn)
print(' ')

eqn=eqn.subs(sympify('LaplaceTransform(y(t), t, s)'),Y)
print('after replacing:',eqn)
print(' ')

eqn=eqn.subs(sympify(y1),e)
print('after replacing:',eqn)
eqn=eqn.subs(sympify(y),d)
print(' ')
print('after replacing:',eqn)
print(' ')

collected_expr = collect(eqn, Y)
Y1=simplify(solve(eqn,Y))

ans=inverse_laplace_transform(Y1,s,t)
ANURADHA.J