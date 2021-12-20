from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', 
        filetypes=(('Text File', '*.txt'), ('HTML File', '*.html'), ('All Files', '*.*'))
        )
    if file is None:
        return
    data = str(textarea.get(1.0, END))
    file.write(data)
    file.close()
    textarea.delete(1.0, END)

window = Tk()

textarea = Text(window, font=('Ink Free', 25), height=8,
 width=20, padx=20, pady=10)
textarea.pack()
btn = Button(window, text='Save File', command=saveFile)
btn.pack()


window.mainloop()
