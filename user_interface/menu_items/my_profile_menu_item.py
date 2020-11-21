import tkinter as tk
from user_interface.active_windows import my_profile_window
from user_interface.menu_items import menu_item

class MyProfileMenuItem(menu_item.MenuItem):
    """This class is used to create a button that will bring the user to the my profile menu.
    """
    def __init__(self, main_menu, frame):
        """
        Args:
            main_menu ([]): this class must know about the main menu because it knows about the GUI, and we need to alter the GUI's active window
        """
        menu_item.MenuItem.__init__(self, main_menu, frame)

        self.create_menu_item_button("My Profile")
        self.menu_item_button["command"] = self.get_my_profile_window

    def get_my_profile_window(self):
        """This function will hide everything on the active window and display the profile window
        """
        self.gui.active_window.hide()

        self.associated_window = my_profile_window.MyProfileWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()