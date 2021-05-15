import random

ans = random.randint(1,99)
count = 0
min = 0
max = 100

print(ans)
while True:
	Start = "請猜一個數字("+str(min)+"-"+str(max)+"):	"
	guess = int(input(Start))
	count += 1
	if ans == guess:
		print("恭喜你，猜中了")
		break
	if ans > guess:
		print("猜的數字太小了")
		min = guess + 1
	if ans < guess:
		print("猜的數字太大了")
		max = guess - 1
		
print("你猜了"+str(count)+"次")
