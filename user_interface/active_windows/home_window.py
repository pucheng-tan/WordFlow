import tkinter as tk
from user_interface.active_windows import active_window

class HomeWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.welcome()

    def welcome(self):
        home_text = "Welcome" + "!"
        self.welcome_label = tk.Label(self.frame, text=home_text, font=("Helvetica", 20))
        self.welcome_label.pack()