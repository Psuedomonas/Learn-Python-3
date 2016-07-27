#!/usr/bin/python3
# Filename: TrialbyFire
''' 
By Nicholas A Zehm
08-Jan-2013
An attempt at making a monster dueling pseudo game
call it - TrialbyFire
File name - ObjStor.py
Version 0.5.1
  - impliment monster objects via dictionary
  - main menu set up
  - makeMon
  - killMon
  - selectMon
  - Battle
  - SavePen(TODO)
  - LoadPen(TODO)
Wed 09 Jan 2013 10:04:20 PM CST 
'''

import random
import time
import pickle

# Storage file
penabFile = 'MonsterPen2.dat'

# The monster pen
ab = {}

def savePen():
  '''Write pen to file'''
  f = open(penabFile, 'wb')
  pickle.dump(ab, f) # dump the object to a file
  f.close()
  print('*** Pen saved ***')
  main()


def loadPen():
  '''Load pen to file'''
  f = open(penabFile, 'rb')
  ab = pickle.load(f) # load object from file
  print('*** Pen loaded ***')
  showPen()
  main()


def showPen():
  '''Show monsters in pen (dictionary) '''
  for name, health in ab.items():
    print('Name : {0}  \t Health: {1}'.format(name, health))


def makeMon():
  '''makes a new monster (entry in the dictionary)'''
  name = input("Enter the new monster's name : ")
  health = int(input("Enter the new monster's health : "))
  ab[name] = health
  if name in ab:
    print('{0} is now in pen!'.format(name))
  else:
    print('For mysterious reasons, {0} died on way to pen'.format(name))
  return main ()


def killMon():
  '''kills a monster in the pen'''
  showPen()
  name = input('\nWhich monster do you want to kill? : ')
  if name in ab:
    kmonst = input('Are you sure you want to kill {0}, who has {1} health? '.format(name, ab[name]))
    if kmonst == 'yes':
      del ab[name]
      print('\n{0} has been killed... Its bloody corpse was eaten by the others.\n'.format(name))
      showPen()
  else:
    print('\n{0} is not in the pen!\n'.format(name))
  print('Leaving the slaughterhouse...\n')
  return main()


def selectMon():
  '''chooses a monster for the battle pit'''
  showPen()
  name1 = input('Choose a monster to fight in the battle dome!\n')
  if name1 in ab:
    monst1 = name1
  else:
    print('\n{0} is not in the pen!\n'.format(name1))
    return main()

  name2 = input('Choose the monster to fight {0}!\n'.format(name1))
  if name2 in ab:
    monst2 = name1
  else:
    print('\n{0} is not in the pen!\n'.format(name2))
    return main()
  print('\nEntering the battle pit!')
  return Battle(name1, name2)


def Battle(mon1, mon2):
  '''The battle'''
  alive = True
  h1 = int(ab[mon1])
  h2 = int(ab[mon2])
  h1a = h1
  h2a = h2

  while alive:
    atckFst = random.randint(1,2) # first to attack
    attack = random.randint(1,4)  # attack skill
    defend = random.randint(1,4)  # defender deflect
    if atckFst == 1: # 1 attack first
      print('\n{0} attacks {1}...'.format(mon1, mon2))
      time.sleep(0.5)
      if attack == 1: # failed attack
        print('\t{0} completely missed.'.format(mon1))
      else:  # attack success
        if defend == 1: # defend success
          print('\t{0} deflected attack'.format(mon2))
        else: # defend fail
          if h2 > 1:
            h2 = h2 - 1
            ab[mon2] = h2
            print('\t{0} injured by {1}, health now {2}'.format(mon2, mon1, h2))
          else:
            h2 = 0
            ab[mon2] = h2
            alive = False
            print('\n{0} killed! {1} wins!'.format(mon2,mon1))
    elif atckFst == 2: # 2 attack first
      print('\n{0} attacks {1}...'.format(mon2, mon1))
      time.sleep(0.5)
      if attack == 1: # failed attack
        print('\t{0} completely missed.'.format(mon2))
      else:  # attack success
        if defend == 1: # defend success
          print('\t{0} deflected attack'.format(mon1))
        else: # defend fail
          if h1 > 1:
            h1 = h1 - 1
            ab[mon1] = h1
            print('\t{0} injured by {1}, health now {2}.'.format(mon1,mon2,h1))
          else:
            h1 = 0
            ab[mon2] = h1
            alive = False
            print('\n{0} killed! {1} wins!'.format(mon1,mon2))
    time.sleep(1)

    #proc = input('')
    #if proc == 'exit': break

  ''' Kill dead monster '''
  if h1 == 0:
    print("{0} devours {1}'s corpse!".format(mon2,mon1))
    h2 = h2a + h1a//2 - ((h2a - h2)//4)
    ab[mon2] = h2
    print('{0} heals to {1} health!\n'.format(mon2, h2))
    del ab[mon1]
  elif h2 == 0:
    print("{0} devours {1}'s corpse!".format(mon1,mon2))
    h1 = h1a + h2a//2 - ((h1a - h1)//4)
    ab[mon1] = h1
    print('{0} heals to {1} health!'.format(mon1, h1))
    del ab[mon2]
  proc = input('')
  print('Exiting Arena!')
  return main()


def main():
  '''The Main Menu function'''
  print('You can : \n\t"check"\tout the monsters in the pen.\n\t"add"\ta new monster to the pen.\n\t"kill"\ta monster from the pen.')
  print('\t"fight" monsters in the pen.\n\t"save"\tthe pen\n\t"load"\tPen from file\n\t"exit"\tthe dome.')

  i = input('What would you like to do? : ')
  if i == 'c' or i == 'check':
    print('\nThere are {0} monsters in the pens'.format(len(ab)))
    showPen()
    wait = input('')
    return main()
  elif i == 'a' or i == 'add':
    return makeMon()
  elif i == 'f' or i == 'fight':
    return selectMon()
  elif i == 'k' or i == 'kill':
    return killMon()
  elif i == 's' or i == 'save':
    return savePen()
  elif i == 'l' or i == 'load':
    return loadPen()


# Program procedure
print('*** Welcome to the monster battle dome! ***')
main()
print('\nLeaving the battle dome...')
