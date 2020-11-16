import tkinter as tk

import main_menu
from active_windows import home_window

# import context_service

class GUI(object):
    def __init__(self, privilege, master):

        self.privilege = privilege # Will probably be a context manager
        self.master = master

        self.main_menu = main_menu.MainMenu(privilege, self)
        self.active_window = home_window.HomeWindow(self)

        self.main_menu.frame.grid(row=1, column=0)
        self.active_window.show()

root = tk.Tk()

GUI("Standard", root)

root.mainloop()