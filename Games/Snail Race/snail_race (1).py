from turtle import *
from random import *
from time import *

sc = Screen()
setup(800, 500)
title("Snail race")
bgcolor("light blue")
speed(0)

penup()
goto(-100, 205)
color("purple")
write("SNAIL RACE", font=("Arial", 20, "bold"))

goto(-350, 200)
pendown()
color("pink")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

gap_size = 20
shape("square")
penup()

color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()

snail1 = Turtle()
wn = Screen()
wn.addshape(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\giphy_3.gif')
snail1.shape(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\giphy_3.gif')
snail1.penup()
snail1.goto(-300, 150)
snail1.pendown()

snail2 = Turtle()
wn = Screen()
wn.addshape(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\giphy_2.gif')
snail2.shape(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\giphy_2.gif')
snail2.penup()
snail2.goto(-300, 50)
snail2.pendown()

snail3 = Turtle()
wn = Screen()
wn.addshape(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\giphy.gif')
snail3.shape(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\giphy.gif')
snail3.shapesize(1.5)
snail3.penup()
snail3.goto(-300, -50)
snail3.pendown()

snail4 = Turtle()
wn = Screen()
wn.addshape(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\giphy_1.gif')
snail4.shape(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\giphy_1.gif')
snail4.shapesize(1.5)
snail4.penup()
snail4.goto(-300, -150)
snail4.pendown()

while snail1.xcor() <= 230 and snail2.xcor() <= 230 and snail3.xcor() <= 230 and snail4.xcor() <= 230:
    snail1.forward(randint(1, 10))
    snail1.penup()

    snail2.forward(randint(1, 10))
    snail2.penup()

    snail3.forward(randint(1, 10))
    snail3.penup()

    snail4.forward(randint(1, 10))
    snail4.penup()

Screen().bye()

if snail1.xcor() > snail2.xcor() and snail1.xcor() > snail3.xcor() and snail1.xcor() > snail4.xcor():
    print('SNAIL1 HAS WON! ')
    from tkinter import *
    window = Tk()
    window.title('WINNER')
    window.geometry('1280x720')
    photo = PhotoImage(
        file=r"C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\1st_SNAIL_HAS_WON.png")
    w = Label(window, image=photo)
    w.pack()
    window.mainloop()

elif snail2.xcor() > snail1.xcor() and snail2.xcor() > snail3.xcor() and snail2.xcor() > snail4.xcor():
    print('SNAIL2 HAS WON! ')
    from tkinter import *
    window = Tk()
    window.title('WINNER')
    window.geometry('1280x720')
    photo = PhotoImage(
        file=r"C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\2nd_SNAIL_HAS_WON.png")
    w = Label(window, image=photo)
    w.pack()
    window.mainloop()


elif snail3.xcor() > snail1.xcor() and snail3.xcor() > snail2.xcor() and snail3.xcor() > snail4.xcor():
    from tkinter import *
    window = Tk()
    window.title('WINNER')
    window.geometry('1280x720')
    photo = PhotoImage(
        file=r"C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\3rd_SNAIL_HAS_WON.png")
    w = Label(window, image=photo)
    w.pack()
    window.mainloop()


elif snail4.xcor() > snail1.xcor() and snail4.xcor() > snail2.xcor() and snail4.xcor() > snail3.xcor():
    from tkinter import *
    window = Tk()
    window.title('WINNER')
    window.geometry('1280x720')
    photo = PhotoImage(
        file=r"C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail Race\Assets\4th_SNAIL_HAS_WON.png")
    w = Label(window, image=photo)
    w.pack()
    window.mainloop()
