from tkinter import *

##Note: the colors are to mark the different frames, and are not final



class activeWindow(object):
    """We will use the active window as a blueprint to create every other window. Each window has the same side buttons and the same layout,
    so we can allow other windows to inherit the active window.
    """

    # Let priviledge level be equal to (user,admin,sadmin)
    # mainMenu is true if activeWindow is main menu, else its false
    def __init__(self, master, priviledge="user", isMainMenu=True,windowName="window name here"):
        """Initialize active window

        Args:
            master ([type]): this is the root window that the window will display on
            priviledge (str, optional): [this is the priviledge level of the user (user, admin, sadmin)]. Defaults to "user".
            isMainMenu (bool, optional): [True if this is the main Menu, false if not]. Defaults to True.
        """

        
        self.master = master 
        self.priveledge = priviledge
        self.isMainMenu = isMainMenu

        self.windowName = windowName

        self.createMenuBar()
        self.createMenuSidePanel()
        self.createMainFrame()

        


    #temp function to make sure that buttons are working
    def hello(self):
        print("hello")
    
        
        

    def createMenuSidePanel(self):
        """create the side panel on the left of the screen. This is a frame with two imbedded frames. This function is called in init
        """
        self.menuSidePanel = Frame(self.master,height=800,width=200,bg="blue")
        self.menuSidePanel.pack(side=LEFT)
        self.menuSidePanel.pack_propagate(0)

        #top frame
        self.menuSidePanelTop = Frame(self.menuSidePanel,width=200,height=600,bg="yellow")
        self.menuSidePanelTop.pack(side=TOP)
        self.menuSidePanelTop.pack_propagate(0)

        #bottom frame
        self.menuSidePanelBottom = Frame(self.menuSidePanel,width=200,height=200,bg="orange")
        self.menuSidePanelBottom.pack(side=BOTTOM)
        self.menuSidePanelBottom.pack_propagate(0)



        self.mainMenuTitle = Label(self.menuSidePanelTop,text=self.windowName)
        self.mainMenuTitle.pack()

        #add the buttons to the top frame
        self.buttonsForSidePanelTop()

        #add the buttons to the bottom frame
        self.buttonsForSidePanelBottom()


    def buttonsForSidePanelTop(self):
        """this function will check the users priviledge and give the user the appropiate buttons
        """


        if self.priveledge == "sadmin":
            self.sadminSidePanel()

        elif self.priveledge == "admin":
            self.adminSidePanel()

        elif self.priveledge == "user":
            self.userSidePanel()

        else:
            print("incorrect priveledge")


    def userSidePanel(self):
        """this function creates the buttons for a normal user
        """
        buttons = []
        self.assignedChallengeButton = Button(self.menuSidePanelTop, text="Assigned Challenges",command=self.hello, width=100,pady=5)
        buttons.append(self.assignedChallengeButton)
        self.newChallengeButton = Button(self.menuSidePanelTop, text="New Challenge",command=self.hello,width=100,pady=5)
        buttons.append(self.newChallengeButton)
        self.myHistoryButton = Button(self.menuSidePanelTop, text="My History",command=self.hello,width=100)
        buttons.append(self.myHistoryButton)

        for button in buttons:
            button.pack()

    def sadminSidePanel(self):
        """this function creates buttons for a super admin user
        """
        buttons = []

        self.schoolManagementButton = Button(self.menuSidePanelTop, text="School Management",command=self.hello)
        buttons.append(self.schoolManagementButton)
        self.classroomManagementButton = Button(self.menuSidePanelTop, text="Classroom Management",command=self.hello)
        buttons.append(self.classroomManagementButton)
        self.userManagementButton = Button(self.menuSidePanelTop, text="User Management",command=self.hello)
        buttons.append(self.userManagementButton)
        self.reportMenuButton = Button(self.menuSidePanelTop, text="Reports",command=self.hello)
        buttons.append(self.reportMenuButton)
        self.newChallengeButton = Button(self.menuSidePanelTop, text="New Challenge",command=self.hello)
        buttons.append(self.newChallengeButton)
        self.myHistoryButton = Button(self.menuSidePanelTop, text="My History",command=self.hello)
        buttons.append(self.myHistoryButton)

        for button in buttons:
            button.pack()



        


    def adminSidePanel(self):
        """this function creates the buttons for a admin user
        """
        buttons = []

        self.classroomManagementButton = Button(self.menuSidePanelTop, text="Classroom Management",command=self.hello)
        buttons.append(self.classroomManagementButton)
        self.userManagementButton = Button(self.menuSidePanelTop, text="User Management",command=self.hello)
        buttons.append(self.userManagementButton)
        self.newChallengeButton = Button(self.menuSidePanelTop, text="New Challenge",command=self.hello)
        buttons.append(self.newChallengeButton)
        self.reportMenuButton = Button(self.menuSidePanelTop, text="Reports",command=self.hello)
        buttons.append(self.reportMenuButton)
        self.myHistoryButton = Button(self.menuSidePanelTop, text="My History",command=self.hello)
        buttons.append(self.myHistoryButton)

        for button in buttons:
            button.pack()

    def buttonsForSidePanelBottom(self):
        """this function adds buttons on the bottom left franme
        """
        buttons = []

        #if the active window is not the main menu, then add a return to main menu button
        if (self.isMainMenu == False):
            self.backToMainMenuButton = Button(self.menuSidePanelBottom, text="Back to Main Menu", command=self.hello)
            buttons.append(self.backToMainMenuButton)
        self.profileButton = Button(self.menuSidePanelBottom, text="My Profile", command=self.hello)
        buttons.append(self.profileButton)
        self.helpButton = Button(self.menuSidePanelBottom, text="Help", command=self.hello)
        buttons.append(self.helpButton)

        for button in buttons:
            button.pack()
        
            



        
        

    

        

    def createMainFrame(self):
        """this function creates the main space that we can put things (we willa dd things to self.mainFrame)
        """

        self.mainFrame = Frame(self.master,bg="green",height=800,width=1000)
        self.mainFrame.pack(side=RIGHT)
        self.mainFrame.pack_propagate(0)

    ##### THIS IS experimental
    def createMenuBar(self):
        """this is experimental
        """
        self.menuBar = Menu(self.master)

        def hello():
            print("hello")

        self.helpMenu=Menu(self.menuBar)
        self.helpMenu.add_command(label="Exit", command=hello)
        

        self.master.config(menu=self.menuBar)
        #self.menuBar.pack(side=TOP)

    

    

        



        


        

        

        




# root = Tk()
# root.resizable(False,False)
# #root.geometry("1200x1000")
# root.title("Word Flow - Typing Practice")

# run = activeWindow(root)

# root.mainloop()