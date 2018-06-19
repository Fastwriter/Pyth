def hack(a,b):
    import os
    p=[]
    for d, sd ,f in os.walk(a):
        for i in f:
            if i==b:
                p.append(os.path.join(d,i))
    print(p)
