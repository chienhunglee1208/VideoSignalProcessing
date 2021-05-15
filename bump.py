f = open('bump.txt', 'r')
lines = f.readlines()
x = []
y = []
total = 0

for i in range(0, len(lines)):
	x.append(0)
for i in range(0, len(lines)):
	for j in range(0, len(lines[i])):
		if(lines[i][j] == "*"):
			x[i]+=1
for i in range(0, len(lines)):
	print("第 {} 行裡有 {} 個炸彈".format(i+1, x[i]))
	total += x[i]
print()

for i in range(0, len(lines[0])):
	y.append(0)
for i in range(0, len(lines[0])):
	for j in range(0, len(lines)):
		if(lines[j][i] == "*"):
			y[i]+=1
for i in range(0, len(lines[0])):
	print("第 {} 列裡有 {} 個炸彈".format(i+1, y[i]))
print()

print("總共有 {} 個炸彈".format(total))