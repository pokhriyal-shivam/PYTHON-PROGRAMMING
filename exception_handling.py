try:
    a = int(input("hii ,  enter a no"))
    print(a)

except ValueError as v:
    print("hey")
    print(v)

except Exception as e:
    print(e)

print("thank you")
