from activeWindow import activeWindow
from tkinter import *

class newChallengeMenu(activeWindow):
    """This is the module for the main menu window
    """
    def __init__(self, master, priviledge="user"):
        super().__init__(master, priviledge, False, windowName="New Challenge")
        
        self.newChallengeMainFrame()
    


    def newChallengeMainFrame(self):
        welcomeLabel = Label(self.mainFrame,text="This is a placeholder for the new challenge screen!")
        welcomeLabel.pack(pady=10)