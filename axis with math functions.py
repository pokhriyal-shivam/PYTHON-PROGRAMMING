import numpy as np

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(np.sum(arr,axis = 0))
print(np.sum(arr,axis = 1))

print(np.mean(arr,axis = 0))
print(np.mean(arr,axis = 1))

print(np.min(arr,axis = 0))
print(np.min(arr,axis = 1))

print(np.max(arr,axis = 0))
print(np.max(arr,axis = 1))

