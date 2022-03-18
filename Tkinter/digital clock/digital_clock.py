from tkinter import *
import time

root = Tk()

root.title('Clock')
root.geometry('500x200')


def clock():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    day = time.strftime('%A')
    am_pm = time.strftime('%p')

    label.config(text=hour + ':' + minute + ':' + second + ' ' + am_pm)
    label.after(1000, clock)

    label2.config(text=day)


label = Label(root, text='', font=('Helvetica', 48), fg='grey', bg='cyan')
label.pack(pady=30)

label2 = Label(root, text='', font=('Helvetica', 14))
label2.pack(pady=10)

clock()

root.mainloop()
