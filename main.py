"""Runs the authentication screen."""

import tkinter as tk
import login


def main():
    """Runs the authentication screen."""

    root = tk.Tk()
    app = login.Authentication(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
