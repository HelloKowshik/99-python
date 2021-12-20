from tkinter import *
import time

HEIGHT = 500
WIDTH = 500
xVelocity = 3
yVelocity = 2

window = Tk()

ufo = PhotoImage(file='ufo.png')
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

my_image = canvas.create_image(0,0,image=ufo,anchor=NW)
ufo_width = ufo.width()
ufo_height = ufo.height()

while True:
    coords = canvas.coords(my_image)
    if coords[0] >= (WIDTH-ufo_width) or coords[0] < 0:
        xVelocity = -xVelocity
    if coords[1] >= (HEIGHT-ufo_height) or coords[1] < 0:
        yVelocity = -yVelocity    
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
