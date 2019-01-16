import turtle
import random as rd
#import pylab as plb
#import time

pos = 10

for _ in range(5):
    if rd.random() < 0.5:
        drunk.forward(pos)
        drunk.bakward(pos)

joe = turtle.Turtle()

go(joe, x=50, y=50)
square(joe, 100)

joe.clear()

#tri
# joe.pencolor('red')
# for _ in range(3):
#     joe.forward(100)
#     joe.right(120)


turtle.mainloop()
