from tkinter import *
import random

WIDTH = 600
HEIGHT = 600
SPEED = 100
SPACE_SIZE = 50
BODY = 3
BG_COLOR = '#000'
SN_COLOR = 'green'
FD_COLOR = 'red'

class Snake:
    def __init__(self):
        self.body = BODY
        self.coords = []
        self.squares = []

        for i in range(0, BODY):
            self.coords.append([0, 0])
        for x, y in self.coords:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SN_COLOR, tag='snake')   
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coords = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FD_COLOR, tag= 'food')

def next_turn(snake, food):
    x, y = snake.coords[0]
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    snake.coords.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SN_COLOR)    
    snake.squares.insert(0, square) 

    if x == food.coords[0] and y == food.coords[1]:
        global score
        score += 1
        label.config(text = 'Score: {}'.format(score))
        canvas.delete('food')
        food = Food()

    else:    
        del snake.coords[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):    
        game_over()
    else:    
        window.after(SPEED, next_turn, snake, food)    

def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction 
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction                         


def check_collision(snake):
    x, y = snake.coords[0]
    if x < 0 or x >= WIDTH:
        return True
    elif y < 0 or y >= HEIGHT:
        return True

    for body_part in snake.coords[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")                   

window = Tk()
window.title('Snake Game')
window.config(background=BG_COLOR)
window.resizable(False, False)

score = 0
direction = 'down'
label = Label(window, text='Score: {}'.format(score), font=('Constantia', 30),bg=BG_COLOR, fg='whiteSmoke')
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

window.bind('<Left>', lambda e: change_direction('left'))
window.bind('<Right>', lambda e: change_direction('right'))
window.bind('<Up>', lambda e :change_direction('up'))
window.bind('<Down>', lambda e: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
