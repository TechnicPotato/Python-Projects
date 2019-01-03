import turtle, time
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
