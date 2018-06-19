def cop():
    a=open('fox.txt')
    b=open('co.txt','w')
    for e in a:
        b.write(e)
    a.close()
    b.close()
