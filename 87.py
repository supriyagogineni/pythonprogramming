k,n=map(int,raw_input().split())
def gcd(a,b):
    z=abs(a-b)
    if (a-b)==0:
        return b
    else:
        return gcd(z,min(a,b))
print gcd(k,n)
