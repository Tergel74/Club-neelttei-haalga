from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('500x500')


FRAME2_FONT_SIZE = 16
FONT = 'Arial'
FRAME2_CELL_WIDTH, FRAME2_CELL_HEIGHT = 10, 3

def click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear_screen():
	global expression
	expression = ''
	input_text.set('')

def calc():
	global expression
	result = str(eval(expression))
	input_text.set(result)
	expression = ''

expression=''

input_text = StringVar()

input_frame = Frame(root, width=500, height=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, textvariable=input_text, width=500, justify=RIGHT, font=(FONT, 20, 'bold'))
input_field.grid(column=0, row=0)
input_field.pack(ipady=10)

grid_frame = Frame(root, width=500, height=500, bg='grey')
grid_frame.pack()

seven = Button(grid_frame, text='7', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(7)).grid(row=0, column=0, padx=1, pady=1)
eight = Button(grid_frame, text='8', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(8)).grid(row=0, column=1, padx=1, pady=1)
nine = Button(grid_frame, text='9', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(9)).grid(row=0, column=2, padx=1, pady=1)
divide = Button(grid_frame, text='/', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click('/')).grid(row=0, column=3, padx=1, pady=1)


four = Button(grid_frame, text='4', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(4)).grid(row=1, column=0, padx=1, pady=1)
five = Button(grid_frame, text='5', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(5)).grid(row=1, column=1, padx=1, pady=1)
six = Button(grid_frame, text='6', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(6)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(grid_frame, text='*', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click('*')).grid(row=1, column=3, padx=1, pady=1)


one = Button(grid_frame, text='1', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(1)).grid(row=2, column=0, padx=1, pady=1)
two = Button(grid_frame, text='2', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(2)).grid(row=2, column=1, padx=1, pady=1)
three = Button(grid_frame, text='3', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(3)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(grid_frame, text='-', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click('-')).grid(row=2, column=3, padx=1, pady=1)


zero = Button(grid_frame, text='0', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH * 2, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click(0)).grid(row=3, column=0, columnspan = 2, pady=1, padx=1)
dot = Button(grid_frame, text='.', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click('.')).grid(row=3, column=2, padx=1, pady=1)
plus = Button(grid_frame, text='+', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: click('+')).grid(row=3, column=3, padx=1, pady=1)


clear = Button(grid_frame, text='Clear', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH * 3, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: clear_screen()).grid(row=4, column=0, columnspan = 3, pady=1, padx=1)
equals = Button(grid_frame, text='=', font=(FONT, FRAME2_FONT_SIZE), width=FRAME2_CELL_WIDTH, height=FRAME2_CELL_HEIGHT, cursor='arrow', bd=0, command=lambda: calc()).grid(row=4, column=3,pady=1, padx=1)

root.mainloop()

