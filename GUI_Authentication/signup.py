"""Creates the CreateUser window.

Typical usage example:
    create_user = CreateUser(root)
    create_user.mainloop()
"""

import tkinter as tk
from GUI_Authentication import login


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
        self.create_labels()
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

    def create_labels(self):
        """Creates the labels for the CreateUser window.
        Creates both the permanent labels that are always visible on the
        CreateUser window and the labels that only appear under certain
        conditions such as a missing field. It also places the permanent labels
        on the CreateUser frame.
        """

        # Permanent labels
        self.new_user_label = tk.Label(self.frame, text="New User")

        self.school_label = tk.Label(self.frame, text="School:")
        self.email_label = tk.Label(self.frame, text="Email:")
        self.invite_code_label = tk.Label(self.frame, text="Invite Code:")
        self.password_label = tk.Label(self.frame, text="Password:")
        self.verify_password_label = tk.Label(self.frame,
                                              text="Verify Password:")

        # Temporary labels
        self.forget_label = tk.Label(self.frame,
                                     text="You are missing a field!",
                                     fg="red")
        self.different_passwords_label = tk.Label(
            self.frame, text="The passwords do not match!", fg="red")

        self.new_user_label.grid(row=1)

        self.school_label.grid(row=3)
        self.email_label.grid(row=5)
        self.invite_code_label.grid(row=7)
        self.password_label.grid(row=9)
        self.verify_password_label.grid(row=11)

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
        login.Authentication(new_root).mainloop()

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

        school = self.school_entry.get()
        email = self.email_entry.get()
        invite_code = self.invite_code_entry.get()
        password = self.password_entry.get()
        verify_password = self.verify_password_entry.get()

        if (not school or not email or not invite_code or not password
                or not verify_password):
            # Forget any other labels
            self.different_passwords_label.grid_forget()

            self.forget_label.grid(row=14)
        elif password != verify_password:
            # Forget any other labels
            self.forget_label.grid_forget()

            self.different_passwords_label.grid(row=14)
        else:
            # Forget all labels
            self.forget_label.grid_forget()
            self.different_passwords_label.grid_forget()

            print(school, email, invite_code, password, verify_password)


# print("Sign Up")
# root = tk.Tk()
# app = SignUp(master=root)
# app.mainloop()
