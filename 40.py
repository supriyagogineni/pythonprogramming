def f(num):
    if(num<=1):
        return num
    else:
        return (f(num-1)+f(num-2))
num=int(raw_input())
for i in range(1,num+1):
    print f(i),
