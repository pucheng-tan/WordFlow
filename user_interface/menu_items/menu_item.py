import tkinter as tk

class MenuItem(object):
    def __init__(self, main_menu):
        self.gui = main_menu.gui
        self.main_menu = main_menu

        self.frame = tk.Frame(self.main_menu.frame)

    def place_on_menu(self, row, column):
        self.frame.grid(row=row, column=column)