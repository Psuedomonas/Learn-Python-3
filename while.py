#!/usr/bin/python3
# Filename: while.py

number = 23
running = True

while running:
	guess = int(input('Enter an integer : '))

	if guess == number:
		print('Congratulations, you guessed it.')
		print('(but you did not win any prizes!)')
		running = False
	elif guess < number:
		print('No, it is a little higher then that.')
	else:
		print('No, it is a little lower then that.')
	
if True:
	print('Yes, it is true')

print('Done')


