def project():
    a={'apple':'yabloko', 'ball':'m9ch', 'red':'krasnii', 'banana':'banan'}
    y=a.values()
    while True:
        print('1.Search')
        print('2.Add')
        print('3.Delete')
        print('4.Exit')
        print(a)
        f=str(input('Enter your choice:'))
        if(f=='1'):
            b=str(input('Enter searching word:'))
            for i in a:
                if(i==b):
                    print(a[i])
            for i in a:
                if(a[i]==b):
                    print(i)
        elif(f=='2'):
            c=input('Enter adding word:')
            d=input('Enter the translation:')
            a[c]=d
        elif(f=='3'):
            e=input('Enter deleting word:')
            if e in a:
                del a[e]
            elif e in y:
                for i in a:
                    if(a[i]==e):
                        break
                del a[i]
        elif(f=='4'):
            import sys
            sys.exit()
        else:
            print('There is no that choice!')
project()
