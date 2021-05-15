import math

def square(a, b):
	list = []
	if(a > b):
		a, b = b, a
	for i in range(a, b+1):
		isSquare = 1
		s = int(math.sqrt(i))
		s *= s
		if(i != s):
			isSquare = 0
		if(isSquare == 1):
			list.append(i)
	return list

a = int(input("a = "))
b = int(input("b = "))
ans = square(a, b)

print("{}到{}之間的平方數有{}".format(a, b, ans))
print()