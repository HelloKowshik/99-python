from tkinter import *

def buttons(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def clearAll():
    global equation_text
    equation_label.set('')
    equation_text = ''

def total():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set('Math Error') 
    except SyntaxError:
        equation_label.set('Syntax Error')      

window = Tk()
window.title('Calculator')
window.config(background='black')
window.geometry('500x500')

equation_text = ''
equation_label = StringVar()

label = Label(window, textvariable=equation_label,
 font=('Consolas', 20),bg='black', fg='whiteSmoke', width=24, height=2
 )
label.pack()
frame = Frame(window)
frame.pack()

btn1 = Button(frame, text=1,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(1))
btn1.grid(row=0, column=0)
btn2 = Button(frame, text=2,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(2))
btn2.grid(row=0, column=1)
btn3 = Button(frame, text=3,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(3))
btn3.grid(row=0, column=2)
plus = Button(frame, text='+',bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons('+'))
plus.grid(row=0, column=3)

btn4 = Button(frame, text=4,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(4))
btn4.grid(row=1, column=0)
btn5 = Button(frame, text=5,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(5))
btn5.grid(row=1, column=1)
btn6 = Button(frame, text=6,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(6))
btn6.grid(row=1, column=2)
minus = Button(frame, text='-',bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons('-'))
minus.grid(row=1, column=3)

btn7 = Button(frame, text=7,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(7))
btn7.grid(row=2, column=0)
btn8 = Button(frame, text=8,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(8))
btn8.grid(row=2, column=1)
btn9 = Button(frame, text=9,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(9))
btn9.grid(row=2, column=2)
multiply = Button(frame, text='*',bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons('*'))
multiply.grid(row=2, column=3)

btn0 = Button(frame, text=0,bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons(0))
btn0.grid(row=3, column=0)
decimal = Button(frame, text='.',bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons('.'))
decimal.grid(row=3, column=1)
div = Button(frame, text='/',bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=lambda: buttons('/'))
div.grid(row=3, column=2)
equal = Button(frame, text='=',bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=9, font=35, command=total)
equal.grid(row=3, column=3)

clear = Button(window, text='Clear',bg='black', fg='whiteSmoke',activebackground='black',activeforeground='whiteSmoke', height=2, width=39, font=35, command=clearAll)
clear.pack()


window.mainloop()            
