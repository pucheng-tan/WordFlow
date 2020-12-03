import tkinter as tk
from user_interface.components.styles import Styles

class Header():

    TITLE_FONT = ("Helvetica", 25, "bold")    

    def __init__(self, parent_frame, title_text):
        self.heading_frame = tk.Frame(parent_frame)
        self.heading_frame.pack(side=tk.TOP, fill=tk.X)
        title_label = tk.Label(self.heading_frame, text=title_text)
        title_label["font"] = Header.TITLE_FONT
        title_label.pack(side=tk.LEFT, padx=Styles.PADX, pady=Styles.PADY)