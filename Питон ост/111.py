import math
a=input('write the value x')
b=input('write the value y')
x=float(a)
y=float(b)
z=(x+((2+y)/x**2))/(y+(1/((x**2+10)**(1/2))))
q=float(2.8*math.sin(x)+abs(y))
print(z,q)
