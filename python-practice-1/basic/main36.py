from tkinter import *
import time
from Ball import *

HEIGHT = 500
WIDTH = 500

window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH, bg='goldenrod')
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, 'green')
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, 'yellow')
foot_ball = Ball(canvas, 0, 0, 110, 2, 1, 'red')

while True:
    volley_ball.move()
    tennis_ball.move()
    foot_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
