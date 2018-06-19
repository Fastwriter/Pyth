def cumsum(r):
    total=0
    add=[]
    for n in r:
        total+=n
        add.append(total)
    return add
