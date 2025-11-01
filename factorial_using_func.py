# to print the factorial of user input number using function 


def factorial(n):
    if(n==0 or n==1):
        return 1
    
    return n * factorial(n-1)


n= int(input("enter number: "))

print(f"the factorial of your number is : {factorial(n)}")



OUTPUT:

enter number: 6
the factorial of your number is : 720
