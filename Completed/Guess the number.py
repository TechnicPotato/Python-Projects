import random
def enterconditions(x):
	if (type(x)!= int):
		return False
	elif x<1 or x>100:
		return False
	else:
		return True

global previousguess
previousguess = []

def guessline():
	global answer
	answer = random.randint(1,100)
	guessgame()
	
def guessgame():
	guess = input("Guess the number between 1 and 100! pguess() shows previous guesses. ")
	if guess == "pguess()":
		pguess()
		return guessgame()
	elif guess == "answer":
		print(answer)
		return recurse()
	elif guess == "cheat":
		print(answer)
		return guessgame()
	#Remove Error
	else:
		try:
			g = int(guess)
		except ValueError:
			print("Invalid Input!")
			guessgame()
		#Enterconditions
		if enterconditions(g):
			previousguess.append(g)
			if g == answer:
				print("Congratulations! The answer was", answer)
				print("You had", len(previousguess), "guesses")
				input("Any key to start again")
				recurse()
			elif g > answer:
				print("Too high! Try again!")
				guessgame()
			elif g < answer:
				print("Too low! Try again!")
				guessgame()
			else:
				print("Something went wrong somewhere. Someone get Bill!")
				
		else:
			print("Invalid Input")
			guessgame()

def pguess():
	print(previousguess)
	
def recurse():
	input("Press Enter to begin.")
	global previousguess
	previousguess = []
	guessline()
recurse()
	
