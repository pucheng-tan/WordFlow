from BaseWindow import baseWindow
from activeWindow import activeWindow
from tkinter import *


class newChallengeMenu(baseWindow):
    """This is the module for the main menu window
    """
    def __init__(self, master, priviledge="user"):
        super().__init__(master, priviledge, False, windowName="New Challenge")
        super().createWindow()
        self.newChallengeMainFrame()
    


    def newChallengeMainFrame(self):
        welcomeLabel = Label(self.activeWindow,text="This is a placeholder for the new challenge screen!")
        welcomeLabel.pack(pady=10)
        #This variable will be set the the type of test the user wants
        challengeType = StringVar(self.master)
        challengeType.set("Standard") 
        #Create the option menu
        chooseChallengeTypeDropdown = OptionMenu(self.activeWindow, challengeType, "Standard", "Programming Test (Under development)", "Dictation Test (Under development)")
        chooseChallengeTypeDropdown.pack()

        submitButton = Button(self.activeWindow, text="Start",command=self._loadTypingChallenge)
        submitButton.pack()

    def _loadTypingChallenge(self):
        
        self.activeWindow.destroy()
        self.activeWindow = None

        self.activeWindow = activeWindow(self.mainFrame).getItems()
        self.activeWindow.pack(side=RIGHT)
        self.activeWindow.pack_propagate(0)



        


