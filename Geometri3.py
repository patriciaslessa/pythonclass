import turtle
import random as rd
#import pylab as plb
#import time

drunk = turtle.Turtle(shape='circle')

step = 10
p_step = 0.5
p_angle = 0.5

for _ in range(1000):
    print(drunk.pos())
    if rd.random() < p_angle:
        drunk.left(90)
    else:
        drunk.left(-90)

    if rd.random() < p_step:
        drunk.forward(step)
    else:
        drunk.backward(step)

turtle.mainloop()
