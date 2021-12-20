from tkinter import *

foods = ['Pizza', 'Pasta', 'Chese Burger', 'Hot Dog', 'Chicken Chowmin']

# def order():
#     print(listbox.get(listbox.curselection()))

def multiOrder():
    cur_food = []
    for i in listbox.curselection():
        cur_food.insert(i, listbox.get(i))
    print(cur_food)    

def addItem():
    item = input_field.get()
    foods.append(item)
    listbox.insert(listbox.size(), item)
    listbox.config(height=listbox.size())
    input_field.delete(0, END)

# def deleteItem():
#     current = listbox.get(listbox.curselection())
#     foods.remove(current)
#     listbox.delete(listbox.curselection())
#     listbox.config(height=listbox.size())

def multiDeleteItem():
    for i in reversed(listbox.curselection()):
        # print(i)
        foods.remove(foods[i])
        listbox.delete(i)
    listbox.config(height=listbox.size())

window = Tk()
# listbox = Listbox(window, font=('Constantia', 30), bg='#f7ffde', width=16)
listbox = Listbox(window, font=('Constantia', 30), bg='#f7ffde', width=16, selectmode=MULTIPLE)

for i in range(len(foods)):
    listbox.insert(i, foods[i])

listbox.pack()
listbox.config(height=listbox.size())

label = Label(window, text='Enter New Item:')
label.pack()
input_field = Entry(window, font=('Arial', 30))
input_field.pack()

add_btn = Button(window, text='Add Item', command=addItem)
add_btn.pack()

# delete_btn = Button(window, text='Delete Item', command=deleteItem)
# delete_btn.pack()

multi_delete_btn = Button(window, text='Delete Item', command=multiDeleteItem)
multi_delete_btn.pack()

# submit_btn = Button(window, text='Order', command=order)
# submit_btn.pack()

multi_submit_btn = Button(window, text='Order', command=multiOrder)
multi_submit_btn.pack()


window.mainloop()
