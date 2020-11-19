import tkinter as tk
from user_interface.active_windows import active_window

class ReportsWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # // TODO Make the Reports Window
        # The two lines can be removed once the window starts being made
        label = tk.Label(self.frame, text="Reports")
        label.pack()