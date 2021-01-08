import random

start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('猜一個數字: ')
	num = int(num)
	if num == r:
		print('恭喜你猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('你猜的數字比答案大')
	elif num < r:
		print('你猜的數字比比答案小')
	print('這是你猜的第', count, '次')