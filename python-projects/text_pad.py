import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor()
    textarea.config(fg=color[1])

def change_font(*args):
    textarea.config(font=(font_name.get(), font_size_box.get()),)

def new_file():
    window.title('Untitled')
    textarea.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension='.txt', file=[('All Files', '*.*'), ('Text File', '*.txt')])
    try:
        window.title(os.path.basename(file))
        textarea.delete(1.0, END)
        file = open(file, 'r')
        textarea.insert(1.0, file.read())
    except Exception as e:
        print(e)
    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled',defaultextension='.txt', 
        filetypes=[('All Files', '*.*'), ('Text File', '*.txt')]
        )
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, 'w')
            file.write(textarea.get(1.0, END))    
        except Exception as e:
            print(e)
        finally:
            file.close()            


def cut():
    textarea.event_generate('<<Cut>>')

def copy():
    textarea.event_generate('<<Copy>>')

def paste():
    textarea.event_generate('<<Paste>>')                            

def about():
    showinfo('Simple Text Editor', 'Written in Python By Kowshikur Rahman')

def quit():
    window.destroy()


window = Tk()
window.title('Simple Text Editor')
file = None
window_width = 600
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))
font_name=StringVar(window)
font_name.set('Arial')
font_size=StringVar(window)
font_size.set('25')

textarea = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(textarea)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
textarea.grid(sticky=N+E+S+W)

frame = Frame(window)
frame.grid()
color_btn = Button(frame, text='Color', command=change_color)
color_btn.grid(row=0, column=0)
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)
font_size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
font_size_box.grid(row=0, column=2)

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=new_file)
fileMenu.add_command(label='Open', command=open_file)
fileMenu.add_command(label='Save', command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)

helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='About', command=about)

scroll_bar.pack(side=RIGHT, fill=Y)
textarea.config(yscrollcommand=scroll_bar.set)

window.mainloop()
