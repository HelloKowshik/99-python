from tkinter import *

def func():
    if x.get() == 1:
        print('Thanks for Accept!')
    else:
        print('Please Agree Our Terms!')    

window = Tk()

x = IntVar()

checkbox = Checkbutton(window, text='Accept', variable=x,
 onvalue=1, offvalue=0, command=func,
 font=('Arial', 20), fg='green', bg='#000', padx=20, pady=15,
 activeforeground='green', activebackground='#000'
 )
checkbox.pack()



window.mainloop()
