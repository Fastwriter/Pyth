a=int(input('Enter the numerator:'))
b=int(input('Enter the denominator:'))
if(a>b):
    c=a%b
    d=a//b
    print('equavalent is', d,'and', c,'/',b)
else:
    print(a,'/',b)
