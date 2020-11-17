import tkinter as tk
from user_interface.active_windows import assigned_challenges_window
from user_interface.menu_items import menu_item

class AssignedChallengesMenuItem(menu_item.MenuItem):
    """This class is used to create a button that will bring the user to the assigned challenges menu.
    """
    def __init__(self, main_menu, frame):
        """
        Args:
            main_menu ([]): this class must know about the main menu because it knows about the GUI, and we need to alter the GUI's active window
        """
        menu_item.MenuItem.__init__(self, main_menu, frame)

        self.create_button()

    def create_button(self):
        """Create the Assigned Challenges button
        """
        self.button = tk.Button(self.frame, text="Assigned Challenges")
        self.button["command"] = self.get_assigned_challenges_window

        self.button.grid(row=0, column=0)

    def get_assigned_challenges_window(self):
        """This function will hide everything on the active window and display the assigned challenges window
        """

        
        self.gui.active_window.hide()

        self.associated_window = assigned_challenges_window.AssignedChallengesWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()