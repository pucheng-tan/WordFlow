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

    def create_menu_item_button(self, button_text):
        """Creates and places a button on the menu item.
        Args:
            button_text: The text that should be on the button of the menu item.
        """
        self.menu_item_button = tk.Button(self.frame, text=button_text)
        self.menu_item_button["font"] = ("Helvetica", 15)

        self.menu_item_button.pack(fill=tk.X)