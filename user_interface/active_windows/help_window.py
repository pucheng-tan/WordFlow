import tkinter as tk
from user_interface.active_windows import active_window

class HelpWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.display_help_information()


    def display_help_information(self):
        help_scroll_bar = tk.Scrollbar(self.frame)
        help_text = tk.Text(self.frame)
        help_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        help_text.pack(side=tk.LEFT, fill=tk.BOTH)
        help_scroll_bar.config(command=help_text.yview)
        help_text.config(yscrollcommand=help_scroll_bar.set)
        quote = """HAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished."""
        help_text.insert(tk.END, quote)

    # def show(self):
    #     self.frame.pack(fill=tk.BOTH)