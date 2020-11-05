import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.school_label = tk.Label(self.master, text="School").grid(row=0)
        self.email_label = tk.Label(self.master, text="Email").grid(row=2)
        self.password_label = tk.Label(self.master, text="Password").grid(row=4)

        school_entry = tk.Entry(self.master)
        email_entry = tk.Entry(self.master)
        password_entry = tk.Entry(self.master)

        school_entry.grid(row=1)
        email_entry.grid(row=3)
        password_entry.grid(row=5)

        sign_in = tk.Button(self.master, text="Sign In", fg="white", bg="blue")
        sign_in["command"] = self.sign_in
        sign_in.grid(row=6)


        new_user_label = tk.Label(self.master, text="New User").grid(row=8)
        sign_up = tk.Button(self.master, text="Sign Up", fg="white", bg="blue")
        sign_up["command"] = self.sign_up
        sign_up.grid(row=9)

    def sign_in(self):
        print("Sign In")


    def sign_up(self):
        print("Sign Up")


root = tk.Tk()
app = Application(master=root)
app.mainloop()