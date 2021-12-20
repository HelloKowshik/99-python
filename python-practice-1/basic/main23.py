from tkinter import *
from tkinter import messagebox


def showMsg():
    # messagebox.showinfo(title='Message Box', message='Thanks For Clicking!')
    # messagebox.showwarning(title='Warning', message='Alert Before Clicking!')
    # messagebox.showerror(title='Error', message='Something Went Wrong!')
    # messagebox.askokcancel(title='Agreement', message='OK/Cancel')
    # messagebox.askretrycancel(title='Try Again', message='Try Again?') # return True/False
    # messagebox.askyesno(title='YES/NO', message='Do you like cheeese?')
    # answer = messagebox.askquestion(title='Answer', message='Will You Play?')
    # if answer == 'yes':
    #     messagebox.showinfo(title='Message', message='Thanks for Playing!')
    # else:
    #     messagebox.showinfo(title='Message', message='Best of luck!')

    check = messagebox.askyesnocancel(title='Message', message='Do you like Python?')
    if check == True:
            messagebox.showinfo(title='Message', message='That is cool!')
    elif check == False:
            messagebox.showinfo(title='Message', message='Very sad!')
    else:
        messagebox.showinfo(title='Message', message='Unknown!')                



window = Tk()

add_btn = Button(window, text='Click', command=showMsg)
add_btn.pack()

window.mainloop()
