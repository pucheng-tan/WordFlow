import tkinter as tk
from user_interface.active_windows import user_management_window
from user_interface.menu_items import menu_item

class UserManagementMenuItem(menu_item.MenuItem):
    """This class is used to create a button that will bring the user to the user management menu.
    """
    def __init__(self, main_menu, frame):
        """
        Args:
            main_menu ([]): this class must know about the main menu because it knows about the GUI, and we need to alter the GUI's active window
        """
        menu_item.MenuItem.__init__(self, main_menu, frame)

        self.create_menu_item_button("User Management")
        self.menu_item_button["command"] = self.get_user_management_window

    def get_user_management_window(self):
        """This function will hide everything on the active window and display the user management window
        """
        self.gui.active_window.hide()

        self.associated_window = user_management_window.UserManagementWindow(self.gui)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()