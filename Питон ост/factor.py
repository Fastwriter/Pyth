def factor(n):
    if n==0:
        return 1
    else:
        recurse = factor(n-1)
        result = n * recurse
        return result
