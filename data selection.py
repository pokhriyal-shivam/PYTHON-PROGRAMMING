import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Mohan", "Aman", "Rohit", "Neha"],
    "Age": [20, 21, 22, 23, 21, 20],
    "Marks": [80, 75, 90, 60, 85, 70]
}

df = pd.DataFrame(data)

# column selection
print(df["Marks"])
print(df[["Name","Marks"]])

# row selection
print(df.iloc[0])
print(df.iloc[1])

print(df.iloc[2,1])


print(df.loc[1, "Marks"])
