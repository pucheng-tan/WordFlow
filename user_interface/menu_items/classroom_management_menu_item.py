import tkinter as tk
from user_interface.active_windows import classroom_management_window
from user_interface.menu_items import menu_item

class Classroom_Management_MenuItem(menu_item.MenuItem):
    def __init__(self, main_menu):
        menu_item.MenuItem.__init__(self, main_menu)

        self.create_button()

    def create_button(self):
        self.button = tk.Button(self.frame, text="Classroom Management")
        self.button["command"] = self.get_classroom_challenge_window

        self.button.pack()

    def get_classroom_challenge_window(self):
        self.gui.active_window.hide()

        self.associated_window = classroom_management_window.ClassroomManagementWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()