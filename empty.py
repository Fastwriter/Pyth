def y():
    N=int(input('Column:'))
    n=0
    for i in range(0,101):
        if(i%4==0 or i%7==0):
            continue
        else:
            n=int(n+1)
            print(i, end=' ')
            if(n%N==0):
                print('\n')
y()
