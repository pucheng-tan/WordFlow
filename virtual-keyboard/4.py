import tkinter as tk

root = tk.Tk()

def key_pressed(event):
    print(event.char)

root.bind("<Key>", key_pressed)

root.mainloop()