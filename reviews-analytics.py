data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: # 每則留言為一行, 每次讀取一行, 共1000000行資料
		data.append(line) # 逐行附加至data空清單中
		count += 1
		if count % 100000 == 0: # 餘數符號 % 意義為若count到1000的倍數才印出來
			print(len(data)) # print 會很花時間, 若無這行會直接印出留言的長度
#print(data[0])
print('檔案讀取完, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	
print('每一筆留言的平均字數是:', sum_len/len(data))

