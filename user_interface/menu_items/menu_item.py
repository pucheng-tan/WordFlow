import tkinter as tk

class MenuItem(object):
    """MenuItem is the super class for all menu items.

    MenuItem also provides each menu item with 'place_on_menu' which allows each item to be placed on the menu.

    """
    def __init__(self, main_menu, frame):
        self.gui = main_menu.gui
        self.main_menu = main_menu

        self.frame = tk.Frame(frame)

    def place_on_menu(self):
        """Place the item on the menu at the specified row and column.

        Args:
            row ([int]): row number to place menu item at
            column ([int]): column number to place menu item at
        """
        self.frame.pack(fill=tk.X)