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

        # The main menu frame
        self.frame = tk.LabelFrame(self.master, height=1000)

        self.frame_top = tk.LabelFrame(self.frame)
        # self.frame_middle = tk.LabelFrame(self.frame)
        self.frame_bottom = tk.LabelFrame(self.frame)
        self.frame_top.pack(side=tk.TOP, fill=tk.X)
        self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)

        self.make_common_menu_items()

        self.create_bottom_panel()

        if privilege == "Standard":
            self.make_standard_menu_items()
            self.create_standard_panel()

    def place_main_menu(self):

        # self.master.grid_rowconfigure(0, weight=1)
        # self.master.grid_rowconfigure(2, weight=1)
        # self.master.grid_columnconfigure(1, weight=1)

        # self.frame.grid(row=0, column=0, sticky="ns") # Display the main menu on the left of the screen
        # tk.LabelFrame(text="Test").grid(row=1, column=0)

        # self.frame.grid_rowconfigure(1, weight=2)
        # self.frame.grid_rowconfigure(2, weight=1)
        # self.frame_top.grid(row=1, column=0, sticky=tk.N)
        # self.frame_middle.grid(row=1, column=0, rowspan=2)
        # elf.frame_bottom.grid(row=3, column=0, sticky=tk.S)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

    def make_common_menu_items(self):

        self.new_challenge_menu_item = new_challenge_menu_item.NewChallengeMenuItem(self, self.frame_top)

        self.home_menu_item = home_menu_item.HomeMenuItem(self, self.frame_bottom)
        self.my_profile_menu_item = my_profile_menu_item.MyProfileMenuItem(self, self.frame_bottom)
        self.help_menu_item = help_menu_item.HelpMenuItem(self, self.frame_bottom)

    def create_bottom_panel(self):
        self.home_menu_item.place_on_menu(0, 1)
        self.my_profile_menu_item.place_on_menu(1, 1)

    def make_standard_menu_items(self):

        self.assigned_challenges_menu_item = assigned_challenges_menu_item.AssignedChallengesMenuItem(self, self.frame_top)


    def create_standard_panel(self):
        """This function is used to create the items that are displayed on a standard user's main menu
        """
        # Assigned Challenges, New Challenge, My History

        self.assigned_challenges_menu_item.place_on_menu(0, 1)
        self.new_challenge_menu_item.place_on_menu(1, 1)


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



