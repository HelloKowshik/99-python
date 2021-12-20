from tkinter import *
from time import *

def update():
    time_str = strftime('%I:%M:%S %p')
    time_label.config(text=time_str)
    day_str = strftime('%d %b %Y, %A')
    day_label.config(text=day_str)
    zone_str = strftime('%Z')
    zone_label.config(text=zone_str)

    window.after(1000, update)

window = Tk()
window.config(background='black')
time_label = Label(window, font=('Arial', 50), fg='green', bg='black')
time_label.pack()
day_label = Label(window, font=('Arial', 25), fg='whiteSmoke',bg='black')
day_label.pack()
zone_label = Label(window, font=('courier', 20), fg='whiteSmoke',bg='black')
zone_label.pack()

update()

window.mainloop()
