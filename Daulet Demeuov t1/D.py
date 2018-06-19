#STUDENT: Daulet Demeuov
#GROUP: EN1-C-04
#TASK: Task1 proble D
#Description: Write program that reads N. Prompts N float numbers and finds MAXIMUM, MINIMUM and MEDIAN value between them.
d=int(input('Enter N: '))
import statistics
list=[]
for n in range(d):
    n=float(input('Enter number: '))
    list.append(n)    
print('MAXIMUM is ',max(list))
print('MINIMUM is ',min(list))
print('MEDIAN is ',statistics.median(list))
