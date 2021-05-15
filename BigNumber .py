def add(a, b, c):
	ans = []
	num = ""
	for i in range(30):
		ans.append('0')
	for i in range(29, -1, -1):
		aa = int(a[i])
		bb = int(b[i])
		cc = int(c)
		c = str(int((aa+bb+cc)/10))
		d = str((aa+bb+cc)%10)
		ans[i] = d

	for i in range(30):
		if(ans[i] != "0"):
			break
	for j in range(i, 30):
		num += ans[j]
	return num
def eleven(s):
	
A = input("A = ")
B = input("B = ")

a = list(A)
b = list(B)
c = '0'

for i in range(30-len(a)):
	a.insert(0, '0')
for i in range(30-len(b)):
	b.insert(0, '0')

result = add(a, b, c)
print("相加總合 = ", result)
e = eleven(result)
if(e == 1):
	print("是11的倍數")
else:
	print("不是11的倍數")