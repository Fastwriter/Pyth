def f():
    a=[]
    b = open ('words.txt')
    for line in b:
        word=line.strip()
        a.append(word)
    print(a)


f()
