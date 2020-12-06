import tkinter as tk
from user_interface.active_windows import active_window
from managements import user_management

class MyProfileWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # // TODO Make the My Profile Window
        self.user_management = user_management.UserManagement()

        self.user_profile = self.user_management.get_logged_in_user_profile()

        self.display_user_profile()

    def display_user_profile(self):
        """Displays the user's profile in the my profile window."""
        self.create_profile()
        profile = ["First Name", "Last Name", "Email", "Display Name", "Privilege Level"]

        privileges = {0: "Super-Admin", 1: "Admin", 2: "Standard"}

        for information in profile:
            user_information = self.user_profile[information.lower().replace(" ", "_")]
            if information == "Privilege Level":
                user_information = privileges[user_information]
            information_label = tk.Label(self.frame, text=information + ": " + user_information)

            information_label.pack()

    def create_profile(self):
        """Creates a full user profile."""
        
        profile_information = ["email", "display_name", "last_name",
                               "first_name", "privilege_level"]

        for information in profile_information:
            if information not in self.user_profile or self.user_profile[information] is None:
                self.user_profile[information] = "-"
