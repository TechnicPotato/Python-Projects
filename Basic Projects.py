import turtle, time, sys, re
#99 Bottles of Beer
def bottles(n):
	bottles = n
	for i in range(n+1):
		if bottles == 1:
			print(bottles, "bottle of beer on the wall,", bottles,"bottle of beer.")
			print("Take one down and pass it around,", bottles, "bottle of beer on the wall.")
			print()
			bottles-=1
		elif bottles == 0:
			print("No more bottles of beer on the wall, no more bottles of beer.")
			print("Go to the store and buy some more,", n,"bottles of beer on the wall.")

		else:
			print(bottles, "bottles of beer on the wall,", bottles,"bottles of beer.")
			print("Take one down and pass it around,", bottles, "bottles of beer on the wall.")
			print()
			bottles -= 1

#Counts the letters and determines if the count is same for 2 digits
def xo(s,a,b):
	print(s.lower().count(a))
	print(s.lower().count(b))
	return s.lower().count(a) == s.lower().count(b)

#Builds a tower
def tower_builder(n_floors):
    n = n_floors * 2 - 1
    offset = int((n-1)/2)
    a = []
    for i in range(n_floors):
        print(" " * offset + ("*" * ((i+1)*2 - 1)) + " " * offset)
        offset -= 1
#Builds a funny shape
t = turtle.Turtle()
t.ht()
def rotation(distance,n):
	t.speed(10)
	for i in range(n):
		t.fd(distance)
		t.bk(distance/2)
		t.rt(360/n)
	time.sleep(10)
	t.clear()

#Experiments with dictionaries
student_grades = {}
def gradeinput(Name,Grade):
	student_grades[str(Name)] = str(Grade)
def clear():
	student_grades = {}

#Factorisation Stuff
def functionfactorize(n):
	factors = []
	for i in range(2,n+1):
		if n%(i) == 0:
			factors.append(i)
	return(factors)

def isPrime(n):
	return len(functionfactorize(n)) == 1

#Variable Calculator
'''rawstring = input("Enter the raw string")
Just manually edit the rawstring'''
def initialprocessing(rawstring):
	processedstring = rawstring.split("\n")
	stringprocessing = [i.replace(","," ").split() for i in processedstring]
	finalproduct = [[int(i) for i in x] for x in stringprocessing]
	return finalproduct
def secondaryprocessing(rawstring):
	rawlist = initialprocessing(rawstring)
	maximum = max([len(i) for i in rawlist])
	for i in rawlist:
		while True:
			if len(i) < maximum:
				i.append(0)
			else:
				break
	return rawlist

def task(rawstring):
	processedstring = secondaryprocessing(rawstring)
	math = [sum(i) for i in processedstring]
	overallsum =  [sum([b[a] for b in processedstring]) for a in range(0,len(processedstring[0]))]
	
