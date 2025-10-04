# to find the factorial of a number using python

n = int(input("enter the number"))

product = 1

for i in range(1,n+1):
    
    product = product*i


print(f"the factorial of {n} is {product}")




output:
enter the number7
the factorial of 7 is 5040
