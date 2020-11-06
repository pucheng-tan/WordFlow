import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Welcome")

        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        # Permanent labels
        self.school_label = tk.Label(self.master, text="School").grid(row=0)
        self.email_label = tk.Label(self.master, text="Email").grid(row=2)
        self.invite_code_label = tk.Label(self.master, text="Invite Code").grid(row=4)
        self.password_label = tk.Label(self.master, text="Password").grid(row=6)
        self.verify_password_label = tk.Label(self.master, text="Verify Password")

        # Temporary labels
        self.forget_label = tk.Label(self.master, text="You are missing a field!", fg="red")

        self.verify_password_label.grid(row=8)

    def create_entries(self):

        self.school_entry = tk.Entry(self.master)
        self.email_entry = tk.Entry(self.master)
        self.invite_code_entry = tk.Entry(self.master)
        self.password_entry = tk.Entry(self.master)
        self.verify_password_entry = tk.Entry(self.master)


        self.school_entry.grid(row=1, padx=10, pady=10)
        self.email_entry.grid(row=3)
        self.invite_code_entry.grid(row=5)
        self.password_entry.grid(row=7)
        self.verify_password_entry.grid(row=9)

    def create_buttons(self):

        sign_in = tk.Button(self.master, text="Create Account", fg="white", bg="blue")
        sign_in["command"] = self.create_account
        sign_in.grid(row=10, padx=10, pady=10)


    def create_account(self):
        school = self.school_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not school or not email or not password:
            self.forget_label.grid(row=11)
        else:
            self.forget_label.grid_forget()
            print(school, email, password)


root = tk.Tk()
app = Application(master=root)
app.mainloop()