import random
from turtle import *
t = Turtle()
t.speed(0)

def pen(color):
    t.color(color)

pen('blue')

def move():
    t.pu()
    x = random.randint(-185,165)
    y = random.randint(-185,165)
    t.goto(x,y)
    t.pd()

def sky(colour):
     wn = Screen()
     wn.bgcolor(colour)

sky('black')

def firework(size):
    for num in range (20):
         t.fd(size)
         t.rt(180-(360/20))

firework(50)
move()
pen('purple')
firework(75)
move()

pen('red')
firework(100)   
firework(40)
move()

pen('blue')
firework(85)
move()

pen('pink')
firework(200)
firework(40)
move()

pen('yellow')
firework(75)
move()

pen('orange')
firework(200)   
firework(40)
move()

pen('blue')
firework(75)
move()

pen('pink')
firework(200)
firework(40)
move()

pen('yellow')
firework(75)
move()

pen('orange')
firework(200)   
firework(40)
move()
pen('blue')
firework(75)
move()

done()