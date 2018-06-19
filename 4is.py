def r():
    n=int(input('Num:'))
    for i in range(1, n+1):
        x=str('#')
        r=str(' ')
        print(r*(n-i), x*(2*i-1))
r()
