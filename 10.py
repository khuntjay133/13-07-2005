def twosum(nums,target):
     n=len(nums)
     for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
            return None
    

nums=[2,7,11,15]
   
target=9

result=twosum(nums,target)

if result:
        print("two number add to target", result)

else:
        print("No two numbers add to target")