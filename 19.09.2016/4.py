import random
x=random.randint(-30,30)
y=random.randint(-30,30)
z=random.choice(['+','-','/','*'])
if(z=='+'):
    print(x,'+',y,'=','?')
    w=int(input('Your answer, please:'))
    if(w==x+y):
        print('Great')
    else: print('Loser, the answer is ',x+y)
if(z=='-'):
    print(x,'-',y,'=','?')
    w=int(input('Your answer, please:'))
    if(w==x-y):
        print('Great')
    else: print('Loser,the answer is ',x-y)
if(z=='/'):
    print(x,'/',y,'=','?')
    w=float(input('Your answer, please:'))
    if(w==x/y):
        print('Great')
    else: print('Loser,the answer is ',x/y)
if(z=='*'):
    print(x,'*',y,'=','?')
    w=int(input('Your answer, please:'))
    if(w==x*y):
        print('Great')
    else: print('Loser,the answer is ',x*y)
