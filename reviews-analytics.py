data = []
count = 0
with open('reviews.txt', 'r') as f: # reviews.txt 要放在與 reviews-analytics.py 同一個資料夾
	for line in f: # 每則留言為一行, 每次讀取一行, 共1000000行資料
		data.append(line) # line字串逐行附加至data空清單中
		count += 1
		if count % 1000000 == 0: # 餘數符號 % 意義為若count到1000的倍數才印出來
			print(len(data)) # print 會很花時間, 若無這行會直接印出留言的長度(字母)
#print(data[0])
print(data[2])
print('第三筆留言字母有', len(data[2]), '個')
print('檔案讀取完, 總共有', len(data), '筆資料')

sum_len = 0
for d in data: # d:字串 data:清單
	sum_len += len(d)
# 若寫成 for d in data[i], data[i]的每個字會被個別存到d裡, print(len(d))時會印出垂直排列的111111111
print('每一筆留言的平均字數是:', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料長度小於100')