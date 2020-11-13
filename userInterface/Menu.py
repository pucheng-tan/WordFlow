from tkinter import *

class Menu(object):
    def __init__(self,master):
        
        self.master = master

        self.menuFrame = Frame(self.master,height=800,width=200,bg="blue")

        #top frame
        self.menuFrameTop = Frame(self.menuFrame,width=200,height=600,bg="yellow")
        self.menuFrameTop.pack(side=TOP)
        self.menuFrameTop.pack_propagate(0)

        #bottom frame
        self.menuFrameBottom = Frame(self.menuFrame,width=200,height=200,bg="orange")
        self.menuFrameBottom.pack(side=BOTTOM)
        self.menuFrameBottom.pack_propagate(0)


        

        
        

    def getItems(self, priviledge, isMainMenu, windowName):
        
        
        self.mainMenuTitle = Label(self.menuFrameTop,text=windowName)
        self.mainMenuTitle.pack()

        #add the buttons to the top frame
        self.__getButtonsForTop(priviledge)

        #add the buttons to the bottom frame
        self.__getButtonsForBottom(isMainMenu)

        return self.menuFrame


    #################################################################

    #SETUP TOP PANEL

    def __getButtonsForTop(self, priviledge):
        """this function will check the users priviledge and give the user the appropiate buttons
        """


        if priviledge == "sadmin":
            self.__sadminButtons()

        elif priviledge == "admin":
            self.__adminButtons()

        elif priviledge == "user":
            self.__userButtons()

        else:
            print("incorrect priveledge")
    
    def __userButtons(self):

        buttons = []

        #Assigned Challenges Menu
        self.assignedChallengeButton = Button(self.menuFrameTop, text="Assigned Challenges",command=self.__loadAssignedChallengeMenu, width=100,pady=5)
        buttons.append(self.assignedChallengeButton)

        #Load new challenge menu
        self.newChallengeButton = Button(self.menuFrameTop, text="New Challenge",command=self.__loadNewChallengeMenu,width=100,pady=5)
        buttons.append(self.newChallengeButton)

        #my history menu
        self.myHistoryButton = Button(self.menuFrameTop, text="My History",command=self.__loadMyHistoryMenu,width=100)
        buttons.append(self.myHistoryButton)

        for button in buttons:
            button.pack()

    def __loadNewChallengeMenu(self):
        from newChallengeWindow import newChallengeMenu
        self.master.destroy()
        self.master = None

        # use `root` with another class
        test = newChallengeMenu(self.master,"user")

    def __loadAssignedChallengeMenu(self):
        from assignedChallengeWindow import assignedChallengeMenu
        self.master.destroy()
        self.master = None

        # use `root` with another class
        test = assignedChallengeMenu(self.master,"user")

    def __loadMyHistoryMenu(self):
        from myHistoryWindow import myHistoryMenu
        self.master.destroy()
        self.master = None

        
        test = myHistoryMenu(self.master,"user")

    def __sadminButtons(self):
        buttons = []

        self.schoolManagementButton = Button(self.menuSidePanelTop, text="School Management",command=self.__loadSchoolManagementMenu)
        buttons.append(self.schoolManagementButton)
        self.classroomManagementButton = Button(self.menuSidePanelTop, text="Classroom Management",command=self.__loadClassroomManagementMenu)
        buttons.append(self.classroomManagementButton)
        self.userManagementButton = Button(self.menuSidePanelTop, text="User Management",command=self.__loadUserManagementMenu)
        buttons.append(self.userManagementButton)
        self.reportMenuButton = Button(self.menuSidePanelTop, text="Reports",command=self.__loadReportsMenu)
        buttons.append(self.reportMenuButton)
        self.newChallengeButton = Button(self.menuSidePanelTop, text="New Challenge",command=self.__load)
        buttons.append(self.newChallengeButton)
        self.myHistoryButton = Button(self.menuSidePanelTop, text="My History",command=self.hello)
        buttons.append(self.myHistoryButton)

        for button in buttons:
            button.pack()

    def __adminButtons(self):
        pass

##########################################################

#SETUP BOTTOM PANEL

    def __getButtonsForBottom(self, isMainMenu):
        buttons = []

        #if the active window is not the main menu, then add a return to main menu button
        if (isMainMenu == False):
            self.backToMainMenuButton = Button(self.menuFrameBottom, text="Back to Main Menu", command=self.__loadMainMenu)
            buttons.append(self.backToMainMenuButton)
        self.profileButton = Button(self.menuFrameBottom, text="My Profile", command=self.__loadProfileMenu)
        buttons.append(self.profileButton)
        self.helpButton = Button(self.menuFrameBottom, text="Help", command=self.__loadHelpMenu)
        buttons.append(self.helpButton)

        for button in buttons:
            button.pack()


    def __loadMainMenu(self):
        from mainMenuWindow import mainMenu
        self.master.destroy()
        self.master = None

        test = mainMenu(self.master,"user")
        

    def __loadProfileMenu(self):

        from profileWindow import profileMenu
        self.master.destroy()
        self.master = None

        test = profileMenu(self.master,"user")

    def __loadHelpMenu(self):
        from helpWindow import helpMenu
        self.master.destroy()
        self.master = None

        test = helpMenu(self.master,"user")
    

    