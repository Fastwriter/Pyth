def count_num(e):
    p=list()
    q=list()
    n=0
    for z in e:
        if z in p:
            continue
        else:
            p.append(z)
        for x in e:
            if z==x:
                n+=1
        q.append(n)
        n=0
    for z in range(0,len(p)):
        if z==len(p)-1:
            print(p[z], q[z])
        else:
            print(p[z], q[z],',', end=' ')
