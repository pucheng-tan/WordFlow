import tkinter as tk
from user_interface.active_windows import active_window

class MyProfileWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # // TODO Make the My Profile Window
        label = tk.Label(self.frame, text="My Profile")
        label.pack()