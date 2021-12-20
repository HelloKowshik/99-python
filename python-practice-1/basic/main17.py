from tkinter import *

window = Tk()
photo = PhotoImage(file='images2.png')
count = 0
def click():
    global count
    count += 1
    print(f'Button Clicked {count} times!')
button = Button(window, text='Click Me', font=('Comic sans', 10, 'bold'), 
    command=click, bg='#000', fg='green', activeforeground='green', 
    activebackground='#000'
    )
window.geometry("500x500")
window.title('Test Window')
window.config(background='#5cfcff')
label = Label(window, text='Kowshikur Rahman',
 font=('courier', 30, 'bold'), 
 fg='whiteSmoke',
 bg='#000',
 relief=SUNKEN,
 bd=5,
 padx=10,
 pady=10,
 image=photo,
 compound='bottom'
 )
label.pack()
button.pack()

window.mainloop()
