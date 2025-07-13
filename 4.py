def left_rotate(arr, n,d):

    first = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[-1] = first
    return arr

arr = list(map(int, input().split()))
n = len(arr)
d=int(input("Enter number of rotations: "))
for _ in range(d):

 result = left_rotate(arr, n,d)
print( result)
