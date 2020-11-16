import tkinter as tk

class ActiveWindow(object):
    def __init__(self, gui):
        self.frame = tk.Frame(gui.master)

    def show(self):
        self.frame.grid(row=1, column=1)

    def hide(self):
        self.frame.grid_remove()