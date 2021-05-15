for i in range(1, 10, 1):
	for j in range(1, 10, 1):
		ans = str(i*j)
		if i*j < 10:
			ans = " "+str(ans)
		print(str(i)," * ",str(j)," = ",ans)
	print()
	
print("++++++++++++++++++++++++++++++")
print()

for i in range(1, 10, 1):
	for j in range(1, 10, 1):
		ans = str(i*j)
		if i*j < 10:
			ans = " "+str(ans)
		print(str(i)+" * "+str(j)+" = "+ans,end="  ")
	print()
print()

print("++++++++++++++++++++++++++++++")
print()

for i in range(1, 10, 1):
	for j in range(1, 10, 1):
		