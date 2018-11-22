m,n=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
if n in list:
    count=list.count(n)
    print count
else:
    print 0
