#Happy New Year
import time,datetime,turtle,tkinter,random
from tkinter import Tk
from turtle import Turtle
#returns seconds til new year

def trigger():
	time = datetime.datetime(2019, 1,1,0,0,0)
	ctime = datetime.datetime.now()
	dif =  time - ctime
	return dif.seconds	
		
root = Tk()	
def window():
	global root
	global count
	count = tkinter.Message(root, text = "Filler!")
	count.config(font=("times", 72, "bold"))
	count.pack()
	
	
def countdown(n):
	n = str(n)
	count.config(text = n + " seconds!")
	root.update()
	
def start():
	window()
	while True:
		secondsleft = trigger()
		countdown(secondsleft)
		time.sleep(1)
		if secondsleft == 0:
			root.destroy()
			break
	fireworks()
	
	
def fireworks():
	turtles = []
	for i in range(10):
		turtles.append(turtle.Turtle())
	for Turtle in turtles:
		Turtle.lt(90)
		Turtle.color("white")
		Turtle.pencolor("red")
		Turtle.speed(10)
	turtles[9].pencolor("white")
	for Turtle in turtles:
		Turtle.fd(200)
	turtles.pop(9)
	for Turtle in turtles:
		a = random.randint(1,360)
		Turtle.lt(a)
	for Turtle in turtles:
		b =  random.randint(100,200)
		Turtle.fd(b)
		
start()
	
	
	
#root.mainloop()