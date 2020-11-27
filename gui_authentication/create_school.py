"""Creates the CreateSchool window.

Typical usage example:
    create_school = CreateSchool(root)
    create_school.mainloop()
"""

import tkinter as tk
from gui_authentication import screen_handler

from managements import school_management, user_management


class CreateSchool(tk.Frame):
    """Creates the CreateSchool window.

    Attributes:
        master: The master of the CreateSchool window.
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
        self.create_clickable_labels()
        self.create_entries()
        self.create_buttons()

        # Create user manager
        self.user_management = user_management.UserManagement()

        # Create school manager
        self.school_management = school_management.SchoolManagement()

    def create_borders(self):
        """Creates the blue borders and places them on the CreateSchool
        frame."""

        self.first_line = tk.Canvas(self.frame, height=10, width=200)
        self.first_line.create_rectangle(1,
                                         5,
                                         200,
                                         10,
                                         fill="light blue",
                                         outline="light blue")

        self.first_line.grid(row=2)

    def create_permanent_labels(self):
        """Creates the labels for the CreateSchool window.
        
        Creates both the permanent labels that are always visible on the
        CreateSchool window. It also places the permanent labels on the
        CreateSchool frame.
        """

        # Create permanent labels
        self.new_school_label = tk.Label(self.frame, text="New School")

        self.school_label = tk.Label(self.frame, text="School:")
        self.email_label = tk.Label(self.frame, text="Email:")
        self.password_label = tk.Label(self.frame, text="Password")
        self.verify_password_label = tk.Label(self.frame,
                                              text="Verify Password:")

        # Place permanent labels into their positions
        self.new_school_label.grid(row=1)

        self.school_label.grid(row=3)
        self.email_label.grid(row=5)
        self.password_label.grid(row=7)
        self.verify_password_label.grid(row=9)

    def create_temporary_labels(self):
        """Creates the temporary labels given conditions such as missing
        fields."""

        self.temporary_label = None

        # Create temporary labels
        self.forget_field_label = tk.Label(self.frame,
                                           text="You are missing a field!",
                                           fg="red")

        self.different_passwords_label = tk.Label(
            self.frame, text="The passwords do not match!", fg="red")

        self.password_too_short_label = tk.Label(
            self.frame,
            text="Password must be at least six characters long!",
            fg="red")

        self.success_label = tk.Label(
            self.frame,
            text="School successfully created! Sign in to get started!",
            fg="green")

    def create_entries(self):
        """Creates and places the entry fields for the CreateSchool frame."""

        self.school_entry = tk.Entry(self.frame)
        self.email_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame)
        self.verify_password_entry = tk.Entry(self.frame)

        self.school_entry.grid(row=4, padx=10, pady=5)
        self.email_entry.grid(row=6)
        self.password_entry.grid(row=8)
        self.verify_password_entry.grid(row=10)

    def create_clickable_labels(self):
        """Creates and places labels that can be clicked on for the CreateSchool
        frame."""

        self.create_school_label = tk.Label(self.frame,
                                            text="Sign in to existing account",
                                            fg="blue")
        self.create_school_label.configure(font="Verdana 9 underline")

        self.create_school_label.grid(row=13)
        self.create_school_label.bind("<Button>",
                                      self.existing_account_response)

    def existing_account_response(self, event):
        """Responds to the existing account label being clicked."""

        self.master.destroy()
        new_root = tk.Tk()
        screen_handler.run_login_screen(new_root)

    def create_buttons(self):
        """Creates and places all the buttons for the CreateSchool frame."""

        sign_in = tk.Button(self.frame,
                            text="Create School",
                            fg="white",
                            bg="blue")
        sign_in["command"] = self.create_school_response
        sign_in.grid(row=11, padx=11, pady=10)

    def create_school_response(self):
        """Responds to the create school button being clicked."""

        self.school = self.school_entry.get().strip()
        self.email = self.email_entry.get().strip()
        self.password = self.password_entry.get().strip()
        self.verify_password = self.verify_password_entry.get().strip()

        print(self.school, self.email, self.password, self.verify_password)

        valid_entries = self.check_entries()

        if valid_entries:
            # Creating super-admin and school
            user = self.user_management.create_auth_user(
                self.email, self.password)
                
            school = self.school_management.create_school(
                self.school, user["id"])
            if "error" not in school:
                school_user = self.user_management.create_user_profile(
                    self.email, user["id"], 0)
                print(school, school_user)
                print("Good entries")
            else: 
                self.temporary_label["text"] = school["error"]

    def check_entries(self):
        """
        Checks whether the entries are valid.

        Return:
             Returns a boolean value on whether the values entered in the entry
             fields are valid. It is True if the entries are valid and False if
             they are not.
        """
        print(self.password)

        valid_entries = False
        if self.temporary_label:
            self.forget_temporary_label()

        # Empty entry field
        if (not self.school or not self.email or not self.password
                or not self.verify_password):
            self.temporary_label = self.forget_field_label
        # Passwords and Verify Password don't match
        elif self.password != self.verify_password:
            self.temporary_label = self.different_passwords_label
        # Password too short, must be at least 6 characters long
        elif len(self.password) < 6:
            self.temporary_label = self.password_too_short_label
        # Valid entries
        else:
            self.temporary_label = self.success_label
            valid_entries = True

        self.temporary_label.grid(row=12)

        return valid_entries

    def forget_temporary_label(self):
        """Removes the temporary label."""
        self.temporary_label.grid_forget()


# root = tk.Tk()
# app = CreateSchool(master=root)
# app.mainloop()
