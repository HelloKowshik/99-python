from tkinter import *

window = Tk()

def submit():
    data = input_field.get()
    print('btn clicked!', data)
    input_field.config(state=DISABLED)
    submit_btn.config(state=DISABLED)

def clearData():
    input_field.delete(0, END)


def backspace():
    input_field.delete(len(input_field.get()) - 1, END)

input_field = Entry(window, font=('courier', 40), show='*')
input_field.pack(side='left')

submit_btn = Button(window, text='Submit', command=submit)
submit_btn.pack(side='right')    

delete_btn = Button(window, text='Clear', command=clearData)
delete_btn.pack(side='right')

backspace_btn = Button(window, text='Backspace', command=backspace)
backspace_btn.pack(side='right')


window.mainloop()
