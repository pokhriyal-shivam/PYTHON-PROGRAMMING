#file 1 name as calc.py
def add(x,y):
    return x + y 


#file 2 name as calc2.py
import calc as c
print(c.add(3,5))
