import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# write your code here..

print("First five rows:")
print(data.head())

# 2. Calculate average age (2 decimal places)
avg_age = round(data["Age"].mean(), 2)
print("Average age:", avg_age)

# 3. Filter students with grade up to 'B'
filtered = data[data["Grade"].isin(["A", "B"])]

print("Students with a grade up to B")
print(filtered)
