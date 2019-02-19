n1=int(input())
if(n1>0 and (n1 & (n1-1))==0):
    print("0")
else:
    if(n1%2!=0):
        print("1")
    else:
        print("2")
