import math
def gcd(a,b):
    assert int(a) == a and int(b) == b, "The number must be integer"
    if a < 0:
        a = math.mod(a)
    if b < 0:
        b = math.mod(b)
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        if a > b:
            return gcd(b,a%b)
        else:
            return gcd(a,b%a)
        
print(gcd(12,8))