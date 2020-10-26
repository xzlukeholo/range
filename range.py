import random

num = input('你想產生幾個隨機數:')
min1 = input('隨機數的最小值:')
max1 = input('隨機數的最大值:')
min1 = int(min1)
max1 =int(max1)
num = int(num)

for i in range(num):
	r = random.randint(min1, max1)
	print('第', i+1, '個隨機數:', r)

'你想計算多少加到多少的數值呢?'
start = input( '請輸入開始加總的數字:')
end = input( '請輸入結束加總的數字:')
start = int(start)
end = int(end)

sum = 0
for i in range(start, end+1):
	sum += i
print(sum)
