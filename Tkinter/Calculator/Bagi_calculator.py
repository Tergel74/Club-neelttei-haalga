from tkinter import*
root=Tk()
root.title('calculator')
e=Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def button(number):
    current=(e.get())
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def add():
    first_number=e.get()
    global f_num 
    global math 
    math='addition'
    f_num=int(first_number)
    e.delete(0, END)
def sub():
    first_number=e.get()
    global f_num 
    global math 
    math='subtraction'
    f_num=int(first_number)
    e.delete(0, END)
def mul():
    first_number=e.get()
    global f_num 
    global math 
    math='multi'
    f_num=int(first_number)
    e.delete(0, END)
def div():
    first_number=e.get()
    global f_num 
    global math 
    math='divide'
    f_num=int(first_number)
    e.delete(0, END)
def equal():
    second_number=e.get()
    e.delete(0, END)
    if math=='addition':
        e.insert(0, f_num + int(second_number))
    elif math=='subtraction':
        e.insert(0, f_num - int(second_number))
    elif math=='multi':
        e.insert(0, f_num * int(second_number))
    elif math=='divide':
        e.insert(0, f_num / int(second_number))
    else:
        e.insert(0, 'fuck off')
def clear():
    e.delete(0, END)





button_1 = Button(root, text='1', padx=40, pady=20, command=lambda:button(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda:button(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda:button(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda:button(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda:button(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda:button(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda:button(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda:button(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda:button(9))
button_0 = Button(root, text='0', padx=140, pady=20, command=lambda:button(0))
button_a = Button(root, text='+', padx=39, pady=20, command=add)
button_s = Button(root, text='-', padx=39, pady=20, command=sub)
button_d = Button(root, text='/', padx=39, pady=20, command=div)
button_u = Button(root, text='*', padx=39, pady=20, command=mul)
button_e = Button(root, text='=', padx=39, pady=20, command=equal)
button_c = Button(root, text='Clear', padx=130, pady=20, command=clear)


button_1.grid(row=3, column=0, columnspan=1,)
button_2.grid(row=3, column=1, columnspan=1,)
button_3.grid(row=3, column=2, columnspan=1,)
button_d.grid(row=3, column=3, columnspan=1,)

button_4.grid(row=2, column=0, columnspan=1,)
button_5.grid(row=2, column=1, columnspan=1,)
button_6.grid(row=2, column=2, columnspan=1,)
button_s.grid(row=2, column=3, columnspan=1,)

button_7.grid(row=1, column=0, columnspan=1,)
button_8.grid(row=1, column=1, columnspan=1,)
button_9.grid(row=1, column=2, columnspan=1,)
button_a.grid(row=1, column=3, columnspan=1,)

button_0.grid(row=4, column=0, columnspan=3,)
button_u.grid(row=4, column=3, columnspan=1,)

button_c.grid(row=5, column=0, columnspan=3,)
button_e.grid(row=5, column=3, columnspan=1,)
root.mainloop()