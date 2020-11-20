"""Creates the authentication window.

Typical usage example:
    authentication = Authentication(root)
    authentication.mainloop()
"""

import tkinter as tk
from gui_authentication import screen_handler
from managements import user_management

from user_interface import gui


class Authentication(tk.Frame):
    """Creates the authentication window.

    Attributes:
        master: The master of the authentication window.
        frame: The frame containing the widgets for authentication.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Welcome")

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.frame = tk.LabelFrame(self.master)
        self.frame.grid(row=1)

        self.create_borders()
        self.create_permanent_labels()
        self.create_temporary_labels()
        self.create_clickable_labels()
        self.create_entries()
        self.create_buttons()

        # Connect to services
        self.user_management = user_management.UserManagement()

    def create_borders(self):
        """Creates the blue borders and places them on the authentication
        frame."""

        self.first_line = tk.Canvas(self.frame, height=10, width=200)
        self.first_line.create_rectangle(1,
                                         5,
                                         200,
                                         10,
                                         fill="light blue",
                                         outline="light blue")

        self.second_line = tk.Canvas(self.frame, height=10, width=200)
        self.second_line.create_rectangle(1,
                                          5,
                                          200,
                                          10,
                                          fill="light blue",
                                          outline="light blue")

        self.first_line.grid(row=2)
        self.second_line.grid(row=11)

    def create_permanent_labels(self):
        """Creates the permanent labels for the authentication window.

        Creates both the permanent labels that are always visible on the
        authentication window. It also places the permanent labels on the
        authentication frame.
        """

        # Create permanent labels
        self.sign_in_label = tk.Label(self.frame, text="Sign In")

        self.school_label = tk.Label(self.frame, text="School:")
        self.email_label = tk.Label(self.frame, text="Email:")
        self.password_label = tk.Label(self.frame, text="Password:")
        self.new_user_label = tk.Label(self.frame, text="New User")

        # Place permanent labels in their positions
        self.sign_in_label.grid(row=1)
        self.school_label.grid(row=3)
        self.email_label.grid(row=5)
        self.password_label.grid(row=7)
        self.new_user_label.grid(row=12)

    def create_temporary_labels(self):
        """Creates the temporary labels given conditions such as missing
        fields."""

        self.temporary_label = None

        # Create temporary labels
        self.forget_field_label = tk.Label(self.frame,
                                           text="You are missing a field!",
                                           fg="red")

        self.error_label = tk.Label(self.frame,
                                    text="Failed to authenticate",
                                    fg="red")

    def create_entries(self):
        """Creates and places the entry fields for the authentication frame."""

        # Create field entries
        self.school_entry = tk.Entry(self.frame)
        self.email_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame, show="*")

        # Place field entries
        self.school_entry.grid(row=4, padx=10, pady=5)
        self.email_entry.grid(row=6)
        self.password_entry.grid(row=8)

    def create_clickable_labels(self):
        """Creates and places labels that can be clicked on for the
        authentication frame."""

        self.create_school_label = tk.Label(self.frame,
                                            text="Create School",
                                            fg="blue")
        self.create_school_label.configure(font="Verdana 9 underline")

        self.create_school_label.grid(row=14)
        self.create_school_label.bind("<Button>", self.create_school_response)

    def create_school_response(self, event):
        """Responds to the create school label being clicked on.

        Args:
            event: A mouse click.
        """

        self.master.destroy()
        new_root = tk.Tk()
        screen_handler.run_create_school(new_root)

    def create_buttons(self):
        """Creates and places all the buttons for the authentication frame."""

        sign_in = tk.Button(self.frame, text="Sign In", fg="white", bg="blue")
        sign_in["command"] = self.sign_in_response
        sign_in.grid(row=10, padx=10, pady=10)

        sign_up = tk.Button(self.frame, text="Sign Up", fg="white", bg="blue")
        sign_up["command"] = self.sign_up_response
        sign_up.grid(row=13, padx=10, pady=5)

    def sign_in_response(self):
        """Responds to the sign in button being clicked."""

        invalid_entries, response = self.check_entries()

        # TODO: Connect to gui.py to open up welcome screen of user or maybe
        # return True to main.py and main.py will open it up
        if not invalid_entries:
            print("Yes")
            print(response)
            self.master.destroy()
            new_root = tk.Tk()
            gui.GUI(new_root)
        else:
            print("No")
            print(response)

    def check_entries(self):
        """Checks whether the entries are valid.

        Returns:
            A tuple containing whether a temporary label is displayed which is
            True if the entries are invalid and the response from the API.
        """
        display_temporary_label = False
        response = None

        school_id = self.school_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if self.temporary_label:
            self.forget_temporary_label()

        if not school_id or not email or not password:
            self.temporary_label = self.forget_field_label
            display_temporary_label = True
        else:
            response = self.user_management.login(email, password, school_id)
            if "error" in response:
                self.temporary_label = self.error_label
                display_temporary_label = True

        if display_temporary_label:
            self.temporary_label.grid(row=9)

        return (display_temporary_label, response)

    def forget_temporary_label(self):
        """Removes the temporary label."""
        self.temporary_label.grid_forget()

    def sign_up_response(self):
        """Responds to the sign up button being clicked."""

        self.master.destroy()
        new_root = tk.Tk()
        screen_handler.run_signup_screen(new_root)


# root = tk.Tk()
# app = Authentication(master=root)
# app.mainloop()
