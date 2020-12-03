from gui_authentication import login
from gui_authentication import signup
from gui_authentication import create_school


def run_login_screen(master):
    login.Authentication(master).mainloop()

def run_signup_screen(master):
    signup.CreateUser(master).mainloop()

def run_create_school(master):
    create_school.CreateSchool(master).mainloop()




