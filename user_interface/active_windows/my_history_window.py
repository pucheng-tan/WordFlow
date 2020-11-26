import tkinter as tk
from user_interface.active_windows import active_window
from managements import challenge_management
from datetime import datetime

class MyHistoryWindow(active_window.ActiveWindow):

    # the number of challenge results to show on a page
    PAGE_LIMIT = 2

    BUTTON_FG = "white"
    BUTTON_BG = "blue"


    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.challenge_management = challenge_management.ChallengeManagement()
        self.current_page_data = None
        self.pages = []
        self.current_page = 0
        self.setup_elements()

        self.view_next_page()

        
        # // TODO Make the My History Window
        # The two lines below can be removed once the window starts being made
        # label = tk.Label(self.frame, text="My History")
        # label.pack()

    def setup_elements(self):
        next_button = tk.Button(self.frame, 
                                text="Next", 
                                fg=MyHistoryWindow.BUTTON_FG, 
                                bg=MyHistoryWindow.BUTTON_BG)
        prev_button = tk.Button(self.frame, 
                                text="Previous", 
                                fg=MyHistoryWindow.BUTTON_FG, 
                                bg=MyHistoryWindow.BUTTON_BG)

        next_button["command"] = self.view_next_page
        prev_button["command"] = self.view_previous_page
        next_button.grid(row=11, padx=11, pady=10)
        prev_button.grid(row=12, padx=11, pady=10)

    def update_table_data(self):
        """Generates the table where the data is displayed
        """
        # and then display it to the user
        print(self.current_page_data)

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