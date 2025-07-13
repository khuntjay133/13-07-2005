def my_sum(arr):
    total = 0
    for i in arr:
        total += i    
    return total

arr = list(map(int, input().split()))

result = my_sum(arr)
print(result)
