# Read input
num_courses = int(input())
marks = list(map(int, input().split()))

# Check fail condition
if any(mark < 40 for mark in marks):
    print("Fail")
else:
    aggregate = sum(marks) / num_courses
    
    # Print exactly as required
    print(f"Aggregate Percentage: {aggregate:.2f}")
    
    if aggregate > 75:
        print("Grade: Distinction")
    elif aggregate >= 60:
        print("Grade: First Division")
    elif aggregate >= 50:
        print("Grade: Second Division")
    else:
        print("Grade: Third Division")
