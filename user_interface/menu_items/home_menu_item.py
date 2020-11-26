import tkinter as tk
# from ..active_windows import home_window
from user_interface.active_windows import home_window
from user_interface.menu_items import menu_item

class HomeMenuItem(menu_item.MenuItem):
    """This class is used to create a button that will bring the user to the Home menu.
    """
    def __init__(self, main_menu, frame):
        menu_item.MenuItem.__init__(self, main_menu, frame)
        """
        Args:
            main_menu ([]): this class must know about the main menu because it knows about the GUI, and we need to alter the GUI's active window
        """

        self.create_menu_item_button("Home")
        self.menu_item_button["command"] = self.get_home_window

    def get_home_window(self):
        """This function will hide everything on the active window and display the home window
        """
        self.gui.active_window.hide()

        self.associated_window = home_window.HomeWindow(self.gui)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()