import tkinter as tk
from user_interface.active_windows import active_window

from managements import user_management


class HomeWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.welcome()

    def welcome(self):
        """The home page received when logging in.

        Displays Welcome email!.
        """
        self.user_management = user_management.UserManagement()
        email = self.user_management.get_logged_in_user_profile()["email"]

        home_text = "Welcome " + email + "!"
        self.welcome_label = tk.Label(self.frame,
                                      text=home_text,
                                      font=("Helvetica", 20))
        self.welcome_label.pack()
