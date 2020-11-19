import tkinter as tk
from user_interface.active_windows import active_window

class NewChallengeWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # // TODO Make the New Challenge Window
        label = tk.Label(self.frame, text="New Challenge")
        label.pack()