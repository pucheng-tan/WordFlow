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
        self.textExerpt = "It was a weird concept. Why would I really need to generate a random paragraph? Could I actually learn something from doing so? All these questions were running through her head as she pressed the generate button. To her surprise, she found what she least expected to see."
    


    def newChallengeMainFrame(self):
        welcomeLabel = Label(self.activeWindow,text="This is a placeholder for the new challenge screen!")
        welcomeLabel.pack(pady=10)
        #This variable will be set the the type of test the user wants
        self.challengeType = StringVar(self.master)
        self.challengeType.set("Standard") 
        #Create the option menu
        chooseChallengeTypeDropdown = OptionMenu(self.activeWindow, self.challengeType, "Standard", "Programming Test", "Dictation Test")
        chooseChallengeTypeDropdown.pack()
    
        submitButton = Button(self.activeWindow, text="Start",command=self._loadTypingChallenge)
        submitButton.pack()

        
    def _loadTypingChallenge(self):
        
        # Deletes the current active window
        self.activeWindow.destroy()
        self.activeWindow = None

        # Creates a new active window
        self.activeWindow = activeWindow(self.mainFrame).getItems()
        self.activeWindow.pack(side=RIGHT)
        self.activeWindow.pack_propagate(0)
        # self.label = Label(self.activeWindow, text="Sup Buddy")
        # self.label.pack()
        

        # Initialie the typing challenge
        if (self.challengeType.get() == "Standard"):
            self._InitializeStandardChallenge()
        elif (self.challengeType.get() == "Programming Test"):
            self._InitializeProgrammingChallenge()
        elif (self.challengeType.get() == "Dictation Test"):
            self._InitializeDictationChallenge()


    # Initializes the Standard Challenge
    def _InitializeStandardChallenge(self):
        
        # Create the Text Area and Displays a Paragraph
        displayStandardChallenge = Text(self.activeWindow)
        displayStandardChallenge.insert('end', self.textExerpt)
        displayStandardChallenge.pack()
        
        # Text Box for Input
        textBox = Entry(self.activeWindow, width=35, borderwidth=5)
        textBox.pack()




    
    # Initializes the Programming Challenge
    def _InitializeProgrammingChallenge(self):
        pass
    

    # Initializes the Dictation Challenge
    def _InitializeDictationChallenge(self):
        pass




        


