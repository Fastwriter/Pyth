def is_sorted(e):
    for n in range(len(e)-1):
        if all (e[n]<=e[n+1]):
            return True
        else:
            return False
        
