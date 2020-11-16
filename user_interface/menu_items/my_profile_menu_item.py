import tkinter as tk
from user_interface.active_windows import my_profile_window
from user_interface.menu_items import menu_item

class MyProfileMenuItem(menu_item.MenuItem):
    def __init__(self, main_menu):
        menu_item.MenuItem.__init__(self, main_menu)

        self.create_button()

    def create_button(self):
        self.button = tk.Button(self.frame, text="MyProfile")
        self.button["command"] = self.get_my_profile_window

        self.button.pack()

    def get_my_profile_window(self):
        self.gui.active_window.hide()

        self.associated_window = my_profile_window.MyProfileWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()