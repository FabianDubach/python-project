from tkinter import *
from tkinter import ttk
import random

player_choice = 0

def rock():
    global player_choice
    player_choice = 'rock'

def paper():
    global player_choice
    player_choice = 'paper'

def scissors():
    global player_choice
    player_choice = 'scissors'

def game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choices(choices, k=1)[0]

    player_label.configure(text=f'player choice: {player_choice}')
    computer_label.configure(text=f'computer choice: {computer_choice}')

    if player_choice == computer_choice:
        result_label.configure(text='Its a tie!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        result_label.configure(text='You win!')
    elif player_choice == 'paper' and computer_choice == 'rock':
        result_label.configure(text='You win!')
    elif player_choice == 'scissors' and computer_choice == 'paper':
        result_label.configure(text='You win!')
    else:
        result_label.configure(text='You lost!')

root = Tk()
frm = ttk.Frame(root, padding=200)
frm.grid()

ttk.Label(frm, text='rock, paper, scissors').grid(column=1, row=0)

ttk.Button(frm, text='rock', command=rock).grid(column=0, row=1)
ttk.Button(frm, text='paper', command=paper).grid(column=1, row=1)
ttk.Button(frm, text='scissors', command=scissors).grid(column=2, row=1)

ttk.Button(frm, text='Play', command=game).grid(column=1, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=6)

player_label = ttk.Label(frm, text='player choice: ')
player_label.grid(column=1, row=3)

computer_label = ttk.Label(frm, text='computer choice: ')
computer_label.grid(column=1, row=4)

result_label = ttk.Label(frm, text='')
result_label.grid(column=1, row=5)

root.mainloop()