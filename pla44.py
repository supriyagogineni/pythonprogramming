def rat(m,n):
    print(m[n:]+m[:n])
m,n=map(str,raw_input().split())
n=int(n)
k=len(m)-n
rat(m,k)
