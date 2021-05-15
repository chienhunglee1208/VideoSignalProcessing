def prime(a, b):
	list = []
	if(a > b):
		a, b = b, a
	for i in range(a, b+1):
		isPrime = 1
		for j in range(2, int(i/2)+1):
			if(i % j == 0):
				isPrime = 0
				break
		if(i != 1):
			if(isPrime == 1):
				list.append(i)
	return list

a = int(input("a = "))
b = int(input("b = "))
ans = prime(a, b)

print("{}到{}之間的質數有{}".format(a, b, ans))
print()