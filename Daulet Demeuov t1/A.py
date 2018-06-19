#STUDENT: Daulet Demeuov
#GROUP: EN1-C-04
#TASK: Task1 problem A
#Description: Read five-digit number; find sum and product of digits.
while True:
    a = str(input('Enter number '))
    b = int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4])
    c = int(a[0])*int(a[1])*int(a[2])*int(a[3])*int(a[4])
    print('Sum:',b)
    print('Product:',c)
