def func():
    import math
    A=input('X1')
    B=input('Y1')
    C=input('X2')
    D=input('Y2')
    E=input('R')
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    E=int(E)
    F=float(((C-A)**2+(D-B)**2)**0.5)
    if(F<E):
        print('inside')
    else:
        print('outside')
