try:
    x = float(input("enter first number"))
    y = float(input("enter second number"))
    z = x/y
    print("answer is: ",z)
      
    if y==0:
       raise ZeroDivisionError
    
except ZeroDivisionError:
    print("can't divide from zero")
