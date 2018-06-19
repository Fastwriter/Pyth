import string
def fil():
    d=dict()
    t=d.values()
    l=[]
    f=open('Nurbek.txt')
    p=string.punctuation
    for i in f.read().split():
        i = i.lower().strip(p)
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for key, value in d.items():
        l.append((value, key))
    l.sort(reverse=True)
    for freq, word in l[0:10]:
        print(word, freq)
    print(sum(t))
    print(d)

fil()
