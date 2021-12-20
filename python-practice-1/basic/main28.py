from tkinter import *



window = Tk()

frame = Frame(window, bd=3, relief=SUNKEN)
frame.pack()

Button(frame, text='W', font=('Consolas', 25), width=3).pack(side=TOP)
Button(frame, text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='D', font=('Consolas', 25), width=3).pack(side=LEFT)


window.mainloop()
