from gui_authentication import login
from gui_authentication import signup
from gui_authentication import create_school

class ScreenHandler(object):
    def __init__(self):
        pass

def run_login_screen(master):
    """Runs the login screen.

    Args:
        master: The master of the login screen.
    """
    login.Authentication(master).mainloop()

def run_signup_screen(master):
    """Runs the signup screen.

    Args:
        master: The master of the signup screen.
    """
    signup.CreateUser(master).mainloop()

def run_create_school(master):
    """
    Runs the create school screen.

    Args:
        master: The master of the create school screen.
    """
    create_school.CreateSchool(master).mainloop()
