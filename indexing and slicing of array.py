import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

print(arr[1])
print(arr[3])

# 1 to 5 print
print(arr[0:5])

# print with gap of 2
print(arr[0:7:2])

# only print even 
print(arr[arr%2==0])

# normal logic of reverse print with indexes
print(arr[7:0:-1])

# reverse print
print(arr[::-1])

# reverse with gap of 2
print(arr[::-2])
