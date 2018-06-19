def c13():
    import string
    d = dict()
    p = string.punctuation
    f = open('to kill a mockingbird.txt')
    for x in f.read().split():
        x = x.lower().strip(p)
        d[x]=d.get(x,0)+1
    print('Word count:', sum(d.values()))
    print('Words:','\n',d)
    l=list()
    for key,value in d.items():
        l.append((value,key))
    l.sort(reverse = True)
    print('Sooo...')
    for value,x in l[0:10]:
        print(x, value)
