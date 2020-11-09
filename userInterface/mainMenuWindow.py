from activeWindow import activeWindow
from tkinter import *

class mainMenu(activeWindow):
    """This is the module for the main menu window
    """
    def __init__(self, master, priviledge="user"):
        super().__init__(master,priviledge, True,windowName="Main Menu")
        
        self.mainMenuMainFrame()
    


    def mainMenuMainFrame(self):
        welcomeLabel = Label(self.mainFrame,text="Welcome <Username Placeholder>")
        welcomeLabel.pack(pady=10)

