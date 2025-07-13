def sum_list(list1, list2):
     ans = []
     n1 = len(list1)
     n2 = len(list2)
     for i in range(n1):
        for j in range(n2):
            if i == j: 
             ans.append(list1[i] + list2[j])
     return ans

list1 = [5, 10, 15, 20, 25]
list2 = [10, 20, 30, 40, 50]
result = sum_list(list1, list2)
print("Sum of element:", result)
