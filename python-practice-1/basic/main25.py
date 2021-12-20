from tkinter import *
from tkinter import filedialog

def openFile():
    filePath = filedialog.askopenfilename(title='Open File', filetypes=(('all files', '*.*'),))
    file = open(filePath, 'r')
    print(file.read())
    file.close()

window = Tk()

btn = Button(window, text='Open Dialog Box', font=('Arial', 30),
 command=openFile, padx=10, pady=5, bg='#000', fg='green')
btn.pack()

window.mainloop()
