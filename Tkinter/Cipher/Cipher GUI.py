from tkinter import *

root = Tk()

root.title('Cipher')
root.geometry('560x330')


def encrypt(msg, key):
    secret_msg = ""
    for letter in msg:
        secret_msg += chr(ord(letter) + key)
    ans.config(text='')
    ans.config(text=secret_msg)


def encrypt_back(msg, key):
    secret_msg_back = ""
    for letter in msg:
        secret_msg_back += chr(ord(letter) - key)
    ans.config(text='')
    ans.config(text=secret_msg_back)


label1 = Label(root, text='Message:', font=('Courier', 14))
label1.grid(pady=10, padx=30, row=0, column=0)

e1 = Entry(root, font=('Arial', 10), width=40)
e1.grid(pady=10, padx=10, row=0, column=1)

label2 = Label(root, text='Key:', font=('Courier', 14))
label2.grid(pady=20, padx=30, row=1, column=0)

e2 = Entry(root, font=('Arial', 10), width=10)
e2.grid(pady=20, padx=10, row=1, column=1, sticky=W)

label3 = Label(root, text='Encrypted:', font=('Courier', 14))
label3.grid(pady=20, padx=30, row=2, column=0)

ans = Label(root, text='', font=('Arial', 10))
ans.grid(pady=20, padx=10, row=2, column=1, sticky=W)

button1 = Button(root, text='Encrypt', font=(
    'Courier', 14), width=15, height=1, command=lambda: encrypt(str(e1.get()), int(e2.get())))
button1.grid(pady=20, padx=30, row=3, column=0)

button2 = Button(root, text='Encrypt back', font=(
    'Courier', 14), width=15, height=1, command=lambda: encrypt_back(str(e1.get()), int(e2.get())))
button2.grid(pady=20, padx=30, row=3, column=1)


def copy():
    # root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(ans.cget('text'))


button3 = Button(root, text='Copy to clipboard', font=(
    'Courier', 14), width=30, height=1, command=lambda: copy())
button3.grid(pady=20, padx=30, row=4, column=0, columnspan=2)

root.mainloop()
