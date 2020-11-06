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
        self.password_label = tk.Label(self.master, text="Password").grid(row=4)
        self.new_user_label = tk.Label(self.master, text="New User")

        # Temporary labels
        self.forget_label = tk.Label(self.master, text="You are missing a field!", fg="red")

        self.new_user_label.grid(row=8)

    def create_entries(self):

        self.school_entry = tk.Entry(self.master)
        self.email_entry = tk.Entry(self.master)
        self.password_entry = tk.Entry(self.master)

        self.school_entry.grid(row=1, padx=10, pady=10)
        self.email_entry.grid(row=3)
        self.password_entry.grid(row=5)

    def create_buttons(self):

        sign_in = tk.Button(self.master, text="Sign In", fg="white", bg="blue")
        sign_in["command"] = self.sign_in
        sign_in.grid(row=6, padx=10, pady=10)


        sign_up = tk.Button(self.master, text="Sign Up", fg="white", bg="blue")
        sign_up["command"] = self.sign_up
        sign_up.grid(row=9, padx=10, pady=10)

    def sign_in(self):
        school = self.school_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not school or not email or not password:
            self.forget_label.grid(row=7)
        else:
            self.forget_label.grid_forget()
            print(school, email, password)


    def sign_up(self):
        print("Sign Up")


root = tk.Tk()
app = Application(master=root)
app.mainloop()