#!/usr/bin/python3
# Filename: if.py

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
	print('Congratulations, you guessed it.')
	print('(but you did not win any prizes!)')
elif guess < number:
	print('No, it is a little higher then that.')
else:
	print('No, it is a little lower then that.')

if True:
	print('Yes, it is true')

print('Done')


