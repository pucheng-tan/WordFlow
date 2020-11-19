from BaseWindow import baseWindow
from tkinter import *


class assignedChallengeMenu(baseWindow):
    """This is the module for the main menu window
    """
    def __init__(self, master, priviledge="user"):
        super().__init__(master, priviledge, False, windowName="Assigned Challenges")
        super().createWindow()
        self.assignedChallengeMainFrame()
    


    def assignedChallengeMainFrame(self):
        welcomeLabel = Label(self.activeWindow,text="This is a placeholder for the new challenge screen!")
        welcomeLabel.pack(pady=10)