import tkinter as tk

from user_interface import main_menu
from user_interface.active_windows import home_window

#THE PURPOSE OF TEST GUI IS A GUI THAT DOES NOT DEPEND ON THE LOGIN SCREEN -> PERFECT FOR MAKING QUICK ADJUSTMENTS TO THE GUI

#This is just a mock context service that I can use to give test gui dummy values - we can use the same gui as the real one, without changing the code
class ContextServiceTest(object):
    def get_instance(self):
        return self
    def get_user_privilege(self):
        return 2
    def get_user_email(self):
        return "1123@gmail.com"

    def get_school_id(self):
        return "3p1U6xAvKic1RvXMl5nJ"

    def get_user_uid(self):
        return "T1b5iP7q96YBnaPDRuEN8c5Arwh1"

class TESTGUI(object):
    """GUI class will create a main menu and an active window, which together will make up the GUI.

    In order to run the GUI, you can run this class.
    """
    def __init__(self, master):
        """GUI init

        Args:
            privilege ([type]): privilege level of the user, obtained from the context_service.
                                Needed in order to display the correct buttons that correspond to the user type

            master ([tkinter window]): master is the tkinter window which we want to display the GUI on.
        """

        self.master = master

        
        self.context_service = ContextServiceTest()

        # self.master.state("zoomed")
        # self.master.resizable(False, False)

        # Create a main menu


        self.main_menu = main_menu.MainMenu(self.context_service.get_user_privilege(), self)
        #Just took this line out so I could test

        # Create an active window (currently, the active window will display the
        # home window, since it is the first window viewed when logging in
        self.active_window = home_window.HomeWindow(self)

        # Display the main menu
        self.main_menu.show_main_menu()
        # Display the active window
        self.active_window.show()

