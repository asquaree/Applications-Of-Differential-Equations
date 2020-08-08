from sympy import *
import sympy as sym


x,r,d_0,c_0,c_1,c_2,c_3,c_4,c_5=symbols('x r d_0 c_0 c_1 c_2 c_3 c_4 c_5')
print('Input the coefficients of DE as constants or function of x')
p1x=input('Coefficient of D2y:')
p1x=sympify(p1x)
p2x=input('Coefficient of Dy:')
p2x=sympify(p2x)
p3x=input('Coefficient of y:')
p3x=sympify(p3x)
c=[c_0,c_1,c_2,c_3,c_4,c_5]
y=0
#p=0
for i in range(0,6):
    y=y+c[i]*x**(i)
print('y=',y)
Px=p2x/p1x
print('Px=',Px)
Qx=p3x/p1x
print('Qx=',Qx)
px=simplify(x*Px)
print('px=',px)
qx=simplify((x**2)*Qx)
print('qx=',qx)
a_0=px.subs(x,0)
print('a_0',a_0)
b_0=qx.subs(x,0)
print('b_0',b_0)

expr=r*(r-1)+a_0*r+b_0
sol=solve(expr,r)
print('sol',sol)
print(sol[0])

d=[]
y_y=[]
for i in range(2):
    y1=y*x**sol[i]
    
    y1=expand(y1)
    print('y1',y1)
    y_y.append(y1)
    dy1=diff(y1,x)
    d2y1=diff(dy1,x)
    ode1=p1x*d2y1+p2x*dy1+p3x*y1
    ode1=ode1/x**sol[i];
    ode1=expand(ode1)
    #print('ode1',ode1)
    
    ps1=collect(ode1,x)
    ps1=simplify(ps1)
    #print('ps1',ps1)
    
    d1=[]
    for i in range (6+1):
        d1.append(ps1.coeff(x,i))
    #print('d1',d1)
    d.append(d1)
print(' ')
print('d',d)

fin_list = solve((d[0][0],d[0][1],d[0][2],d[0][3],d[0][4]),(c_1,c_2,c_3,c_4,c_5)) 
c1 = fin_list 
z1= y_y[0].subs(c_1,c1[c_1])
z1=z1.subs(c_2,c1[c_2])
z1=z1.subs(c_3,c1[c_3])
z1=z1.subs(c_4,c1[c_4])
z1=z1.subs(c_5,c1[c_5])
print(' ')
print('The particular solution of the given ODE around x=0 is given by: ')
print('z1',z1)
print(' ')
fin_list = solve((d[1][0],d[1][1],d[1][2],d[1][3],d[1][4]),(c_1,c_2,c_3,c_4,c_5)) 
c2 = fin_list 
z2=y_y[1].subs(c_1,c2[c_1])
z2=z2.subs(c_2,c2[c_2])
z2=z2.subs(c_3,c2[c_3])
z2=z2.subs(c_4,c2[c_4])
z2=z2.subs(c_5,c2[c_5])
print('The particular solution of the given ODE around x=0 is given by: ')
print('z2',z2)
