"""Runs different screens for the GUI and authentication.

Typical Usage Example:
    screen_handler.run_login_screen()
"""

from GUI_Authentication import login
from GUI_Authentication import signup
from GUI_Authentication import create_school


def run_login_screen(master):
    """Runs the login screen.

    Args:
        master: The master of the login frame.
    """
    login.Authentication(master).mainloop()


def run_signup_screen(master):
    """Runs the signup screen.

    Args:
        master: The master of the signup frame.
    """
    signup.CreateUser(master).mainloop()


def run_create_school(master):
    """Runs the create school screen.

    Args:
        master: The master of the create school frame.
    """
    create_school.CreateSchool(master).mainloop()
