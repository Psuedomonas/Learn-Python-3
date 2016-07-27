#!/usr/bin/python3.2
# Filename: using_file.py

poem = '''\
This is or would be a poem
It has multiple lines
I really don't care
I just need to learn how this works
'''

'''f = open('poem.txt', 'w') # open file for 'w'riting
f.write(poem) # write text to file
f.close() # close the file'''

f = open('poem.txt') # if no mode is specified, 'r'ead is assumed by default
while True:
  line = f.readline()
  if len(line) == 0: # Zero length indicates EOF
    break
  print(line, end='')
f.close() # close the file
