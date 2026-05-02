x=int(input())
if(x>0 and x<=9):
	print(x**2)
elif(x>9 and x<=99):
	print(f"{x**(0.5):.2f}")
elif(x>99 and x<=999):
	print(f"{x**(1/3):.2f}")
else:
	print("Invalid")
