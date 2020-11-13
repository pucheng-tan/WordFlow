from BaseWindow import baseWindow
from tkinter import *

class mainMenu(baseWindow):
    """This is the module for the main menu window
    """

    def __init__(self, master, priviledge="user"):
        super().__init__(master,priviledge, True,windowName="Main Menu")
        super().createWindow()
        self.mainMenuMainFrame()
        
    


    def mainMenuMainFrame(self):
        welcomeLabel = Label(self.activeWindow,text="Welcome <Username Placeholder>")
        welcomeLabel.pack(pady=10)

