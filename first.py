n=int(input("Enter a  number: "))
a=len(str(n))
first=int(str(n)[0])
sum1=pow(first,a)
second=int (str(n)[1])
sum2=pow(second,a)  
third=int (str(n)[2])
sum3=pow(third,a)   
print(sum1+sum2+sum3)
if sum1+sum2+sum3==n:
    print("Armstrong number")  
else:
    print("Not an Armstrong number")     