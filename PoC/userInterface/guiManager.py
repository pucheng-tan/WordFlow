"""guiManager will start and run the GUI. Think of this module as the root of the GUI.
 """

from mainMenuWindow import mainMenu
from tkinter import *


root = Tk()

#not resizable in the x or y directions
root.resizable(False,False)

root.title("Word Flow - Typing Practice")

#created a main menu with priviledge level set to normal user and isMainMenu = True
run = mainMenu(root,"user")

root.mainloop()