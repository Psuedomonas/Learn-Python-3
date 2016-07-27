#!/usr/bin/python3
# Filename: TrialbyFire
''' 
By Nicholas A Zehm
08-Jan-2013
An attempt at making a monster dueling pseudo game
call it - TrialbyFire
File name - myClassMonster.py
Version 0.2
'''


import random # for random numbers
import time # for delay stuff
import pickle # save data

# The Monster Object
class monster:
  '''Initialize the monster'''
  def __init__(self, name, health):
    self.name = name
    self.health = health
    print('{0} has been created'.format(self.name))

  def tell(self):
    '''tell object attributes'''
    print('{0} has {1} health'.format(self.name, self.health))

  def sendHealth(self)
    return self.health

  def sendName(self)
    return self.name

# Create monsters
def creator():
  print('\nLets make a monster!')
  n = input('What shall it be named? : ') # get name
  h = random.randint(1,20) # make monster health
  obj = monster(n, h)
  obj.tell()


# obj battle
def battle():
  alive = 1
  atckFst = random.randint(1,2) # first to attack
  attack = random.randint(1,3)  # attack skill
  defend = random.randint(1,3)  # defender deflect
  
  while alive !=0:
    if atckFst == 1: # 1 attack first
      x = 1
      xnm = monster.sendName(1)
      xh = monster.sendHealth(1)
      y = 
      ynm
    elif atckFst == 2: #2 attack first
      x = 2
    else: print("some sort of error in the attack first...")
      alive = 0
    print('{0} attacks {1}'.format(xnm, ynm))

    

    if attack == 1: # failed attack
      print('{0} completely missed.'.format(xnm))
    elif:  # attack success
      if defend == 1: # defend success
        print('{0} deflected attack', )
      elif: # defend fail
        print('')         
    elif atckFst == 2: # 2 attack first

  if xh <= 0 or yh <= 0:
    alive = 0

# save data to disk
def savToFile():
  f = open(SavFilName, 'wb')


# read data from disk
def getFromFile():
  f = open(SaveFilName, 'rb')

'''The main program'''
SavFilName = 'monsterls.data' # save file
  print('Welcome to the monster battle dome')
  m = input('What do you want to do?\n"create" a new monster\n"load" an old monster\nor quit? : ')
  if m == 'c' or m == 'create':
    return creator()
  elif m == 'l' or m == 'load':
    return load()
  else:
    print('Closing Program...')
main()  # main function
print('\nend test') # indicate successful run

