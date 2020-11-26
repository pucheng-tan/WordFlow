import tkinter as tk
from tkinter import ttk
from user_interface.active_windows import active_window
from managements import challenge_management
from datetime import datetime

class MyHistoryWindow(active_window.ActiveWindow):

    # the number of challenge results to show on a page
    PAGE_LIMIT = 2

    ALT_ROW_COLOUR = "lightgrey"

    BUTTON_FG = "white"
    BUTTON_BG = "blue"
    BUTTON_FONT = ("Helvetica", 20)

    DEFAULT_FONT = ("Helvetica", 20)
    HEADER_FONT = ("Helvetica", 18)

    TITLE_FONT = ("Helvetica", 25, "bold")    
    TITLE = "My History"    

    PADX = 20
    PADY = 20


    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.challenge_management = challenge_management.ChallengeManagement()
        self.current_page_data = None
        self.pages = []
        self.current_page = 0

        self.create_heading()        
        self.setup_elements()
        self.generate_table()

        self.view_next_page()

        
        # // TODO Make the My History Window
        # The two lines below can be removed once the window starts being made
        # label = tk.Label(self.frame, text="My History")
        # label.pack()

    def create_heading(self):
        self.heading_frame = tk.Frame(self.frame)
        self.heading_frame.pack(side=tk.TOP, fill=tk.X)
        title_label = tk.Label(self.heading_frame, text=MyHistoryWindow.TITLE)
        title_label["font"] = MyHistoryWindow.TITLE_FONT
        title_label.pack(side=tk.LEFT, padx=MyHistoryWindow.PADX, pady=MyHistoryWindow.PADY)
        
    def setup_elements(self):
        next_button = tk.Button(self.heading_frame, 
                                text="Next", 
                                fg=MyHistoryWindow.BUTTON_FG, 
                                bg=MyHistoryWindow.BUTTON_BG, 
                                font=MyHistoryWindow.BUTTON_FONT)
        prev_button = tk.Button(self.heading_frame, 
                                text="Previous", 
                                fg=MyHistoryWindow.BUTTON_FG, 
                                bg=MyHistoryWindow.BUTTON_BG, 
                                font=MyHistoryWindow.BUTTON_FONT)

        next_button["command"] = self.view_next_page
        prev_button["command"] = self.view_previous_page
        
        next_button.pack(side=tk.RIGHT, padx=MyHistoryWindow.PADX, pady=MyHistoryWindow.PADY)
        prev_button.pack(side=tk.RIGHT, padx=MyHistoryWindow.PADX, pady=MyHistoryWindow.PADY)

        table = self.generate_table()

    def generate_table(self):
        # parent frame for table
        self.table_frame = tk.Frame(self.frame)
        self.table_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=MyHistoryWindow.PADX)

        # scroll bar in the table
        self.scroll_bar = tk.Scrollbar(self.table_frame)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        # table itself, and more scrollbar stuff
        self.data_table = ttk.Treeview(self.table_frame, yscrollcommand=self.scroll_bar.set, selectmode="browse", style="Custom.Treeview")
        self.scroll_bar.config(command=self.data_table.yview)
        self.data_table.pack(fill=tk.X)

        self.data_table["columns"] = ("Col1", "Col2", "Col3")
        self.data_table.heading("Col1", text="Col1", anchor=tk.CENTER)

        table_style = ttk.Style()
        table_style.configure("Treeview.Heading", font=MyHistoryWindow.HEADER_FONT)
        table_style.configure("Treeview", font=MyHistoryWindow.DEFAULT_FONT, rowheight=40)
        self.data_table.tag_configure("odd", background=MyHistoryWindow.ALT_ROW_COLOUR)


    def update_table_data(self):
        """Generates the table where the data is displayed
        """
        # and then display it to the user
        print(self.current_page_data)
        self.data_table.delete(*self.data_table.get_children())
        for i in range(0, len(self.current_page_data)):
            data = self.current_page_data[i]
            values = (data["wpm"], data["accuracy"], data["date_completed"])

            tag = "even" if i % 2 == 0 else "odd"
            self.data_table.insert(parent="", index="end", iid=i, values=values, tags=(tag))


    def view_previous_page(self):
        # TODO: button should just be disabled if we're on page 0
        # updates the data to the previous page data, don't pull again
        if self.current_page > 0:
            self.current_page = self.current_page - 1
            self.current_page_data = self.pages[self.current_page]
        else:
            print("Don't do that")
        self.update_table_data()

    def view_next_page(self):
        # update page number
        self.current_page = self.current_page + 1
        print("page: " + str(self.current_page))
        # if we don't have the page data, get it
        if self.current_page > len(self.pages):
            print(len(self.pages))
            
            # do the stuff to get the data
            last_challenge = None
            if self.current_page_data:
                last_challenge = self.current_page_data[-1]
            self.current_page_data = self.load_challenge_results(last_challenge)
            self.pages.append(self.current_page_data)
        # else just grab the data            
        else:
            self.current_page_data = self.pages[self.current_page]
        
        self.update_table_data()
        

    def load_challenge_results(self, last_challenge=None):
        """ Loads the challenge results data based on the last challenge that is currently in the list.
        Puts that data in self.challenge_results
        Args:
            last_challenge: on a "page" of challenges, the final challenge on that list
        """
        # Define the date to start at as either now if the list is empty, or the last challenge otherwise
        start_at = datetime.now() if not last_challenge else last_challenge["date_completed"]
        # get the data
        results = self.challenge_management.get_my_challenge_history(start_time=start_at, limit=MyHistoryWindow.PAGE_LIMIT)
        
        # check if it's good
        if "error" not in results:
            return list(results.values())
        else:
            self.display_error(results["error"])
            return []

    

    def display_error(self, error_message):
        # TODO: this should be actually displayed on the page
        print(error_message)