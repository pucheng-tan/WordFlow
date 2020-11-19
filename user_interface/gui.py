import tkinter as tk

from user_interface import main_menu
from user_interface.active_windows import home_window

from services import context_service

class GUI(object):
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
        self.context_service = context_service.ContextService.get_instance()
        print(self.context_service.get_user_privilege())

        # self.master.state("zoomed")
        # self.master.resizable(False, False)

        self.main_menu = main_menu.MainMenu(self.context_service.get_user_privilege(), self)  # Create a main menu
        self.active_window = home_window.HomeWindow(self)  # Create an active window (currently, the active window will dispay the home window)

        self.main_menu.place_main_menu() # Display the main menu on the left of the screen

        self.active_window.show() # show the active window

# root = tk.Tk()

# GUI("Standard", root)

# root.mainloop()