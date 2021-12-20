from tkinter import *


def openFile():
    print('File Open')

def saveFile():
    print('File Saved!')  

def cut():
    pass

def copy():
    pass

def paste():
    pass        

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editMenu)

editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_separator()
editMenu.add_command(label='Paste', command=paste)

window.mainloop()
