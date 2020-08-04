def fizzbuzz():
	count = 0
	while True:
		count += 1
		if count == 100:
			break
		if count % 3 == 0 and count % 5 != 0:
			print('Fizz')
			continue
		if count % 5 == 0 and count % 3 != 0:
			print('Buzz')
			continue
		if count % 3 == 0 and count % 5 == 0 and count != 0:
			print('FizzBuzz')
			continue
		print(count)
		
fizzbuzz()