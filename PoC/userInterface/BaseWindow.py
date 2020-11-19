from tkinter import *
from Menu import Menu
from activeWindow import activeWindow


##Note: the colors are to mark the different frames, and are not final



class baseWindow(object):
    """We will use the active window as a blueprint to create every other window. Each window has the same side buttons and the same layout,
    so we can allow other windows to inherit the active window.
    """

    # Let priviledge level be equal to (user,admin,sadmin)
    # mainMenu is true if activeWindow is main menu, else its false
    def __init__(self, master, priviledge,isMainMenu,windowName):
        """Initialize active window

        Args:
            master ([type]): this is the root window that the window will display on
            priviledge (str, optional): [this is the priviledge level of the user (user, admin, sadmin)]. Defaults to "user".
            isMainMenu (bool, optional): [True if this is the main Menu, false if not]. Defaults to True.
        """

        
        self.master = master 

        self.mainFrame = Frame(self.master)
        self.mainFrame.pack()

        self.priviledge = priviledge
        self.isMainMenu = isMainMenu
        self.windowName = windowName




        
    
        
    def createWindow(self):
        self.menu = Menu(self.mainFrame).getItems(self.priviledge,self.isMainMenu,self.windowName)


        #Place the menu on the screen
        
        self.menu.pack(side=LEFT)
        self.menu.pack_propagate(0)

        #Place the active window on the screen 

        self.activeWindow = activeWindow(self.mainFrame).getItems()
        self.activeWindow.pack(side=RIGHT)
        self.activeWindow.pack_propagate(0)











    # def sadminSidePanel(self):
    #     """this function creates buttons for a super admin user
    #     """
    #     buttons = []

    #     self.schoolManagementButton = Button(self.menuSidePanelTop, text="School Management",command=self.hello)
    #     buttons.append(self.schoolManagementButton)
    #     self.classroomManagementButton = Button(self.menuSidePanelTop, text="Classroom Management",command=self.hello)
    #     buttons.append(self.classroomManagementButton)
    #     self.userManagementButton = Button(self.menuSidePanelTop, text="User Management",command=self.hello)
    #     buttons.append(self.userManagementButton)
    #     self.reportMenuButton = Button(self.menuSidePanelTop, text="Reports",command=self.hello)
    #     buttons.append(self.reportMenuButton)
    #     self.newChallengeButton = Button(self.menuSidePanelTop, text="New Challenge",command=self.hello)
    #     buttons.append(self.newChallengeButton)
    #     self.myHistoryButton = Button(self.menuSidePanelTop, text="My History",command=self.hello)
    #     buttons.append(self.myHistoryButton)

    #     for button in buttons:
    #         button.pack()



        


    # def adminSidePanel(self):
    #     """this function creates the buttons for a admin user
    #     """
    #     buttons = []

    #     self.classroomManagementButton = Button(self.menuSidePanelTop, text="Classroom Management",command=self.hello)
    #     buttons.append(self.classroomManagementButton)
    #     self.userManagementButton = Button(self.menuSidePanelTop, text="User Management",command=self.hello)
    #     buttons.append(self.userManagementButton)
    #     self.newChallengeButton = Button(self.menuSidePanelTop, text="New Challenge",command=self.hello)
    #     buttons.append(self.newChallengeButton)
    #     self.reportMenuButton = Button(self.menuSidePanelTop, text="Reports",command=self.hello)
    #     buttons.append(self.reportMenuButton)
    #     self.myHistoryButton = Button(self.menuSidePanelTop, text="My History",command=self.hello)
    #     buttons.append(self.myHistoryButton)

    #     for button in buttons:
    #         button.pack()


        
            



        
    

    # def createMainFrame(self):
    #     """this function creates the main space that we can put things (we willa dd things to self.mainFrame)
    #     """

    #     self.mainFrame = Frame(self.master,bg="green",height=800,width=1000)
    #     self.mainFrame.pack(side=RIGHT)
    #     self.mainFrame.pack_propagate(0)

    # ##### THIS IS experimental
    # def createMenuBar(self):
    #     """this is experimental
    #     """
    #     self.menuBar = Menu(self.master)

    #     def hello():
    #         print("hello")

    #     self.helpMenu=Menu(self.menuBar)
    #     self.helpMenu.add_command(label="Exit", command=hello)
        

    #     self.master.config(menu=self.menuBar)
    #     #self.menuBar.pack(side=TOP)


def test2(activeWindow,priviledge="user"):
    from newChallengeWindow import newChallengeMenu
    def createNewChallengeWindow():
        activeWindow.masterFrame.destroy()
        activeWindow.masterFrame = None

        # use `root` with another class
        another = newChallengeMenu(activeWindow.master)

    def updateUserSidePanel():
        activeWindow.newChallengeButton.configure(command=createNewChallengeWindow)
    if priviledge == "sadmin":
        #updateSAdminSidePanel()
        pass

    elif priviledge == "admin":
        #updateAdminSidePanel()
        pass

    elif priviledge == "user":
        updateUserSidePanel()

    else:
        print("incorrect priveledge")





    

    

        



        


        

        

        



