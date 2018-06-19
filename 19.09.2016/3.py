N=float(input('Your cash: $'))
a=2
b=1
c=0.25
d=0.10
e=0.05
f=0.01

if(N>=a):
    q=N//a
    print(a,'x',q)
    w=N%a
if(N>=b):
    q1=w//b
    w1=w%b
    print(b,'x',q1)
if(N>=c):
    q2=w1//c
    print(c,'x',q2)
    w2=w1%c
if(N>=d):
    q3=w2//d
    print(d,'x',q3)
    w3=w2%d
if(N>=e):
    q4=w3//e
    print(e,'x',q4)
    w4=w3%e
if(N>=f):
    q5=w4//f
    print(f,'x',q5)
    w5=w4%f






                        
