from tkinter import *

def move_up(e):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)

def move_down(e):    
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)

def move_left(e):    
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())

def move_right(e):    
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())

window = Tk()

window.geometry('500x500')
carImage = PhotoImage(file='car.png')

window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

window.bind('<Up>', move_up)
window.bind('<Down>', move_down)
window.bind('<Left>', move_left)
window.bind('<Right>', move_right)

label = Label(window,image=carImage)
label.pack()





window.mainloop()
