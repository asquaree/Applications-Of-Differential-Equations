# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:31:46 2020

@author: AAKASH
"""


from sympy import *
x,c1,c2,r,t=symbols('x c1 c2 r t')
k1=int(input('Enter the coefficient of (ax+b)^2 d^2y/dx^2:'))
k2=int(input('Enter the coefficient of (ax+b) dy/dx:'))
k3=int(input('Enter the coefficient of y:'))
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
f=input('Enter f in terms of x:')
f=sympify(f)
f1=f.subs(x,(exp(t)-b)/a)
expr=(k1*(a**2))*r**2+((a*k2)-(a**2*k1))*r+k3
sol=solve(expr,r)
print('sol',sol)
q=im(sol[0])
if len(sol)==1:
    y1=exp(sol[0]*t)
    y2=t*exp(sol[0]*t)
elif(q!=0):
    p=[re(sol[0]),re(sol[1])]
    q=[im(sol[0]),im(sol[1])]
 ##for another solution,change p[0] -> p[1] and q[0] -> q[1] in (q!=0)condition if roots are complex

    y1=exp(p[1]*t)*cos(q[1]*t)
    y2=exp(p[1]*t)*sin(q[1]*t)
else:
    y1=exp(sol[0]*t)
    y2=exp(sol[1]*t)
        
print('y1 =',y1)
print('y2 =',y2)
yc=c1*y1+c2*y2

w=y1*diff(y2,t)-y2*diff(y1,t)
print('Wronskian =',simplify(w))
p1=-y1*integrate((y2*f)/((a**2)*k1*w),t)
p1=simplify(p1)
p2=y2*integrate((y1*f)/((a**2)*k1*w),t)
p2=simplify(p2)
#print('p1:',p1)
#print('p2:',p2)
yp=p1+p2
yy=yc+yp
yy=simplify(yy)
print(yy)
y3=yy.subs(t,log(a*x+b))
print('The General Solution of the ODE:',simplify(y3))
