cond1 = 3
word1 = 'Fizz'
cond2 = 5
word2 = 'Buzz'
cond3 = 15
word3 = 'FizzBuzz'

for i in range(30):
	if i % cond3 == 0:
		print(word3)
		continue
	elif i % cond2 == 0:
		print(word2)
		continue
	elif i % cond1 == 0:
		print(word1)
		continue
	print(i)
