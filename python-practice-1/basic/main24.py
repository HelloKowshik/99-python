from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser


def addColor():
    color = colorchooser.askcolor()
    # window.config(background=color[1])
    textarea.config(background=color[1])
    # msg = f'You have Choose: {color}'
    # messagebox.showinfo(title='Color Picker', message=msg)

def saveText():
    pass

window = Tk()

window.geometry('420x420')

textarea = Text(window, font=('Ink Free', 25), height=8,
 width=20, padx=20, pady=10
 )
textarea.pack()

txtBtn = Button(window, text='Save Text', command=saveText)
txtBtn.pack()
btn = Button(window, text='Click To Add Color', command=addColor)
btn.pack()

window.mainloop()
