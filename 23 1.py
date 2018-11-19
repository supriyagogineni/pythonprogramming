m= int(raw_input())
def lowest(arr,n):
    m= arr[0]
    for i in range(1, n):
        if arr[i] < m:
            m = arr[i]
    return m
arr = [1,2,3,4,5]
n = len(arr)
Ans = lowest(arr,n)
print (Ans)
