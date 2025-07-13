def remainder(arr, n):
    total = 1
    for i in arr:
        total *= i
        total %= n
    return total

arr = [100, 10, 50, 40, 50]

n = int(input("Enter the number to divide by: "))

ans = remainder(arr, n)

print("Remainder is", ans)
