import tkinter as tk
from user_interface.active_windows import active_window

class SchoolManagementWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # // TODO Make the School Management Window
        # The two lines below can be removed once the window starts being made
        label = tk.Label(self.frame, text="School Management")
        label.pack()