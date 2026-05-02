# Read array input
arr = list(map(int, input().split()))

# Read key
key = int(input())

# Linear search
found = False

for i in range(len(arr)):
    if arr[i] == key:
        print(i)
        found = True
        break

if not found:
    print("Not found")
