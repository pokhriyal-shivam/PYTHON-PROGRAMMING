import numpy as np
from sklearn.preprocessing import StandardScaler

arr = np.array([[10],[20],[30]])
sc = StandardScaler()

x_scale = sc.fit_transform(arr)
print(x_scale)
