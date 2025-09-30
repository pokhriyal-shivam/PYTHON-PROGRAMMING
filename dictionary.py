Marks={
    "shivam":100,
    "yash":10,
    "abhay":99,
    "aditya":89
}

#show the keys and values

# print(Marks.keys())
# print(Marks.values())



#updation

# Marks.update({"yash":98})



#updation + adding new row

Marks.update({"yash":98,"harsh":18})

print(Marks)




print(Marks.get("shivam2"))   #prints none

print(Marks["shivam2"])  #gives an error
