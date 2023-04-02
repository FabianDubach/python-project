import tkinter as tk

from rock_paper_scissors import RockPaperScissors

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Python Project')

if __name__ == '__main__':
    app = App()
    frame = RockPaperScissors(app)
    app.mainloop()