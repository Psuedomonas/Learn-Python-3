#!/usr/bin/python3.2
# Filename: practDef.py

def functA ():
	print("Program A")
	return main()

def functB ():
	print("Program B")
	return main()

def functC ():
	print("Program C")
	return main()

def functD (): 
	print("Closing program...")

def main ():	
	n = input("Your choice : ")
	if n == "A":
		return functA()
	elif n == "B":
		return functB()
	elif n == "C":
		return functC()
	elif n == "D":		
		return functD()

print("Hello, welcome to the program.")
print("You have four choices\n1. Program A\n2. Program B\n3. Program C\n4. Exit this program")
main()

