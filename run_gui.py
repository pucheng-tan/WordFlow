import tkinter as tk
#THIS IS NOW A FUNCTION TO RUN TEST GUI
#THE PURPOSE OF TEST GUI IS A GUI THAT DOES NOT DEPEND ON THE LOGIN SCREEN -> PERFECT FOR MAKING QUICK ADJUSTMENTS TO THE GUI
from user_interface import mock_gui



root = tk.Tk()
mock_gui.TESTGUI(root)
# gui.GUI("Super-Admin", root)
root.mainloop()

