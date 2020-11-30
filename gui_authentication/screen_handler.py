from gui_authentication import login
from gui_authentication import signup
from gui_authentication import create_school


def run_login_screen(self, master):
    login.Authentication(master).mainloop()

def run_signup_screen(self, master):
    signup.CreateUser(master).mainloop()

def run_create_school(self, master):
    create_school.CreateSchool(master).mainloop()




