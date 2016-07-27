#!/usr/bin/python3
# Filename: myClass3

import random

#Program classes
class myObject:
	#population = 0
	'''Initialize the object'''
	def __init__(self, name, health):
		self.name = name
		self.health = health
		#Object.population += 1
		print('{0} has been created'.format(self.name))

	def tell(self):
		'''Tell object values for attributes'''
		print('{0} has {1} health'.format(self.name, self.health))

# Program methods
def A():
	print('So you want to make an object')
	n = input('What will you name it? : ')
	h = random.randint(1,10)
	obj = myObject(n, h)
	obj.tell()

def B():
	print('This will list the objects')
	##
	#

A()
B()
print('end test')
