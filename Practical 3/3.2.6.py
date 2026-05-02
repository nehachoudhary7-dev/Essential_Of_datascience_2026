import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))


# 1. Searching (indices)
search_result = np.where(array1 == search_value)
print(search_result[0])

# 2. Counting occurrences
count_result = np.count_nonzero(array1 == count_value)
print(count_result)

# 3. Broadcasting addition
broadcast_result = array1 + broadcast_value
print(broadcast_result)

# 4. Sorting
sorted_array = np.sort(array1)
print(sorted_array)
