#!/usr/bin/python3
# Filename: myClass

import random

# Program methods
def A():
	print('So you want to make an object')
	n = input('What will you name it? : ')
	h = random.randint(1,10)
	obj = myObject(n, h)
	obj.tell()

def B():
	print('This will list the objects')
	

def main():
	'''The main program'''
	# Will test the lambda capabilities here, make like lua
	print("Options -- q - quit, a - new object, l - list objects")

	while True:
		s = input('You choose : ')
		if s == 'q':
			break
		elif s == 'a':
			#call new object method
			A()
		elif s == 'l':
			#call test object method
			B()
		elif s == 'c':
			print('Erm. No-one knows what this does yet...')
		else:
			print('I do not understand you.')

#Program classes
class myObject:
	population = 0 # need a system to select objects
	'''Initialize the object'''
	def __init__(self, name, health):
		self.name = name
		self.health = health
		myObject.population += 1
		print('{0} has been created'.format(self.name))

	def tell(self):
		'''Tell object values for attributes'''
		print('{0} has {1} health'.format(self.name, self.health))

	def howmany():
		print('There are {0} objects.'.format(myObject.population))

	#static.method = 

# Program procedure
main()

print()
print('Program Terminated')
