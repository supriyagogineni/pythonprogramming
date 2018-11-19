minimum= int(raw_input())
def lowest(arr,n):
    minimum= arr[0]
    for i in range(1, n):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum
arr = [1,2,3,4,5]
n = len(arr)
Ans = lowest(arr,n)
print (Ans)
