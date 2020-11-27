"""Creates the CreateUser window.

Typical usage example:
    create_user = CreateUser(root)
    create_user.mainloop()
"""

import tkinter as tk
# from GUI_Authentication import login
from gui_authentication import screen_handler

class CreateUser(tk.Frame):
    """Creates the CreateUser window.

    Attributes:
        master: The master of the CreateUser window.
        frame: The frame containing the widgets for creating a user.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Welcome")

        self.frame = tk.LabelFrame(self.master)
        self.frame.grid(row=1)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.create_borders()
        self.create_permanent_labels()
        self.create_temporary_labels()
        self.create_entries()
        self.create_clickable_labels()
        self.create_buttons()

    def create_borders(self):
        """Creates the blue borders and places them on the CreateUser frame."""

        self.first_line = tk.Canvas(self.frame, height=10, width=200)
        self.first_line.create_rectangle(1,
                                         5,
                                         200,
                                         10,
                                         fill="light blue",
                                         outline="light blue")

        self.first_line.grid(row=2)

    def create_permanent_labels(self):
        """Creates the labels for the CreateUser window.

        Creates both the permanent labels that are always visible on the
        CreateUser window. It also places the permanent labels on the
        CreateUser frame.
        """

        # Permanent labels
        self.new_user_label = tk.Label(self.frame, text="New User")

        self.school_label = tk.Label(self.frame, text="School:")
        self.email_label = tk.Label(self.frame, text="Email:")
        self.invite_code_label = tk.Label(self.frame, text="Invite Code:")
        self.password_label = tk.Label(self.frame, text="Password:")
        self.verify_password_label = tk.Label(self.frame,
                                              text="Verify Password:")

        self.new_user_label.grid(row=1)

        self.school_label.grid(row=3)
        self.email_label.grid(row=5)
        self.invite_code_label.grid(row=7)
        self.password_label.grid(row=9)
        self.verify_password_label.grid(row=11)

    def create_temporary_labels(self):
        """Creates the temporary labels that appear given a condition such as a
        missing field"""
        self.temporary_label = None

        # Temporary labels
        self.forget_field_label = tk.Label(self.frame,
                                           text="You are missing a field!",
                                           fg="red")
        self.different_passwords_label = tk.Label(
            self.frame, text="The passwords do not match!", fg="red")

        self.success_label = tk.Label(
            self.frame,
            text="Account successfully created! Sign in to get started!",
            fg="green")

    def create_entries(self):
        """Creates and places the entry fields for the CreateUser frame."""

        self.school_entry = tk.Entry(self.frame)
        self.email_entry = tk.Entry(self.frame)
        self.invite_code_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame)
        self.verify_password_entry = tk.Entry(self.frame)

        self.school_entry.grid(row=4, padx=10, pady=10)
        self.email_entry.grid(row=6)
        self.invite_code_entry.grid(row=8)
        self.password_entry.grid(row=10)
        self.verify_password_entry.grid(row=12)

    def create_clickable_labels(self):
        """Creates and places labels that can be clicked on for the CreateUser
        frame."""

        text = "Sign in to existing account"
        self.existing_account_label = tk.Label(self.frame,
                                               text=text,
                                               fg="blue")
        self.existing_account_label.configure(font="Verdana 9 underline")

        self.existing_account_label.grid(row=15)
        self.existing_account_label.bind("<Button>",
                                         self.existing_account_response)

    def existing_account_response(self, event):
        """Responds to the existing account label being clicked.
        Args:
            event: A mouse click.
        """

        self.master.destroy()
        new_root = tk.Tk()
        # login.Authentication(new_root).mainloop()
        screen_handler.run_login_screen(new_root)

    def create_buttons(self):
        """Creates and places all the buttons for the CreateUser frame."""

        sign_in = tk.Button(self.frame,
                            text="Create Account",
                            fg="white",
                            bg="blue")
        sign_in["command"] = self.create_account_response
        sign_in.grid(row=13, padx=10, pady=10)

    def create_account_response(self):
        """Responds to the create account button being clicked."""

        self.school = self.school_entry.get().strip()
        self.email = self.email_entry.get().strip()
        self.invite_code = self.invite_code_entry.get().strip()
        self.password = self.password_entry.get().strip()
        self.verify_password = self.verify_password_entry.get().strip()

        valid_entries = self.check_entries()

        # TODO: Connect so that a user is signed up.
        if valid_entries:
            print("Good entries")
        else:
            print("Bad entries")

    def check_entries(self):
        """
        Checks whether the entries are valid.

        Return:
             Returns a boolean value on whether the values entered in the
             entry fields are valid. It is True if the entries are valid and
             False if they are not.
        """

        valid_entries = False

        if self.temporary_label:
            self.forget_temporary_label()

        # Empty entry field
        if (not self.school or not self.email or not self.invite_code
                or not self.password or not self.verify_password):
            self.temporary_label = self.forget_field_label
        # Password and Verify Password don't match
        elif self.password != self.verify_password:
            self.temporary_label = self.different_passwords_label
        else:
            self.temporary_label = self.success_label
            valid_entries = True

        self.temporary_label.grid(row=14)

        print(self.school, self.email, self.invite_code, self.password,
              self.verify_password)

        return valid_entries

    def forget_temporary_label(self):
        """Removes the temporary label."""
        self.temporary_label.grid_forget()


# print("Sign Up")
# root = tk.Tk()
# app = SignUp(master=root)
# app.mainloop()
