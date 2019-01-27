data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: # 每次讀取一行
		data.append(line) # 逐行附加至data空清單中
		count += 1
		if count % 1000 == 0: # 餘數符號 % 意義為若count到1000的倍數才印出來
			print(len(data)) # print 會很花時間, 若無這行會直接印出留言的長度
print(len(data))
print(data[0])
