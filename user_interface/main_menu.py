import tkinter as tk

#import menu_items.new_challenge_menu_item

from user_interface.menu_items import new_challenge_menu_item
from user_interface.menu_items import home_menu_item
from user_interface.menu_items import my_profile_menu_item

class MainMenu(object):
    def __init__(self, privilege, gui):
        self.gui = gui
        self.master = gui.master

        self.frame = tk.LabelFrame()

        self.create_standard_panel()

    def create_standard_panel(self):

        self.new_challenge_menu_item = new_challenge_menu_item.NewChallengeMenuItem(self)
        self.new_challenge_menu_item.place_on_menu(2, 3)

        self.home_menu_item = home_menu_item.HomeMenuItem(self)
        self.home_menu_item.place_on_menu(1, 2)

        self.my_profile_menu_item = my_profile_menu_item.MyProfileMenuItem(self)
        self.my_profile_menu_item.place_on_menu(1, 2)

    def create_admin_panel(self):
        pass

    def create_super_admin_panel(self):
        pass