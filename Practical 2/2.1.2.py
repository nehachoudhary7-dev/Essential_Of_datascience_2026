# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

print("Original Dictionary:", student)

# Insertion
new_key = int(input())
new_value = input()
student[new_key] = new_value
print("After Insertion:", student)

# Update
upd_key = int(input())
upd_value = input()

if upd_key in student:
    student[upd_key] = upd_value

print("After Update:", student)

# Deletion
del_key = int(input())

if del_key in student:
    student.pop(del_key)

print("After Deletion:", student)

# Traversal
print("Traversing Dictionary:")
for key, value in student.items():
    print(f"{key} : {value}")
