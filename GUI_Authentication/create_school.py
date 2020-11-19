"""Creates the CreateSchool window.

Typical usage example:
    create_school = CreateSchool(root)
    create_school.mainloop()
"""

import tkinter as tk
from GUI_Authentication import screen_handler

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

        self.school = self.school_entry.get()
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()
        self.verify_password = self.verify_password_entry.get()

        print(self.school, self.email, self.password, self.verify_password)

        invalid_entries = self.check_entries()

        if not invalid_entries:
            # Creating super-admin and school
            user = self.user_management.create_auth_user(
                self.email, self.password)
            school = self.school_management.create_school(
                self.school, user["id"])
            school_user = self.user_management.create_user_profile(
                self.email, user["id"], 0)
            print(school, school_user)

    def check_entries(self):
        """
        Checks whether the entries are valid.

        Return:
             Returns a boolean value which is whether a temporary label is
             displayed. It is True if the entries are invalid.
        """

        display_temporary_label = False

        if self.temporary_label:
            self.forget_temporary_label()

        if (not self.school or not self.email or not self.password or
                not self.verify_password):
            self.temporary_label = self.forget_field_label
            display_temporary_label = True
        elif self.password != self.verify_password:
            self.temporary_label = self.different_passwords_label
            display_temporary_label = True

        if display_temporary_label:
            self.temporary_label.grid(row=12)

        return display_temporary_label

    def forget_temporary_label(self):
        """Removes the temporary label."""
        self.temporary_label.grid_forget()


# root = tk.Tk()
# app = CreateSchool(master=root)
# app.mainloop()