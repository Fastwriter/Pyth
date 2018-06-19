def is_anagram(a,b):
    c=list(a)
    c.sort()
    d=list(b)
    d.sort()
    if(c==d):
        return True
    else:
        return False
