#STUDENT: Daulet Demeuov
#GROUP: EN1-C-04
#TASK: Task1 problem E
#Description: Create a program that prints, and finds sum of all numbers between 1 and 50 that are divisible by 2 or 3 but not divisible by 6. 
list=[]
for d in range(1,51):
        if(d%2==0 or d%3==0) and (d%6>0):
                list.append(d)
                print(d, end=' ')
print(end='\n')
print('Sum is',sum(list))
