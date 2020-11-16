import tkinter as tk
import new_challenge_window
import menu_item

class NewChallengeMenuItem(menu_item.MenuItem):
    def __init__(self, main_menu):
        menu_item.MenuItem.__init__(self, main_menu)

        self.create_button()

    def create_button(self):
        self.button = tk.Button(self.frame, text="New Challenge")
        self.button["command"] = self.get_new_challenge_window

        self.button.pack()

    def get_new_challenge_window(self):
        self.gui.active_window.hide()

        self.associated_window = new_challenge_window.NewChallengeWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()