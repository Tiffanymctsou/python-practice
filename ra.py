data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)
print('每筆留言的平均長度是', sum_len/len(data), '個字')

new = []
for d in data: # d是每一個留言(字串); data是清單
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '留言長度小於100個字')
