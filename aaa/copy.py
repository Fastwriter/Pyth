a=open('fox.txt')
b=open('co.txt','w')
for e in a:
    b.write(e)
    b.write(sum(e))
a.close()
b.close()
