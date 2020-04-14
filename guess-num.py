import random
start = input ('Enter the start number: ')
end = input ('Enter the end number: ')

start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('Guess the number: ') #input 要存在(=) num 裡面 
	num = int(num) 
	if num == r:
		print('You win!')
		print('This is the', count, 'time.')
		break
	elif num > r: #另外如果
		print('It is bigger than answer.')
	elif num < r:
		print('It is smaller than answer.')
	print('This is the', count, 'time.')