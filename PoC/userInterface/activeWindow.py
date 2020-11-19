from tkinter import *

class activeWindow(object):
    def __init__(self,master):
        self.master = master
        self.activeFrame = Frame(master,bg="green",height=800,width=1000)
        

    def getItems(self):
        return self.activeFrame

        