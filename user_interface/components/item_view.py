import tkinter as tk
from user_interface.components import header
from user_interface.components.styles import Styles
from user_interface.active_windows import active_window

class ItemView(active_window.ActiveWindow):

    def __init(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

    def set_data(self, item, title_text):
        self.item = item
        self.header = header.Header(self.frame, title_text)
