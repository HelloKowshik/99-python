from tkinter import *

foods = ['pizza', 'hamburger', 'hotdog']

def order():
    item = foods[int(x.get())]
    print(f'You have ordered {item}')


window = Tk()

x = IntVar()
pizza = PhotoImage(file='pizza.png')
hamburger = PhotoImage(file='hamburger.png')
hotdog = PhotoImage(file='hotdog.png')
foodImages = [pizza, hamburger, hotdog]

for index in range(len(foods)):
    radiobtn = Radiobutton(window, text=foods[index],
    variable=x, value=index, padx=30, pady=5, font=('Arial', 25),
    image=foodImages[index], compound='left', indicatoron=0,
    width=400, height=200, command=order
    )
    radiobtn.pack(anchor='w')


window.mainloop()
