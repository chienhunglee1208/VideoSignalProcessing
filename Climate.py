def disp_area():
	for i in range(0, 25, 1):
		if i < 9:
			j = ' ' + str(i+1)
		else:
			j = str(i+1)
		print(j, ": ", climate_data[i][0], end = '\t')

def disp_temp(data):
        print("顯示區域: ", data[0])
        print("---------------------")
        for i in range(1, 13):
                print("{:>2}月均溫: {}度".format(i, float(data[i])))
        print("本地區年均溫度為{}度".format(data[13]))
        print("---------------------")
target_file = 'climate.txt'
with open(target_file, 'r', encoding='utf-8') as fp:
	raw_data = fp.readlines()
climate_data = []
for item in raw_data:
        climate_data.append(item.rstrip('\n').split('\t'))

while True:
	disp_area()
	area = int(input("請輸入你要查詢平均溫度的地區 : (-1結束)"))
	if area == -1: break
	disp_temp(climate_data[area-1])
	x = input("請輸入Enter鍵回主選單")
	print()
