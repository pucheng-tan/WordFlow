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

        self.create_button()

    def create_button(self):
        """Creates and places the button for the home menu item."""

        self.button = tk.Button(self.frame, text="Home", font=("Helvetica", 15))
        self.button["command"] = self.get_home_window

        self.button.pack(fill=tk.X)

    def get_home_window(self):
        """This function will hide everything on the active window and display the home window
        """
        self.gui.active_window.hide()

        self.associated_window = home_window.HomeWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()