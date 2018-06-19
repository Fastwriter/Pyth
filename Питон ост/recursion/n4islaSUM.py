def r(x):
    if(x==0):
        return 0
    else:
        return x%10+r(x//10)
    
