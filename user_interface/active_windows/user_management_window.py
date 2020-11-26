"""Contains the classes for the GUI relating to user management.

Contains both the class for the user management window itself and also the class
for viewing an individual user in the user management window.
Imported modules are school_management and user_management. school_management is
necessary to get the ids of all the users in the school for super-admin users.
user_management is necessary to get the information about the user.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from user_interface.active_windows import active_window

from managements import school_management, user_management


class UserManagementWindow(active_window.ActiveWindow):
    """Creates the window managing users.

    Has different buttons for adding and inviting users as well as viewing the
    users which can then be selected to manage them on an individual basis.
    """
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # To get the users in the school
        self.school_management = school_management.SchoolManagement()
        self.user_management = user_management.UserManagement()

        self.create_heading_frame()
        self.create_user_management_notebook()

    def show(self):
        """See base class."""
        self.frame.pack(expand=True, fill=tk.BOTH)

    def create_heading_frame(self):
        """Creates and places the frame that contains the first row of widgets
        for user management."""

        heading_frame = tk.Frame(self.frame)
        heading_frame.pack(fill=tk.X, pady=20)

        user_management_label = tk.Label(heading_frame,
                                         text="User Management",
                                         font=("Helvetica", 20, "bold"))
        user_management_label.pack(side=tk.LEFT)

        new_user_button = tk.Button(heading_frame,
                                    text="New User",
                                    fg="white",
                                    bg="blue")
        invite_all_button = tk.Button(heading_frame,
                                      text="Invite All",
                                      fg="white",
                                      bg="blue")

        new_user_button["font"] = ("Helvetica", 20)
        invite_all_button["font"] = ("Helvetica", 20)

        invite_all_button.pack(side=tk.RIGHT, padx=20)
        new_user_button.pack(side=tk.RIGHT, padx=20)

    def create_user_management_notebook(self):
        """Creates the part of the window with the tabs for managing different
        levels of users.

        For admin users, the only users they can manage are standard users in
        their classrooms. Super-admin users can manage users at all levels and
        any user that is in the school.
        """
        self.user_management_notebook = ttk.Notebook(self.frame)
        self.user_management_notebook.pack(expand=True, fill=tk.BOTH)

        # TODO Check privilege, might already be done if self.privilege is an attribute of GUI
        self.create_standard_frame()

        # If the user is a super-admin
        if self.privilege == 0:
            self.create_admin_frame()
            self.create_super_admin_frame()

        self.create_tabs(self.privilege)

    def create_standard_frame(self):
        """Creates the frame for managing standard users."""
        self.standard_frame = tk.Frame(self.user_management_notebook)
        self.standard_frame.pack()

    def create_admin_frame(self):
        """Creates the frame for managing admin users."""
        self.admin_frame = tk.Frame(self.user_management_notebook)
        self.admin_frame.pack()

    def create_super_admin_frame(self):
        """Creates the frame for managing super-admin users."""
        self.super_admin_frame = tk.Frame(self.user_management_notebook)
        self.super_admin_frame.pack()

    def create_tabs(self, privilege):
        """Creates the tabs to navigate between managing the different users.

        Admin users have only one tab for standard users. Super-admins have
        three tabs for standard, admin, and super-admin users.
        Args:
            privilege: The privilege level of the user managing other users.
        """
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=("Helvetica", "20", "bold"))

        # Associate a tab with its frame
        self.user_management_notebook.add(self.standard_frame, text="Standard")
        # If the user is a super-admin
        if privilege == 0:
            self.user_management_notebook.add(self.admin_frame, text="Admin")
            self.user_management_notebook.add(self.super_admin_frame,
                                              text="Super-Admin")

        self.user_management_notebook.bind("<<NotebookTabChanged>>",
                                           self.tab_change)

    def tab_change(self, event):
        """When a new tab is changed, changes the frame to hold the appropriate
        users.

        Args:
            event: Clicking on a new tab.
        """
        notebook = self.user_management_notebook
        tab_text = notebook.tab(notebook.select(), "text")

        if "Super" in tab_text:
            self.get_users(0)
        elif "Admin" in tab_text:
            self.get_users(1)
        else:
            self.get_users(2)

    def get_users(self, user_privilege):
        """Gets the users with the appropriate privilege for the tab.

        The standard tab gets standard users. The admin tab gets admin users.
        The super-admin tab gets super-admin users.

        Args:
            user_privilege: The privilege of the users associated with the tab.
        """
        if user_privilege == 0:
            frame = self.super_admin_frame
        elif user_privilege == 1:
            frame = self.admin_frame
        else:
            frame = self.standard_frame

        for widget in frame.winfo_children():
            widget.destroy()

        # Create a frame with a scroll bar
        self.view_users_frame = tk.Frame(frame)
        self.users_scroll_bar = tk.Scrollbar(self.view_users_frame)
        self.users_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.users_table = ttk.Treeview(
            self.view_users_frame,
            yscrollcommand=self.users_scroll_bar.set,
            selectmode="browse",
            style="Custom.Treeview")

        self.users_scroll_bar.config(command=self.users_table.yview)
        self.view_users_frame.pack(side=tk.LEFT,
                                   fill=tk.X,
                                   expand=True,
                                   padx=20)
        self.users_table.pack(fill=tk.X)
        self.users_table["columns"] = ("Name", "Email", "Date Created",
                                       "Last Sign In")

        # Format the columns of the table with the users
        self.users_table.column("#0", width=0, stretch=tk.NO)
        self.users_table.column("Name", anchor=tk.CENTER, minwidth=350)
        self.users_table.column("Email", anchor=tk.W, minwidth=350)
        self.users_table.column("Date Created", anchor=tk.CENTER, minwidth=200)
        self.users_table.column("Last Sign In", anchor=tk.CENTER, minwidth=200)

        # Create the headings of the table with the users
        self.users_table.heading("#0", text="", anchor=tk.W)
        self.users_table.heading("Name", text="Name", anchor=tk.CENTER)
        self.users_table.heading("Email", text="Email", anchor=tk.W)
        self.users_table.heading("Date Created",
                                 text="Date Created",
                                 anchor=tk.CENTER)
        self.users_table.heading("Last Sign In",
                                 text="Last Sign In",
                                 anchor=tk.CENTER)

        # TODO: actually connect to API to get real users
        users = self.user_management.get_school_users(0, user_privilege)
        print(users)

        count = 0
        for i in range(0, len(users)):
            user_data = self.user_management.get_user_data(users[i])
            values = (user_data[0], user_data[1], user_data[2], user_data[3],
                      user_data[4], user_data[5])
            if i % 2 == 0:
                self.users_table.insert(parent="",
                                        index="end",
                                        iid=count,
                                        text="",
                                        values=values)
            else:
                self.users_table.insert(parent="",
                                        index="end",
                                        iid=count,
                                        text="",
                                        values=values,
                                        tags=("odd", ))

            count += 1

        # Style the table
        users_table_style = ttk.Style()
        users_table_style.configure("Treeview.Heading", font=(None, 20))
        users_table_style.configure("Treeview", font=(None, 18), rowheight=40)
        # Should be working but....
        self.users_table.tag_configure("odd", background="light gray")

        # Todo: Figure out how to configure heading...

        self.create_actions_frame(frame)

    def create_actions_frame(self, frame):
        """Creates the frame that contains the actions for managing the users in
        the table.

        Args:
            frame: The frame that the frame with the actions will go on.
        """
        actions_frame = tk.Frame(frame)
        actions_frame.pack(side=tk.RIGHT, expand=True)

        self.actions_label = tk.Label(actions_frame, text="Actions")
        self.actions_label["font"] = ("Helvetica", 20)
        self.actions_label.pack()

        self.view_button = tk.Button(actions_frame,
                                     text="View User",
                                     fg="white",
                                     bg="blue")
        self.view_button["font"] = ("Helvetica", 20)
        self.view_button.pack()

        self.view_button["command"] = self.view_user_response

    def view_user_response(self):
        """When the view user button in the actions frame is clicked, it brings
        up the appropriate window to view the chosen user."""

        cur_item = self.users_table.focus()
        # print(cur_item, self.mytree.item(cur_item))
        selected_item = self.users_table.item(cur_item)
        # print(selected_item["values"])
        # TODO: Figure out what actually needs to be sent to UserInformationWindow
        if selected_item["values"]:
            self.hide()
            user_info = selected_item["values"]
            user_information_Window = UserinformationWindow(
                self.gui, user_info)
            self.gui.active_window = user_information_Window
            self.gui.active_window.show()


class UserinformationWindow(active_window.ActiveWindow):
    """Creates the window for viewing and individual selected user.

    Includes the buttons for different operations for a user and displays a
    user's profile information.
    """
    def __init__(self, gui, user_info):
        active_window.ActiveWindow.__init__(self, gui)

        self.user_management = user_management.UserManagement()

        self.user_info = user_info
        self.first_name = self.user_info[0]
        self.last_name = self.user_info[0]
        self.email = self.user_info[1]
        self.date_created = self.user_info[2]
        self.last_sign_in = self.user_info[3]
        self.user_id = self.user_info[4]
        self.user_privilege = self.user_info[5]

        # Creating the different parts of the user information window
        self.create_heading()
        self.create_actions_frame()
        self.create_profile_frame()

    def show(self):
        """See base class."""
        self.frame.pack(fill=tk.BOTH)

    def create_heading(self):
        """Creates and places the frame that contains the first row of widgets
        for viewing a user."""

        heading_frame = tk.Frame(self.frame)
        heading_frame.pack(side=tk.TOP, fill=tk.X)

        user_management_label = tk.Label(heading_frame,
                                         text="User Management: ")
        back_to_users_button = tk.Button(heading_frame,
                                         text="Back To Users",
                                         fg="white",
                                         bg="blue")

        user_management_label["font"] = ("Helvetica", 25, "bold")
        back_to_users_button["font"] = ("Helvetica", 20)

        user_management_label.pack(side=tk.LEFT, padx=20, pady=20)
        back_to_users_button.pack(side=tk.RIGHT, padx=20, pady=20)

        back_to_users_button["command"] = self.back_to_users_response

    def back_to_users_response(self):
        """Goes back to the user management window when the back to users button
        is clicked."""

        self.hide()
        user_management_Window = UserManagementWindow(self.gui)
        self.gui.active_window = user_management_Window
        self.gui.active_window.show()

    def create_actions_frame(self):
        """Creates and places the frame with the actions for the chosen user
        being viewed."""

        actions_frame = tk.Frame(self.frame)
        actions_frame.pack(fill=tk.X, pady=20)
        # TODO: Figure out what users with what privilege should get what buttons and make the functions for clicking them
        # Create the buttons
        invite_button = tk.Button(actions_frame,
                                  text="Invite",
                                  fg="white",
                                  bg="blue")
        assign_newchallenge_button = tk.Button(actions_frame,
                                               text="Assign New Challenge",
                                               fg="white",
                                               bg="blue")
        reports_button = tk.Button(actions_frame,
                                   text="Reports",
                                   fg="white",
                                   bg="blue")
        if self.privilege == 0:
            remove_user_button = tk.Button(actions_frame,
                                           text="Remove User",
                                           fg="white",
                                           bg="blue")
            remove_user_button["command"] = self.remove_user_response

        buttons = [
            widget for widget in actions_frame.winfo_children()
            if widget.winfo_class() == "Button"
        ]

        for button in buttons:
            button["font"] = ("Helvetica", 20)
            button.pack(side=tk.LEFT, expand=True)

    def remove_user_response(self):
        self.user_management.remove_user(self.user_id)

    def create_profile_frame(self):
        """
        Creates and places the frame that holds the profile information for the
        user and if applicable, the way to change the privilege of the user.

        Only super-admin users can change the privilege of a user, so the
        mechanism for changing the privilege of users only appears for
        super-admin users.
        """
        print(self.user_info)

        # TODO: Connect to API or figure out appropriate way to get user information
        profile_frame = tk.Frame(self.frame)
        profile_frame.pack(fill=tk.BOTH, pady=20)

        profile_label = tk.Label(profile_frame, text="Profile")
        first_name_label = tk.Label(profile_frame,
                                    text="First Name: " + self.first_name)
        last_name_label = tk.Label(profile_frame,
                                   text="Last Name: " + self.last_name)
        email_label = tk.Label(profile_frame, text="Email: " + self.email)
        date_created_label = tk.Label(profile_frame,
                                      text="Date Created: " +
                                      self.date_created)
        last_sign_in_label = tk.Label(profile_frame,
                                      text="Last Sign In: " +
                                      self.last_sign_in)
        classroom_label = tk.Label(profile_frame, text="Classroom: 1")

        labels = [
            widget for widget in profile_frame.winfo_children()
            if widget.winfo_class() == "Label"
        ]

        for label in labels:
            if "Profile" in label["text"]:
                label["font"] = ("Helvetica", 25, "bold")
            else:
                label["font"] = ("Helvetica", 20, "bold")
            label.pack(anchor=tk.W)

        if self.privilege == 0:
            self.change_privilege_option(profile_frame)

    def change_privilege_option(self, frame):
        """
        Makes the mechanism to change the privilege level of the user being
        viewed.

        Args:
            frame: The frame that mechanism to change the privilege level of the
            user being viewed is to be placed on.
        """
        user_privilege_label = tk.Label(frame, text="User Privilege")
        user_privilege_label["font"] = ("Helvetica", 20)

        privileges = ["Super-Admin", "Admin", "Standard"]

        self.change_privilege = tk.StringVar()
        self.change_privilege.set(
            privileges[self.user_privilege])  # Default privilege
        self.privilege_option_menu = tk.OptionMenu(frame,
                                                   self.change_privilege,
                                                   *privileges)

        self.change_privilege_button = tk.Button(frame,
                                                 text="Change User Privilege",
                                                 fg="white",
                                                 bg="blue")

        self.privilege_option_menu.configure(font=("Helvetica", 20))
        self.change_privilege_button["font"] = ("Helvetica", 20)

        self.change_privilege_button[
            "command"] = self.change_privilege_response

        user_privilege_label.pack(side=tk.LEFT, padx=20, pady=20)
        self.privilege_option_menu.pack(side=tk.LEFT, padx=20)
        self.change_privilege_button.pack(side=tk.LEFT)

        if not self.user_privilege:
            self.privilege_option_menu.configure(state=tk.DISABLED)
            self.change_privilege_button["state"] = tk.DISABLED

    def change_privilege_response(self):
        """Handles changing the privilege of the user when the change privilege
        button is clicked.

        If the privilege level is to be changed to super-admin, the change
        cannot be undone.
        """
        new_privilege = self.change_privilege.get()
        response = 0

        if "Super" in new_privilege:
            new_privilege = 0
        elif "Admin" in new_privilege:
            new_privilege = 1
        else:
            new_privilege = 2

        if new_privilege == self.user_privilege:
            messagebox.showinfo(
                "Privilege Change Failed",
                "The user already has this level of privilege.")
        else:
            if new_privilege == 0:
                messagebox.showwarning(
                    "Super-Admin",
                    ("Changing the privilege level of a user to a super-admin"
                     "cannot be undone!")
                )

            response = messagebox.askyesno(
                "Privilege Level Confirmation",
                ("Are you sure you want to change the privilege level of this"
                 " user?")
            )

        # TODO: Connect to user management to actually change the privilege of the user.
        if response:
            print("Change privilege")
            messagebox.showinfo(
                "Change succcessful!",
                "The privilege level of the user has been changed!")
            self.user_management.change_user_privilege(self.user_id,
                                                       new_privilege)

            if new_privilege == 0:
                self.privilege_option_menu.configure(state=tk.DISABLED)
                self.change_privilege_button["state"] = tk.DISABLED
