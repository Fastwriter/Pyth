#STUDENT: Daulet Demeuov
#GROUP: EN1-C-04
#TASK: Task1 problem C
#Description: Write program that reads numbers while negative number is not entered. Print maximum number among entered values as a result
d=int(input('value:'))
if(d>0):
    list=[]
    while (d>=0):
        d=int(input('value:'))
        list.append(d)
    print('Maximum is ',max(list))
else:('Wrong!')
