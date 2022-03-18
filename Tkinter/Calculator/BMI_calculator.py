from tkinter import *

root = Tk()

root.title('BMI Calculator')
root.geometry('525x250')

def calculate():
	m = float(e_m.get())
	kg = float(e_kg.get())
	bmi = round(kg / (m**2), 2)
	if bmi < 18.5:
		label4['text'] = f'Range: underweight'
		label3['text'] = f'BMI: {bmi}'
	elif bmi >= 18.5 and bmi < 25:
		label4['text'] = f'Range: healthy'
		label3['text'] = f'BMI: {bmi}'
	elif bmi >= 25 and bmi < 30:
		label4['text'] = f'Range: overweight'
		label3['text'] = f'BMI: {bmi}'
	elif bmi >= 30 and bmi < 40:
		label4['text'] = f'Range: obese'
		label3['text'] = f'BMI: {bmi}'
	else:
		label4['text'] = f'Range: error'
		label3['text'] = f'BMI: {bmi}'


label1 = Label(root, text='Height in meters:', font=('Helvetica', 16))
label1.grid(pady=10, padx=50, column=0, row=0)

e_m = Entry(root, font=('Helvetica', 10))
e_m.grid(pady=10, padx=50, column=0, row=1)

label2 = Label(root, text='Weight in kilograms:', font=('Helvetica', 16))
label2.grid(pady=10, padx=25, column=1, row=0)

e_kg = Entry(root, font=('Helvetica', 10))
e_kg.grid(pady=10, padx=25, column=1, row=1)

button = Button(root, text='Calculate', command=lambda:[calculate()], font=('Helvetica', 16))
button.grid(pady=10, row=3)

label3 = Label(root, text='BMI:', font=('Helvetica', 16))
label3.grid(pady=10, row=4)

label4 = Label(root, text='Range:', font=('Helvetica', 16))
label4.grid(pady=10, row=5)

root.mainloop()