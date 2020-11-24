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

        # Create a tree Frame with scroll bar
        self.tree_view_frame = tk.Frame(self.standard_frame)
        self.tree_scroll = tk.Scrollbar(self.tree_view_frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        mytree = ttk.Treeview(self.tree_view_frame, yscrollcommand=self.tree_scroll.set, selectmode="browse")

        self.tree_scroll.config(command=mytree.yview)
        self.tree_view_frame.pack()
        mytree.pack()
        mytree["columns"] = ("Name", "Email", "Date Created", "Last Sign In")
        # FOrmatting Colums
        mytree.column("#0", width=0, stretch=tk.NO)
        mytree.column("Name", anchor=tk.CENTER)
        mytree.column("Email", anchor=tk.W)
        mytree.column("Date Created", anchor=tk.CENTER)
        mytree.column("Last Sign In", anchor=tk.CENTER)

        # Creating Headings
        mytree.heading("#0", text="", anchor=tk.W)
        mytree.heading("Name", text="Name", anchor=tk.CENTER)
        mytree.heading("Email", text="Email", anchor=tk.W)
        mytree.heading("Date Created", text="Date Created", anchor=tk.CENTER)
        mytree.heading("Last Sign In", text="Last Sign In", anchor=tk.CENTER)
        
        # Fake Data
        count = 0
        for i in range(0,25):
            if i % 2 == 0:
                mytree.insert(parent="", index="end", iid=count, text="", values=("FAke Name", "fakename@hotmail.com", 12, 18))
            else:
                mytree.insert(parent="", index="end", iid=count, text="", values=("Real Name", "realname@hotmail.com", 10, 20), tags=("odd",))
                
            count+= 1
        
        # Should be working but....
        mytree.tag_configure("odd", background="light gray")
        


    def create_tabs(self):
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=("Helvetica", "20", "bold"))

        self.user_management_notebook.add(self.standard_frame, text="Standard")
        self.user_management_notebook.add(self.admin_frame, text="Admin")
        self.user_management_notebook.add(self.super_admin_frame, text="Super-Admin")

        self.user_management_notebook.bind("<<NotebookTabChanged>>", self.hello)

    def hello(self, event):
        print("Hello World!")