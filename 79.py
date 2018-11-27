import math
k,l=map(int,raw_input().split())
a=k * l
if math.sqrt(a).is_integer():
    print "yes"
else:
    print "no"
