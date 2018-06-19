def remove(t):
    p=tuple()
    n=0
    a=len(t)
    while( n < a-1):
        p+=(t[n],)
        n+=1
    print(p)
