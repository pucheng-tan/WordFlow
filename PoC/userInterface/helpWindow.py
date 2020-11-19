from BaseWindow import baseWindow
from tkinter import *


class helpMenu(baseWindow):
    """This is the module for the main menu window
    """
    def __init__(self, master, priviledge="user"):
        super().__init__(master, priviledge, False, windowName="Help")
        super().createWindow()
        self.helpMenuMainFrame()
    


    def helpMenuMainFrame(self):
        welcomeLabel = Label(self.activeWindow,text="This is a placeholder for the new help menu!")
        welcomeLabel.pack(pady=10)