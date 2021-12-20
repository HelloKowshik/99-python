from tkinter import *


# def doSomething(e):
    # print('You Tried:', e)
    # print('You Pressed:', e.keysym)
    # label.config(text=e.keysym)

def mouse_event(e):
    # print('Event: ', e)
    # label.config(text=e.keysym)
    data = f'x={e.x}, y={e.y}'
    label.config(text=data)

window = Tk()

# window.bind('<Key>', doSomething)
# window.bind('<Key>', mouse_event)
window.bind('<Motion>', mouse_event)

# label = Label(window, font=('Helvatica', 100))
label = Label(window, font=('Helvatica', 50))
label.pack()

window.mainloop()
