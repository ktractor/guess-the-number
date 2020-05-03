sos=0
print('Guess a number between 1, and 100')
import random
num = random.randint(1,100)
while True:
	guess = input()
	i = int(guess)
	if i == num:
		print('you guessed it right! It took you %s turns' % sos)
		break
	elif i < num:
		print('Try higher')
		sos= sos + 1
	elif i > num:
		print('Try lower')
		sos = sos + 1