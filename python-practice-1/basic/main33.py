from tkinter import *

def drag_start(e):
    widget = e.widget
    widget.startX = e.x
    widget.startY = e.y

def motion_start(e):
    widget = e.widget
    x = widget.winfo_x() - widget.startX + e.x
    y = widget.winfo_y() - widget.startY + e.y
    widget.place(x=x, y=y)

window = Tk()

label = Label(window, bg='blue', height=5, width=10)
label.place(x=0,y=0)

label1 = Label(window, bg='green', height=5, width=10)
label1.place(x=50,y=50)

label.bind('<Button-1>', drag_start)
label.bind('<B1-Motion>', motion_start)

label1.bind('<Button-1>', drag_start)
label1.bind('<B1-Motion>', motion_start)

window.mainloop()
