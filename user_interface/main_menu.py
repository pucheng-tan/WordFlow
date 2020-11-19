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
    """MainMenu class creates a main menu.

    This class holds all attributes and methods needed to create a main menu.
    Main menu will be used to give the user menu items that they can use to
    switch between different active windows.
    """
    def __init__(self, privilege, gui):
        """MainMenu init

        Args:
            privilege ([type]): privilege level of the user, obtained from the context_service.
                                Needed in order to display the correct menu items that correspond to the user type

            gui ([GUI]): the gui is needed in order to display the main menu on the GUI's frame
        """
        self.gui = gui
        self.master = gui.master

        # The main menu frame
        self.frame = tk.LabelFrame(self.master, height=1000)

        # Make and place the top and bottom frames on the main menu frame
        self.frame_top = tk.LabelFrame(self.frame)
        self.frame_bottom = tk.LabelFrame(self.frame)
        self.frame_top.pack(side=tk.TOP, fill=tk.X)
        self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)

        self.create_main_menu(privilege)

    def create_main_menu(self, privilege):
        """Creates the main menu for the GUI frame.

        Makes the menu items and then places the menu items on the main menu.

        Args:
            privilege: The level of privilege of the user.
        """

        self.create_common_menu_items()

        if privilege == 2:
            self.create_standard_menu_items()
            self.create_standard_panel()
        elif privilege == 0:
            self.create_super_admin_menu_items()
            self.create_super_admin_panel()

        self.create_bottom_panel()

    def place_main_menu(self):
        """Places the main menu on the left side of the GUI frame."""

        # Display the main menu on the left of the screen
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

    def create_common_menu_items(self):
        """Makes all the menu items that all the main menus for the different
        users have."""

        self.new_challenge_menu_item = new_challenge_menu_item.NewChallengeMenuItem(self, self.frame_top)
        self.my_history_menu_item = my_history_menu_item.MyHistoryMenuItem(self, self.frame_top)

        self.home_menu_item = home_menu_item.HomeMenuItem(self, self.frame_bottom)
        self.my_profile_menu_item = my_profile_menu_item.MyProfileMenuItem(self, self.frame_bottom)
        self.help_menu_item = help_menu_item.HelpMenuItem(self, self.frame_bottom)

    def create_standard_menu_items(self):
        """Makes the menu items that only standard users have on their main
        menus."""

        self.assigned_challenges_menu_item = assigned_challenges_menu_item.AssignedChallengesMenuItem(self, self.frame_top)

    def create_super_admin_menu_items(self):
        """Makes the menu items that only super-administrative users have on
        their main menus."""

        self.school_management_menu_item = school_management_menu_item.SchoolManagementMenuItem(self, self.frame_top)
        self.classroom_management_menu_item = classroom_management_menu_item.ClassroomManagementMenuItem(self, self.frame_top)
        self.user_management_menu_item = user_management_menu_item.UserManagementMenuItem(self, self.frame_top)
        self.reports_menu_item = reports_menu_item.ReportsMenuItem(self, self.frame_top)

    def create_standard_panel(self):
        """This function is used to create the top frame that is displayed on a standard user's main menu.
        """
        # Assigned Challenges, New Challenge, My History
        self.assigned_challenges_menu_item.place_on_menu()
        self.new_challenge_menu_item.place_on_menu()
        self.my_history_menu_item.place_on_menu()

    # //TODO Create the admin panel
    def create_admin_panel(self):
        """This function is used to create the top frame that is displayed on an admin's main menu.
        """
        # School Management, Classroom Management, User Management, Reports, New Challenge, My History

    def create_super_admin_panel(self):
        """This function is used to create the top frame that is displayed on a super admin's main menu.
        """
        # School Management, Classroom Management, User Management, Reports, New Challenge, My History
        self.school_management_menu_item.place_on_menu()
        self.classroom_management_menu_item.place_on_menu()
        self.user_management_menu_item.place_on_menu()
        self.reports_menu_item.place_on_menu()

        self.new_challenge_menu_item.place_on_menu()
        self.my_history_menu_item.place_on_menu()

    def create_bottom_panel(self):
        """This function is used the create the bottom frame for the main
        menu of all the users."""

        # Home, My Profile, Menu
        self.home_menu_item.place_on_menu()
        self.my_profile_menu_item.place_on_menu()
        self.help_menu_item.place_on_menu()




