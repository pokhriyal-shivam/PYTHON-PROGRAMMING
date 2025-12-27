import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Mohan", "Aman", "Rohit", "Neha"],
    "Age": [20, 21, 22, 23, 21, 20],
    "Marks": [80, 75, 90, 60, 85, 70]
}

df = pd.DataFrame(data)

print(df[df["Marks"]>75])

print(df[(df["Marks"]>75) & (df["Age"]>21)])


# data sorting
print(df.sort_values("Marks"))

print(df.sort_values("Marks",ascending=False))
