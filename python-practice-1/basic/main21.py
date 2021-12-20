from tkinter import *

def submit():
    print(f'Current Temparature: {scale.get()}')

window = Tk()

scale = Scale(window, from_=100, to=0, length=400, 
    orient='horizontal', tickinterval=10, troughcolor='#69EAFF', 
    fg='#FF1C00', bg='#111111'
    )
scale.pack()

submit_btn = Button(window, text='Get Temparature', command=submit)
submit_btn.pack()


window.mainloop()
