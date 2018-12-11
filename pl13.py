num=int(input())
sum=0
while(num>0):
    n=int(num%10)
    sum=(n*n)+sum
    num=int(num/10)
print(sum)
