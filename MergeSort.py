def Merge(a, b):
	c = []
	Ai = 0
	Bi = 0
	while(Ai<len(a) and Bi<len(b)):
		if(a[Ai] > b[Bi]):
			c.append(b[Bi])
			Bi+=1
		elif(a[Ai] < b[Bi]):
			c.append(a[Ai])
			Ai+=1
		elif(a[Ai] == b[Bi]):
			c.append(a[Ai])
			c.append(b[Bi])
			Ai+=1
			Bi+=1

	while(Ai<len(a) and Bi==len(b)):
		c.append(a[Ai])
		Ai+=1

	while(Ai==len(a) and Bi<len(b)):
		c.append(b[Bi])
		Bi+=1

	return c

a=[1, 3, 5, 7, 9]
b=[2, 3, 4]
ans=Merge(a,b)

print("Merge two sorted list : {}".format(ans))