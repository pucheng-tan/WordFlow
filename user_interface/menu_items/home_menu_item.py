import tkinter as tk
import home_window
import menu_item

class HomeMenuItem(menu_item.MenuItem):
    def __init__(self, main_menu):
        menu_item.MenuItem.__init__(self, main_menu)

        self.create_button()

    def create_button(self):
        self.button = tk.Button(self.frame, text="Home")
        self.button["command"] = self.get_home_window

        self.button.pack()

    def get_home_window(self):
        self.gui.active_window.hide()

        self.associated_window = home_window.HomeWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()