def f(t):
    p=[]
    n=0
    v=0
    while(n<len(t)):
        v+=t[n]
        p.append(v)
        n+=1
    print(p)
