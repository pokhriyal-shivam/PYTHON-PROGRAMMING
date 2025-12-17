list = [1,2,3,4]

with open("hello.txt","a") as file:
    file.write(str(list))


with open("hello.txt","r") as file:
    print(file.read())
