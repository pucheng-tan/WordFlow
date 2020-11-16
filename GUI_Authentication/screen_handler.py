from GUI_Authentication import login
from GUI_Authentication import signup
from GUI_Authentication import create_school

class ScreenHandler(object):
    def __init__(self):
        pass

    def run_login_screen(self, master):
        login.Authentication(master).mainloop()

    def run_signup_screen(self, master):
        signup.CreateUser(master).mainloop()

    def run_create_school(self, master):
        create_school.CreateSchool(master).mainloop()




