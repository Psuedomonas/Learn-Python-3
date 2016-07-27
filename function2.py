#!/usr/bin/python3
# Filename: function2.py

def printMax(a, b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal')
	else:
		print(b, 'is maximum')

printMax(3,4)
x = 5
y = 7
printMax(x,y)
