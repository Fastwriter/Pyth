def f():
    import string
    a=string.punctuation
    d=dict()
    p = []
    max_l = 0
    f=open('to kill a mockingbird.txt')
    string = f.read().split()
    for i in string:
        i = i.lower().strip(a)
        if(len(i)>max_l): max_l = len(i)
    for i in range(1,max_l+1):
        d[i] = list()
    for i in string:
        i = i.lower().strip(a)
        for y in d.keys():
            if(len(i) == y):
                d[y].append(i)
                continue
    new_dict = dict()
    for key, value in d.items():
        if(len(value) != 0):
            new_dict[key] = value
    print(new_dict)
f()
