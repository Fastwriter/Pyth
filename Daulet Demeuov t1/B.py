#STUDENT: Daulet Demeuov
#GROUP: EN1-C-04
#TASK: Task1 problem B
#Description: Read one number N (0<N<128). Print binary representation of number N.
while True:
    N=int(input('Enter number'))
    if(0<N<128):
        print(bin(N)[2:].zfill(8))
    else: print('Watt?!')
