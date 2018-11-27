num=raw_input("")
b=len(num)
s=list(num)
if b%2==0:
    m=b/2 - 1
    s[m]='*'
    s[m+1]='*'
else:
    m=b/2 - 1
    s[m+1]='*'
print "".join(s)
