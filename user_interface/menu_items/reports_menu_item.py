import tkinter as tk
from user_interface.active_windows import reports_window
from user_interface.menu_items import menu_item

class ReportsMenuItem(menu_item.MenuItem):
    def __init__(self, main_menu):
        menu_item.MenuItem.__init__(self, main_menu)

        self.create_button()

    def create_button(self):
        self.button = tk.Button(self.frame, text="Reports")
        self.button["command"] = self.get_reports_window

        self.button.pack()

    def get_reports_window(self):
        self.gui.active_window.hide()

        self.associated_window = reports_window.ReportsWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()