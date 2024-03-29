from tkinter import *
import random

def next_turn(row, col):
    global player
    if buttons[row][col]['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons[row][col]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+' Turn'))
            elif check_winner() is True:
                label.config(text=(players[0]+' Wins!'))
            elif check_winner() == 'Tie':
                label.config(text='Tie')      
        else:
            buttons[row][col]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=((players[0]+' Turn')))
            elif check_winner() is True:
                label.config(text=(players[1]+' Wins!'))
            elif check_winner() == 'Tie':
                label.config(text='Tie')                

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg='red')
            buttons[row][1].config(bg='red')
            buttons[row][2].config(bg='red')
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != '':
            buttons[0][col].config(bg='red')
            buttons[1][col].config(bg='red')
            buttons[2][col].config(bg='red')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='red')
        buttons[1][1].config(bg='red')
        buttons[2][2].config(bg='red')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='red')
        buttons[1][1].config(bg='red')
        buttons[2][0].config(bg='red')
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg='yellow')
        return 'Tie'
    else:
        return False                                  

def empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != '':
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True                

def new_game():
    global player
    player = random.choice(players)
    label.config(text=(player+' Turn'))
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='', bg='#F0F0F0')

window = Tk()
window.title('Tic-Tac-Toe')
players = ['X', 'O']
player = random.choice(players)
buttons = [[0,0,0], [0,0,0], [0,0,0]]
msg = f'{player} Turn'
label = Label(text= msg, font=('Consolas', 30))
label.pack(side=TOP)

resetBtn = Button(text='Reset', font=('Consolas', 20), command=new_game)
resetBtn.pack(side=TOP)

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text='', font=('Consolas', 25), height=2,
            width=5, command=lambda row=row, col=col: next_turn(row, col)
            )
        buttons[row][col].grid(row=row, column=col)

window.mainloop()                
