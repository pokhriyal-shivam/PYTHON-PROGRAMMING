# program to convert fehreinheit into celcius

def fehreinheit_to_celcius(f):
    return 5*(f-32)/9

f=int(input("enter the temperature : "))

print(f"the temperature into celcius is : {fehreinheit_to_celcius(f)} ")



output:
enter the temperature : 111
the temperature into celcius is : 43.888888888888886
