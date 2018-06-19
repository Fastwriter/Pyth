'''import os
a='start '
res=os.popen(a).read()
print(res)
'''

import dbm
import pickle
f=open('f.txt','w')
line1='Hey there! My name is Daulet.'
f.write(line1)
f.close()
f = open('f.txt', 'r')
for i in f:
    f1=pickle.dumps(i)
db = dbm.open('daukabase','c')
db['l']=f1
print(db['l'])
t=db['l']
t=pickle.loads(t)
print(t)
f.close()
db.close()

import pickle
import dbm
s='hey there!'
s1=pickle.dumps(s)
print(s1)
d={1:'one', 2:'two'}
d1=pickle.dumps(d)
print(d1)

db=dbm.open('dbtemp', 'c')
db['d']=d1
a=db['d']
a=pickle.loads(a)
print(a)
db.close()
