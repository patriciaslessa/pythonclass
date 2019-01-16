import turtle
import random as rd
#import pylab as plb
import time



def go(obj,x=0,y=0):
    joe.penup()
    joe.goto(x, y)
    joe.pendown()

joe = turtle.Turtle()

go(joe,x=50,y=50)

#square
for _ in range(4):
    joe.forward(100)
    joe.right(90)
joe.clear()

#tri
joe.pencolor('red')
for _ in range(3):
    joe.forward(100)
    joe.right(120)

#joe.

turtle.mainloop()
