import tkinter as tk

class MenuItem(object):
    """MenuItem is the super class for all menu items.

    MenuItem also provides each menu item with 'place_on_menu' which allows each item to be placed on the menu.

    """
    def __init__(self, main_menu):
        self.gui = main_menu.gui
        self.main_menu = main_menu

        self.frame = self.main_menu.frame

    def place_on_menu(self, row, column):
        """Place the item on the menu at the specified row and column.

        Args:
            row ([int]): row number to place menu item at
            column ([int]): column number to place menu item at
        """
        self.main_menu.frame.grid(row=row, column=column)