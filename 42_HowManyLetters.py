Sentence='The International Conference on Digital Information Processing, Data Mining, and Wireless Communications'

#都轉成小寫
Sentence = Sentence.lower()

#算有幾個不同的字母
listS=list(Sentence)
letters=[]
for let in listS:
	if let not in letters:
		letters.append(let)

print("有{}種不同字母".format(len(letters)))

#算Histogram, 每個字母有幾個
for let in letters:
	print("{}有{}個".format(let, listS.count(let)))

#Histogram用字典表示
dicS1={}
for let in letters:
	dicS1[let]=listS.count(let)
	
print(dicS1)

# Sorted by value
import operator
sorted_dicS1 = sorted(dicS1.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_dicS1)

#此時的sorted_dicS1為list 用 index方式印出內容
for i in range (len(sorted_dicS1)):
	print("{}有{}個".format(sorted_dicS1[i][0], sorted_dicS1[i][1]))

#此時的sorted_dicS1為list 用 list item 方式印出內容
for item in sorted_dicS1:
	print("{}有{}個".format(item[0], item[1]))

#直接用 Histogram Dictionary
dicS2={}

for let in listS:
	keys=dicS2.keys()
	if let not in keys:
		dicS2[let]=1
	else:
		dicS2[let]+=1

print(dicS2)
sorted_dicS2 = sorted(dicS2.items(), key=operator.itemgetter(1), reverse=True)
for item in sorted_dicS2:
	print("{}有{}個".format(item[0], item[1]))
