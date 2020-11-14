"""Creates the authentication window.

Typical usage example:
    authentication = Authentication(root)
    authentication.mainloop()
"""

import tkinter as tk
from Authentication import create_school, signup


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
        self.create_labels()
        self.create_clickable_labels()
        self.create_entries()
        self.create_buttons()

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

    def create_labels(self):
        """Creates the labels for the authentication window.
        Creates both the permanent labels that are always visible on the
        authentication window and the labels that only
        appear under certain conditions such as a missing field. It also places
        the permanent labels on the authentication frame.
        """

        # Create permanent labels
        self.sign_in_label = tk.Label(self.frame, text="Sign In")

        self.school_label = tk.Label(self.frame, text="School:")
        self.email_label = tk.Label(self.frame, text="Email:")
        self.password_label = tk.Label(self.frame, text="Password:")
        self.new_user_label = tk.Label(self.frame, text="New User")

        # Create temporary labels
        self.forget_label = tk.Label(self.frame,
                                     text="You are missing a field!",
                                     fg="red")

        # Place permanent labels in their positions
        self.sign_in_label.grid(row=1)
        self.school_label.grid(row=3)
        self.email_label.grid(row=5)
        self.password_label.grid(row=7)
        self.new_user_label.grid(row=12)

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
        create_school.CreateSchool(new_root).mainloop()

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

        school = self.school_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not school or not email or not password:
            self.forget_label.grid(row=9)
        else:
            self.forget_label.grid_forget()
            print(school, email, password)

    def sign_up_response(self):
        """Responds to the sign up button being clicked."""

        self.master.destroy()
        new_root = tk.Tk()
        signup.CreateUser(new_root).mainloop()


# root = tk.Tk()
# app = Authentication(master=root)
# app.mainloop()
