import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Mohan", "Aman", "Rohit", "Neha"],
    "Age": [20, 21, 22, 23, 21, 20],
    "Marks": [80, 75, 90, 60, 85, 70]
}

df = pd.DataFrame(data)

df["result"] = df["Marks"]>=75
print(df)
