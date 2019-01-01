#Dice Rolling Simulator
import random
def validconditions(x):
	if (type(x) == int) and (x>0):
		return True
	else:
		return False


#Finds factors of X
def findfactors(x):
	global factortable
	factortable = []
	for i in range(1,x+1):
		if x % i == 0:
			factortable.append(i)
#Calculates the middle two factors required to obtain x
def centering(x):
	global a
	global b
	length = len(factortable)
	hlength = length / 2 
	if length % 2 == 0:
		hlength = int(hlength)
		a = factortable[hlength]
		b = factortable[(hlength-1)]
	elif length % 2 == 1:
		a = factortable[int((hlength-0.5))]
		b = a
	else:
		print("Something went wrong")
		return False
	
#Rolls a die and formulates it into a table. 
def rolldie(x):
	if validconditions(x):
		findfactors(x)
		centering(x)
		dtable = []
		c = 1
		#Dividers
		for i in range((6*a) -1):
			print("-", end ="")
		print()
		#Centres the title
		for i in range((3*a)-9):
			print("*", end = "")
		print(" Dice Roll Table ", end ="") #14 length
		for i in range((3*a)-9):
			print("*", end="")
		print()
		#More Dividers
		for i in range((6*a) -1):
			print("_", end ="")
		print()
		#Forming the Table
		for i in range(x):
			dtable.append(random.randint(1,6))
		for i in range(x):
			if i != a and i != (c*a):
				print("|",dtable[i], end = " | ")
			elif i == (a * c):
				print()
				print("|",dtable[i], end = " | ")
				c += 1
			else:
				print("Failure")
			
	else:
		print("Invalid Conditions")
		