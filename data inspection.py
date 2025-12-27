import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Mohan", "Aman", "Rohit", "Neha"],
    "Age": [20, 21, 22, 23, 21, 20],
    "Marks": [80, 75, 90, 60, 85, 70]
}

df = pd.DataFrame(data)

# top 5 rows
print(df.head())

# bottom 5 rows
print(df.tail())

# shape
print(df.shape)

# column
print(df.columns)

# info about the data(data health)
print(df.info()) 

# describe(math summary of numeric column)
print(df.describe())
