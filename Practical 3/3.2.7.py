import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)


# 1. Print all student details
print("All student Details:\n",a)

# 2. print total students

print("Total Students:", len(a))

# 3. Print all student Roll numbers
print("All Student Roll Nos", a[:,0]   )

# 4. Print subject 1 marks
print("Subject 1 Marks", a[:,1])

# 5. print minimum marks of Subject 2
print("Min marks in Subject 2", a[:,2].min()     )

# 6. print maximum marks of Subject 3
print("Max marks in Subject 3", a[:,3].max()    )

# 7. Print All subject marks
a1 = np.delete(a,0,1)
print("All subject marks:", a1      )

# 8. print Total marks of students
print("Total Marks", a[:,1]+a[:,2]+a[:,3]       )

# 9. print average marks of each student
a2 = np.array(a[:,1]+a[:,2]+a[:,3])
A =np.around(a2/3,1)
print(A)

# 10. print average marks of each subject
s1 = (a[:,1]).mean()
s2 = (a[:,2]).mean()
s3 = (a[:,3]).mean()
A1 = np.array((s1,s2,s3))
print("Average Marks of each subject", A1      )

# 11. print average marks of S1 and S2
A2 = np.array((s1,s2))
print("Average Marks of S1 and S2", A2         )

# 12. print average marks of S1 and S3
A3 = np.array((s1,s3))
print("Average Marks of S1 and S3", A3               )

# 13. print Roll number who got maximum marks in Subject 3
i = (a[:,3]).argmax()
r = a[i][0]
print("Roll no who got maximum marks in Subject 3", r)

# 14. print Roll number who got minimum marks in Subject 2
I = (a[:,2]).argmin()
R = a[I][0]
print("Roll no who got minimum marks in Subject 2", R     )

# 15. print Roll number who got 24 marks in Subject 2
r1 = (a[(a[:,2])==24 ,0]).reshape(-1,1)
print("Roll no who got 24 marks in Subject 2", r1                )

# 16. print count of students who got marks in Subject 1 < 40
count = np.argwhere(a[:,1]<40)
c = len(count)
print("Count of students who got marks in Subject 1 < 40",   c            )

# 17. print count of students who got marks in Subject 2 > 90
count1 = np.argwhere(a[:,2]>90)
c1 = len(count1)
print("Count of students who got marks in Subject 2 > 90:", c1             )

# 18. print count of students in each subject who got marks >= 90
Count = [len(np.argwhere(a[:,1]>=90)),len(np.argwhere(a[:,2]>=90)),len(np.argwhere(a[:,3]>=90))]
Count = np.array(Count)
print("Count of students in each subject who got marks >= 90:",  Count            )

# 19. print count of subjects in which each student got marks >= 90
print("Roll no:",   a[:,0]   )
count0 = []
for i in range(len(a[:,0])):
	val = 0
	if a[i][1]>=90:
		val = val + 1
	if a[i][2]>=90:
		val = val + 1
	if a[i][3]>=90:
		val = val + 1
	count0.append(val)
count0 = np.array(count0)
print("Count of subjects in which student got marks >= 90:", count0      )

# 20. Print S1 marks in ascending order
asc = np.sort(a[:,1])
print(asc)

# 21. Print S1 marks >= 50 and <= 90
print(a[a[:,1]>=50])
print(a[a[:,1]<=90])


# 22. Print the index position of marks 79
print(np.where(a[:, 1]==79))





