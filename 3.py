def maxi(arr, n):
    maximum=arr[0]
    for i in range(1, n):
        if arr[i]>maximum:
            maximum=arr[i]
    return maximum
    
        



arr=list(map(int,input().split()))
n= len(arr)
ans=maxi(arr, n)
print("Maximum element is", ans)

