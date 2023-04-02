from tkinter import ttk
import random

class RockPaperScissors(ttk.Frame):

    choices = ['rock', 'paper', 'scissors']
    
    def __init__(self, container):
        super().__init__(container, padding=200)

        self.label = ttk.Label(self, text='rock, paper, scissors').grid(column=1, row=0)

        self.button_rock = ttk.Button(self, text='rock', command=self.rock).grid(column=0, row=1)
        self.button_paper = ttk.Button(self, text='paper', command=self.paper).grid(column=1, row=1)
        self.button_scissors = ttk.Button(self, text='scissors', command=self.scissors).grid(column=2, row=1)

        self.button_play = ttk.Button(self, text='Play', command=self.game).grid(column=1, row=2)
        self.button_quit = ttk.Button(self, text="Quit", command=self.destroy).grid(column=1, row=6)

        self.player_label = ttk.Label(self, text='player choice: ')
        self.player_label.grid(column=1, row=3, sticky='ew')

        self.computer_label = ttk.Label(self, text='computer choice: ')
        self.computer_label.grid(column=1, row=4, sticky='ew')

        self.result_label = ttk.Label(self, text='')
        self.result_label.grid(column=1, row=5, sticky='ew')

        self.pack()

    def rock(self):
        self.player_choice = 'rock'

    def paper(self):
        self.player_choice = 'paper'

    def scissors(self):
        self.player_choice = 'scissors'

    def game(self):
        computer_choice = random.choices(RockPaperScissors.choices, k=1)[0]

        self.player_label.configure(text=f'player choice: {self.player_choice}')
        self.computer_label.configure(text=f'computer choice: {computer_choice}')

        if self.player_choice == computer_choice:
            self.result_label.configure(text='Its a tie!')
        elif self.player_choice == 'rock' and computer_choice == 'scissors':
            self.result_label.configure(text='You win!')
        elif self.player_choice == 'paper' and computer_choice == 'rock':
            self.result_label.configure(text='You win!')
        elif self.player_choice == 'scissors' and computer_choice == 'paper':
            self.result_label.configure(text='You win!')
        else:
            self.result_label.configure(text='You lost!')