import tkinter as tk
# import login

class SignUp(tk.Frame):
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
        self.first_line = tk.Canvas(self.frame, height=10, width=200)
        self.first_line.create_rectangle(1, 5, 200, 10, fill="light blue", outline="light blue")

        self.first_line.grid(row=2)

    def create_labels(self):
        # Permanent labels
        self.new_user_label = tk.Label(self.frame, text="New User")

        self.school_label = tk.Label(self.frame, text="School")
        self.email_label = tk.Label(self.frame, text="Email")
        self.invite_code_label = tk.Label(self.frame, text="Invite Code")
        self.password_label = tk.Label(self.frame, text="Password")
        self.verify_password_label = tk.Label(self.frame, text="Verify Password")

        # Temporary labels
        self.forget_label = tk.Label(self.frame, text="You are missing a field!", fg="red")

        self.new_user_label.grid(row=1)

        self.school_label.grid(row=3)
        self.email_label.grid(row=5)
        self.invite_code_label.grid(row=7)
        self.password_label.grid(row=9)
        self.verify_password_label.grid(row=11)

    def create_entries(self):

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
        self.existing_account_label = tk.Label(self.frame, text="Sign in to existing account", fg="blue")
        self.existing_account_label.configure(font="Verdana 9 underline")

        self.existing_account_label.grid(row=15)
        self.existing_account_label.bind("<Button>", self.existing_account)

    def existing_account(self, event):
        # self.master.destroy()
        new_root = tk.Tk()
        # login.Login(self.master).mainloop()

    def create_buttons(self):

        sign_in = tk.Button(self.frame, text="Create Account", fg="white", bg="blue")
        sign_in["command"] = self.create_account
        sign_in.grid(row=13, padx=10, pady=10)


    def create_account(self):
        school = self.school_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not school or not email or not password:
            self.forget_label.grid(row=14)
        else:
            self.forget_label.grid_forget()
            print(school, email, password)

# print("Sign Up")
# root = tk.Tk()
# app = SignUp(master=root)
# app.mainloop()