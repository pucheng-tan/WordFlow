import tkinter as tk
import login

def main():
    root = tk.Tk()
    app = login.Authentication(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
