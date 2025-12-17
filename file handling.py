with open("hello.txt","w") as file:
    file.write("hello from the file\n")
    file.write("my name is shivam")


with open("hello.txt","r") as file:
    print(file.read())

    
