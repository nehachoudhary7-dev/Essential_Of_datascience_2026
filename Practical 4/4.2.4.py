import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# # write the code


# # Output the most frequent product pairs
# import pandas as pd
# from itertools import combinations
# from collections import Counter

# # Prompt user to input the file name
# file_name = input()


# Group products by Date
grouped = df.groupby('Date')['Product'].apply(list)

pair_counter = Counter()

# Generate product pairs for each date
for products in grouped:
    # Remove duplicates within the same date if any
    unique_products = sorted(set(products))
    
    # Generate all combinations of 2 products
    pairs = combinations(unique_products, 2)
    
    pair_counter.update(pairs)

# Find highest frequency
max_count = max(pair_counter.values())

# Output the most frequent product pairs
for pair, count in pair_counter.items():
    if count == max_count:
        print(f"{pair[0]} and {pair[1]}: {count} times")
