import tkinter as tk

# //TODO cleanup import statements (if possible)

from user_interface.menu_items import assigned_challenges_menu_item

from user_interface.menu_items import new_challenge_menu_item
from user_interface.menu_items import my_history_menu_item

from user_interface.menu_items import school_management_menu_item
from user_interface.menu_items import classroom_management_menu_item
from user_interface.menu_items import user_management_menu_item
from user_interface.menu_items import reports_menu_item

from user_interface.menu_items import home_menu_item
from user_interface.menu_items import my_profile_menu_item
from user_interface.menu_items import help_menu_item

class MainMenu(object):
    """MainMenu class creates a mainmenu on the left of the screen.

    This class holds all attributes and methods needed to create a main menu. Main menu will be used to give the user buttons that they can use to switch
    between different menus
    """
    def __init__(self, privilege, gui):
        """MainMenu init

        Args:
            privilege ([type]): privilege level of the user, obtained from the context_service.
                                Needed in order to display the correct buttons that correspond to the user type

            gui ([GUI]): the gui is needed in order to display the main menu on the GUI's frame
        """
        self.gui = gui
        self.master = gui.master

        # The frame containing main menu
        self.frame = tk.LabelFrame(self.master)

        
        self.frame_top = tk.LabelFrame(self.frame)
        self.frame_bottom = tk.LabelFrame(self.frame)

        self.frame_top.grid(row=1, column=1)
        self.frame_bottom.grid(row=2, column=1)

        self.make_common_menu_items()
        self.create_standard_panel()



    def make_common_menu_items(self):

        self.new_challenge_menu_item = new_challenge_menu_item.NewChallengeMenuItem(self, self.frame_top)

        self.home_menu_item = home_menu_item.HomeMenuItem(self, self.frame_bottom)

    def create_standard_panel(self):
        """This function is used to create the items that are displayed on a standard user's main menu
        """
        #newchallenge, assigned challenges, myhistory
        self.new_challenge_menu_item.place_on_menu(0, 1)

        self.home_menu_item.place_on_menu(1, 1)

        self.my_profile_menu_item = my_profile_menu_item.MyProfileMenuItem(self, self.frame_top)
        self.my_profile_menu_item.place_on_menu(2, 1)

        
        


    # //TODO Create the admin panel
    def create_admin_panel(self):
        """This function is used to create the items that are displayed on a admin's main menu
        """
        #classroom, user, report, newchallenge, myhistory
        
    # //TODO Create the super admin panel
    def create_super_admin_panel(self):
        """This function is used to create the items that are displayed on a super admin's main menu
        """
        #School, classroom, user, report, newchallenge, my history
        pass

    # //TODO Create bottom panel
    # Profile, help, home



