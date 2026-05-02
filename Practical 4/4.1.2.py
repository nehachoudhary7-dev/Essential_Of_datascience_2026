import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# -----------------------------
# Add a new row
new_name = input("New name: ")
new_age = int(input("New age: "))
new_row = {'Name': new_name, 'Age': new_age}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("After adding a row:\n", df)

# -----------------------------
# Modify a row
row_to_modify = int(input("Index of row to modify: "))
new_age_value = int(input("New age: "))
df.at[row_to_modify, 'Age'] = new_age_value
print("After modifying a row:")
print(df)

# -----------------------------
# Delete a row
row_to_delete = int(input("Index of row to delete: "))
df = df.drop(index=row_to_delete).reset_index(drop=True)
print("After deleting a row:")
print(df)

# -----------------------------
# Add a new column
genders_input = input("Enter genders separated by space: ").split()
df['Gender'] = genders_input
print("After adding a new column:")
print(df)

# -----------------------------
# Modify a column (convert Name to uppercase)
df['Name'] = df['Name'].str.upper()
print("After modifying a column:")
print(df)

# -----------------------------
# Delete a column (Age)
df = df.drop(columns=['Age'])
print("After deleting a column:")
print(df)



