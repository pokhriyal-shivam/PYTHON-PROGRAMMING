from sklearn.preprocessing import MinMaxScaler

X = [[10],[20],[30]]
mm = MinMaxScaler()
print(mm.fit_transform(X))
