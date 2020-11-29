import tkinter as tk
from services import context_service

# In order to create a window in our GUI, create a new window that extends active window, or use one of our already created windows.
# Next, create widgets and display them in the self.frame of the window being created

# Note: When creating a new window, make sure that you give it a new menu item, and display that item on the main menu

class ActiveWindow(object):
    """ActiveWindow class will create a window that can be displayed on the GUI. 
    
    The active window will be displayed to the right of the main menu. When we want to add items to a new window, we will add them to the active window.
    Each window will inherit the ActiveWindow class, allowing us to show and hide the window.


    Args:
        object ([type]): [description]
    """
    def __init__(self, gui):
        self.gui = gui

        self.master = gui.master
        self.privilege = gui.privilege

        self.frame = tk.Frame(self.master)

        #self.context_service = context_service.ContextService.get_instance()
        self.context_service = gui.context_service

    def show(self):
        """Show the active window
        """
        self.frame.pack(expand=True)

    def hide(self):
        """Hide the active window
        """
        self.frame.pack_forget()