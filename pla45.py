k,m=map(int,raw_input().split())
p=int(k/2)
q=int(m**0.5)
if(p*2==k and q*q==m):
    print("yes")
else:
    print("no")
