#Bouncing Ball Simulator
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball Simulator v0.3")

ball = turtle.Turtle()
ball.shape = ("circle")
ball.penup()
ball.speed(0)
ball.color("green")
ball.goto(0,200)
ball.dy = 0

gravity = 9.8

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)


screen.mainloop()
