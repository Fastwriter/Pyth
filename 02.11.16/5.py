def tran(e,r):
    d={}
    c=len(e)
    for i in e:
        d[i]=list()
    for i in range(c):
        d[e[i]].append(r[i])
    print(d)
