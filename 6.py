def monotonic(arr):
    for i in range(1,n):
        if arr[i] < arr[i - 1]:
            return False 
    return True


arr = list(map(int, input().split()))
n= len(arr)
if monotonic(arr):  
    print("Array is monotonic")
else:
    print("Array is not monotonic")

