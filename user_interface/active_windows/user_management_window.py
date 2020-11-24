import tkinter as tk
from tkinter import ttk
from user_interface.active_windows import active_window



class UserManagementWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # // TODO Make the User Management Window
        # The two lines below can be removed once the window is being made

        self.first_frame = tk.Frame(self.frame)
        self.first_frame.pack(fill=tk.X, pady=20)

        self.create_labels()
        self.create_buttons()
        self.create_user_management_notebook()
        self.get_users()

    def show(self):
        self.frame.pack(expand=True, fill=tk.BOTH)

    def create_labels(self):
        label = tk.Label(self.first_frame, text="User Management", font=("Helvetica", 20, "bold"))
        label.pack(side=tk.LEFT)

    def create_buttons(self):
        new_user_button = tk.Button(self.first_frame, text="New User", fg="white", bg="blue")
        invite_all_button = tk.Button(self.first_frame, text="Invite All", fg="white", bg="blue")

        new_user_button["font"] = ("Helvetica", 20)
        invite_all_button["font"] = ("Helvetica", 20)

        new_user_button.pack(side=tk.RIGHT, padx=20)
        invite_all_button.pack(side=tk.RIGHT)

    def create_user_management_notebook(self):
        self.user_management_notebook = ttk.Notebook(self.frame)
        self.user_management_notebook.pack(expand=True, fill=tk.BOTH)

        self.create_standard_frame()
        self.create_admin_frame()
        self.create_super_admin_frame()
        self.create_tabs()

    def create_standard_frame(self):
        self.standard_frame = tk.Frame(self.user_management_notebook, bg="green")
        self.standard_frame.pack()

    def create_admin_frame(self):
        self.admin_frame = tk.Frame(self.user_management_notebook, bg="blue")
        self.admin_frame.pack()

    def create_super_admin_frame(self):
        self.super_admin_frame = tk.Frame(self.user_management_notebook, bg="red")
        self.super_admin_frame.pack()

    def get_users(self):
        users = ["Name", "One", "Two", "Three"]
        emails = ["Email", "Email 1", "Email 2", "Email 3"]
        self.my_listbox = tk.Listbox(self.standard_frame, font=("Helvetica", 20))
        self.my_listbox.pack(side=tk.LEFT)
        self.my_listbox.bind('<<ListboxSelect>>', self.activate)

        self.my_email_listbox = tk.Listbox(self.standard_frame, font=("Helvetica", 20))
        self.my_email_listbox.pack(side=tk.LEFT)

        for item in range(0, len(users)):
            self.my_listbox.insert("end", users[item])
            self.my_email_listbox.insert("end", emails[item])
            if item == 0:
                self.my_listbox.itemconfig(item, fg="white", bg="blue")
                self.my_email_listbox.itemconfig(item, fg="white", bg="blue")
            if item % 2 != 0:
                self.my_listbox.itemconfig(item, bg="light gray")
                self.my_email_listbox.itemconfig(item, bg="light gray")

        tk.Label(self.standard_frame, text="Actions").pack(side=tk.RIGHT)

    def activate(self, event):
        print(self.my_listbox.index(tk.ANCHOR))

    def create_tabs(self):
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=("Helvetica", "20", "bold"))

        self.user_management_notebook.add(self.standard_frame, text="Standard")
        self.user_management_notebook.add(self.admin_frame, text="Admin")
        self.user_management_notebook.add(self.super_admin_frame, text="Super-Admin")

        self.user_management_notebook.bind("<<NotebookTabChanged>>", self.hello)

    def hello(self, event):
        print("Hello World!")