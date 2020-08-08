# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:31:06 2020

@author: AAKASH
"""


from sympy import *
x,y,r,c1,c2,t=symbols('x y r c1 c2 t ')
p1=int(input('Enter the coefficient of x^2 d^2y/dx^2:'))
p2=int(input('Enter the coefficient of x dy/dx:'))
p3=int(input('Enter the coefficient of y:'))

f=input('Enter the function in terms of x:')
f=sympify(f)
f1=f.subs(x,exp(t))
expr=p1*(r**2)+(p2-p1)*r+p3
sol=solve(expr,r)
print(sol)
q=im(sol[0])
if len(sol)==1:
    y1=exp(sol[0]*t)
    y2=t*exp(sol[0]*t)
elif(q!=0):
    p=[re(sol[0]),re(sol[1])]
    q=[im(sol[0]),im(sol[1])]
 ###for another solution,change p[0] -> p[1] and q[0] -> q[1] in (q!=0)condition if roots are complex
    y1=exp(p[0]*t)*cos(q[0]*t)
    y2=exp(p[0]*t)*sin(q[0]*t)
else:
    y1=exp(sol[0]*t)
    y2=exp(sol[1]*t)
        
print('y1 =',y1)
print('y2 =',y2)
yc=y1*c1+y2*c2
print('yc =',yc)
w=y1*diff(y2,t)-y2*diff(y1,t)
print('w =',simplify(w))
yp=-y1*integrate(y2*f1/(p1*w),t)+y2*integrate(y1*f1/(p1*w))
yy=yc+yp
y3=yy.subs(t,log(x))
print('The general solution of the given ODE is given by:',simplify(y3))
