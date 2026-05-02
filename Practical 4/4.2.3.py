import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# write the code..



# Group by City and calculate total quantity sold
city_sales = df.groupby('City')['Quantity'].sum()

# Find the city with the highest total quantity sold
best_city = city_sales.idxmax()


# Display the result
print(f"City sold the most products: {best_city}")
