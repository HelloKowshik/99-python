from tkinter import *

window = Tk()
points = [200,0,400,400,0,400]
canvas = Canvas(window, height = 400, width = 400)
# canvas.create_line(0, 0, 400, 400, fill='blue', width=5)
# canvas.create_line(0, 400, 400, 0, fill='green', width=5)
# canvas.create_rectangle(50, 50, 250, 250, fill='green')
# canvas.create_polygon(points, fill='orange', outline='black', width=5)
# canvas.create_arc(0,0,400,400,fill='green', style=PIESLICE, extent=180)
canvas.create_arc(0,0,400,400,fill='red', extent=180, width=10)
canvas.create_arc(0,0,400,400,fill='white',start=180, extent=180, width=10)
canvas.create_oval(150,150,250,250, fill='whiteSmoke', width=10)
canvas.pack()

window.mainloop()
