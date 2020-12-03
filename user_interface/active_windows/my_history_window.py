import tkinter as tk
from tkinter import ttk
from user_interface.active_windows import active_window
from user_interface.components import list_view, header
from user_interface.components.styles import Styles
from managements import challenge_management
from datetime import datetime



class MyHistoryWindow(active_window.ActiveWindow):

    CHALLENGE_MODES = ["Standard", "Dictation", "Java", "Python", "PHP", "HTML", "C"]


    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.challenge_management = challenge_management.ChallengeManagement()
        self.heading_frame = header.Header(self.frame, "My History")
        # self.create_heading()    

        HEADINGS = ["Date", "Mode", "WPM", "Accuracy"]
        FIELDS = ["date_text", "mode", "wpm", "accuracy"]
        self.history_list = list_view.ListView(self.frame, HEADINGS, FIELDS, self.load_challenge_results)
        
    def format_data(self, data):
        # turn the data into a list
        data_list = list(data.values())

        # and then modify how things are formatted for each item
        for item in data_list:
            mode_text = MyHistoryWindow.CHALLENGE_MODES[item["mode"]]
            item["mode"] = mode_text

            # TODO: This is formatting the datetime, but it's still ugly
            # reference used: https://www.programiz.com/python-programming/datetime/strftime
            date_text = (item["date_completed"]).strftime("%m/%d/%Y, %H:%M:%S")
            item["date_text"] = date_text
        return data_list

    def load_challenge_results(self, limit, last_challenge=None):
        """ Loads the challenge results data based on the last challenge that is currently in the list.
        Puts that data in self.challenge_results
        Args:
            last_challenge: on a "page" of challenges, the final challenge on that list
        """
        # Define the date to start at as either now if the list is empty, or the last challenge otherwise
        start_at = datetime.now() if not last_challenge else last_challenge["date_completed"]
        # get the data
        challenges = self.challenge_management.get_my_challenge_history(start_time=start_at, limit=limit)
        return self.format_data(challenges)
