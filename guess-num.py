import random

r = random.randint(1,100)
while True:
	num = input('Guess the number: ') #input 要存在(=) num 裡面 
	num = int(num) #因為要猜的是數字，所以要讓num變整數(casting 型別轉換)
	if num == r:
		print('You win!')
		break
	elif num > r: #另外如果
		print('It is bigger than answer.')
	elif num < r:
		print('It is smaller than answer.')

