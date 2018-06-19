x=int(input('Your letter mass:'))
y=40
if(0 < x<30):
    print('Cost: 40 sinas')
if(30<=x<50):
    print('Cost:',y+15, 'sinas')
if(50<=x<100):
    print('Cost:',y+30, 'sinas')
if(x>=100):
    x = x - 100
    c = x / 50;
    if (x / 50 == int(x / 50)):
        print('Cost:',70 + int(c * 25), 'sinas')
    else:
        print('Cost:',70 + ((int(c) + 1) * 25), 'sinas')
