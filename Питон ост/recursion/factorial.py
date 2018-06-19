def gcd(a,b):
    return b and gcd(b,a%b) or a
def lcm(a,b):
    return (a*b)/gcd(a,b)
