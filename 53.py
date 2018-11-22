m=int(raw_input())
s=[]
while(m>0):
    dig=m%10
    s.append(dig)
    m=m//10
print sum(s)
