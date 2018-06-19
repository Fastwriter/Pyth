a=[0,1,2,
   3,4,5,
   6,7,8]

def xogame():
    print(a[0],'|',a[1],'|',a[2])
    print('----------')
    print(a[3],'|',a[4],'|',a[5])
    print('----------')
    print(a[6],'|',a[7],'|',a[8])

while True:
    p1 = int(input('Choice the square P1(0-8):'))

    if a[p1] != 'x' and a[p1] !='o':
        a[p1] = 'x'
    else:
        print('This square is taken')
        p1 = int(input('Choice the square P1(0-8):'))
    xogame()
    

    p2 = int(input('Choice the square P2(0-8):'))

    if a[p2] != 'x' and a[p2] !='o':
        a[p2] = 'o'
    else:
        print('This square is taken')
        p2 = int(input('Choice the square P2(0-8):'))
    xogame()
    
