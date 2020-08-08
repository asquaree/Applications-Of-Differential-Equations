
from sympy import *
import sympy as sym
from sympy.solvers.solveset import linsolve
x,r,d_0,c_0,c_1,c_2,c_3,c_4,c_5=symbols('x r d_0 c_0 c_1 c_2 c_3 c_4 c_5')
print('Input the coefficients of DE as constants or function of x')
p1=input('Coefficient of D2y:')
p2=input('Coefficient of Dy:')
p3=input('Coefficient of y:')

c=[c_0,c_1,c_2,c_3,c_4,c_5]

p1=sympify(p1)
p2=sympify(p2)
p3=sympify(p3)

y=0

for i in range(0,6):
    y=y+c[i]*x**(i)

print('y=',y)
y=sympify(y)
dy=diff(y,x) 
d2y=diff(dy,x) 
ode=p1*d2y+p2*dy+p3*y
ode=expand(ode) 
print('ode',ode)
ps=collect(ode,x)
ps=simplify(ps)
print('ps',ps)

d=[]
for i in range (6+1):
    d.append(ps.coeff(x,i))
    
print('d',d)

fin_list = solve((d[0],d[1],d[2],d[3]),(c_2,c_3,c_4,c_5)) 
c = fin_list 
z=y.subs(c_2,c[c_2])
z=z.subs(c_3,c[c_3])
z=z.subs(c_4,c[c_4])
z=z.subs(c_5,c[c_5])
print('The particular solution of the given ODE around x=0 is given by: ')
print('z',z)