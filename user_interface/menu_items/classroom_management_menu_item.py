import tkinter as tk
from user_interface.active_windows import classroom_management_window
from user_interface.menu_items import menu_item

class Classroom_Management_MenuItem(menu_item.MenuItem):
    """This class is used to create a button that will bring the user to the classroom management menu.
    """
    def __init__(self, main_menu, frame):
        """
        Args:
            main_menu ([]): this class must know about the main menu because it knows about the GUI, and we need to alter the GUI's active window
        """
        menu_item.MenuItem.__init__(self, main_menu, frame)

        self.create_button()

    def create_button(self):
        self.button = tk.Button(self.frame, text="Classroom Management")
        self.button["command"] = self.get_classroom_challenge_window

        self.button.pack()

    def get_classroom_challenge_window(self):
        """This function will hide everything on the active window and display the classroom management window
        """
        self.gui.active_window.hide()

        self.associated_window = classroom_management_window.ClassroomManagementWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()