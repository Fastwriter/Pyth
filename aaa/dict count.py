def f():
    import string
    a=string.punctuation
    d=dict()
    c=open('to kill a mockingbird.txt')
    for i in c.read().split():
        i = i.lower().strip(a)
        b = len(i)
    for x in range(0, 20):
        if(x==b):
            d[x]=i
    print(d)
