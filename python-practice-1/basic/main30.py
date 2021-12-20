from tkinter import *


window = Tk()

firstnameLabel = Label(window, text='First Name:').grid(row=0, column=0)
firstnameEntry = Entry(window).grid(row=0, column=1)

secondnameLabel = Label(window, text='Second Name:').grid(row=1, column=0)
secondnameEntry = Entry(window).grid(row=1, column=1)

emailLabel = Label(window, text='Email:').grid(row=2, column=0)
emailEntry = Entry(window).grid(row=2, column=1)

passwordLabel = Label(window, text='Password:').grid(row=3, column=0)
passwordEntry = Entry(window, show='*').grid(row=3, column=1)

btn = Button(window, text='Sign Up').grid(row=4, column=0, columnspan=2)


window.mainloop()
