from BaseWindow import baseWindow
from tkinter import *

class myHistoryMenu(baseWindow):
    """This is the module for the main menu window
    """
    def __init__(self, master, priviledge="user"):
        super().__init__(master, priviledge, False, windowName="My History")
        super().createWindow()
        self.myHistoryMainFrame()
    


    def myHistoryMainFrame(self):
        welcomeLabel = Label(self.activeWindow,text="This is a placeholder for the My History Menu")
        welcomeLabel.pack(pady=10)