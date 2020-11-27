import tkinter as tk
from user_interface.active_windows import reports_window
from user_interface.menu_items import menu_item

class ReportsMenuItem(menu_item.MenuItem):
    """This class is used to create a button that will bring the user to the reports menu.
    """
    def __init__(self, main_menu, frame):
        """
        Args:
            main_menu ([]): this class must know about the main menu because it knows about the GUI, and we need to alter the GUI's active window
        """
        menu_item.MenuItem.__init__(self, main_menu, frame)

        self.create_menu_item_button("Reports")
        self.menu_item_button["command"] = self.get_reports_window

    def get_reports_window(self):
        """This function will hide everything on the active window and display the reports window
        """
        self.gui.active_window.hide()

        self.associated_window = reports_window.ReportsWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()