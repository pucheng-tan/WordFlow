from BaseWindow import baseWindow
from tkinter import *


class profileMenu(baseWindow):
    """This is the module for the main menu window
    """
    def __init__(self, master, priviledge="user"):
        super().__init__(master, priviledge, False, windowName="Profile")
        super().createWindow()
        self.profileMainFrame()
    


    def profileMainFrame(self):
        welcomeLabel = Label(self.activeWindow,text="This is a placeholder for the new profile page!")
        welcomeLabel.pack(pady=10)