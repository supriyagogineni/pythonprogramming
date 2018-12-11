m=raw_input()
n=len(m)
c=list(m)
for i in range(n):
    c[i]=ord(m[i])+3
for j in range(n):
    c[j]=chr(c[j])
print ''.join(c)
