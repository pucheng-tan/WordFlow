import tkinter as tk
import active_window

class MyProfileWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # Make the My Profile Window
        label = tk.Label(self.frame, text="My Profile")
        label.pack()