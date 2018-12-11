num=int(raw_input())
n1=list(map(int,raw_input().split()))
n2=list(map(int,raw_input().split()))
if set(n1)==set(n2):
    print("yes")
else:
    print("no")
