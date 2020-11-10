import tkinter as tk
import login

class CreateSchool(tk.Frame):
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
        self.create_clickable_labels()
        self.create_entries()
        self.create_buttons()

    def create_borders(self):
        self.first_line = tk.Canvas(self.frame, height=10, width=200)
        self.first_line.create_rectangle(1, 5, 200, 10, fill="light blue", outline="light blue")

        self.first_line.grid(row=2)

    def create_labels(self):
        # Create permanent labels
        self.new_school_label = tk.Label(self.frame, text="New School")

        self.school_label = tk.Label(self.frame, text="School")
        self.email_label = tk.Label(self.frame, text="Email")
        self.password_label = tk.Label(self.frame, text="Password")
        self.verify_password_label = tk.Label(self.frame, text="Verify Password")

        # Create temporary labels
        self.forget_label = tk.Label(self.frame, text="You are missing a field!", fg="red")

        # Place Permanent labels into their positions
        self.new_school_label.grid(row=1)

        self.school_label.grid(row=3)
        self.email_label.grid(row=5)
        self.password_label.grid(row=7)
        self.verify_password_label.grid(row=9)

    def create_entries(self):

        self.school_entry = tk.Entry(self.frame)
        self.email_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame)
        self.verify_password_entry = tk.Entry(self.frame)

        self.school_entry.grid(row=4, padx=10, pady=5)
        self.email_entry.grid(row=6)
        self.password_entry.grid(row=8)
        self.verify_password_entry.grid(row=10)

    def create_clickable_labels(self):

        self.create_school_label = tk.Label(self.frame, text="Sign in to existing account", fg="blue")
        self.create_school_label.configure(font="Verdana 9 underline")

        self.create_school_label.grid(row=13)
        self.create_school_label.bind("<Button>", self.existing_account)

    def existing_account(self, event):
        self.master.destroy()
        new_root = tk.Tk()
        login.Authentication(new_root).mainloop()

    def create_buttons(self):

        sign_in = tk.Button(self.frame, text="Create School", fg="white", bg="blue")
        sign_in["command"] = self.create_school
        sign_in.grid(row=11, padx=11, pady=10)

    def create_school(self):
        school = self.school_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not school or not email or not password:
            self.forget_label.grid(row=12)
        else:
            self.forget_label.grid_forget()
            print(school, email, password)

# root = tk.Tk()
# app = CreateSchool(master=root)
# app.mainloop()