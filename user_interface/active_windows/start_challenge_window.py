import tkinter as tk
from user_interface.active_windows import active_window

from user_interface.active_windows import new_challenge_window

class StartChallengeWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.label = tk.Label(self.frame)

        self.create_timer()
        self.choose_a_typing_challenge()

    def choose_a_typing_challenge(self):
        # self.label['text'] = "Choose a typing challenge!"

        self.select_challenge_frame = tk.Frame(self.frame)
        self.select_challenge_frame.pack()

        self.create_radio_buttons()
        self.create_option_menu()
        self.create_buttons()

    def create_timer(self):
        """Creates the labels for the timer frame.
        Creates both the permanent labels that do not change and the labels the
        labels that do change when a button is pressed.
        """
        self.challenge_duration = "02:00"

        # create timer labels (time_label displays time)
        self.timer_frame = tk.LabelFrame(self.frame, borderwidth=0)
        self.timer_frame.pack()
        self.duration_label = tk.Label(self.timer_frame, text="Duration:")
        self.time_label = tk.Label(self.timer_frame,
                                   text=self.challenge_duration,
                                   font=("TkDefaultFont", 15), borderwidth=3,
                                   relief="sunken")

        self.duration_label.grid(row=1, column=0, rowspan=2)
        self.time_label.grid(row=1, column=1, rowspan=2)
        # display buttons
        self.up_button = tk.Button(self.timer_frame, text="\u25b2", fg="blue",
                                   bg="white")
        self.down_button = tk.Button(self.timer_frame, text="\u25bc", fg="blue",
                                     bg="white")

        self.up_button["command"] = self._up_button_response
        self.down_button["command"] = self._down_button_response

        self.up_button.grid(row=1, column=2)
        self.down_button.grid(row=2, column=2)

    def _up_button_response(self):
        """Increases the amount of time."""
        total_time = int(self.challenge_duration[1]) + 1
        if total_time <= 5:
            self.challenge_duration = "0" + str(total_time) + ":00"
            self.time_label.configure(text=self.challenge_duration)
            self.timer_frame.update()

    def _down_button_response(self):
        """Decreases the amount of time."""
        total_time = int(self.challenge_duration[1]) - 1
        if total_time >= 1:
            self.challenge_duration = "0" + str(total_time) + ":00"
            self.time_label.configure(text=self.challenge_duration)
            self.timer_frame.update()

    def _load_typing_challenge(self):

        # delete all the current widges
        for item in self.frame.pack_slaves():
            item.destroy()

    def create_radio_buttons(self):

        self.challenge_type = tk.StringVar()
        self.challenge_type.set("Standard")

        standard_button = tk.Radiobutton(self.select_challenge_frame, text="Standard", variable=self.challenge_type,
                                         value="Standard")
        self.programmer_button = tk.Radiobutton(self.select_challenge_frame, text="Programmer", variable=self.challenge_type,
                                           value="Programmer")
        dictation_button = tk.Radiobutton(self.select_challenge_frame, text="Dictation", variable=self.challenge_type,
                                          value="Dictation")

        standard_button.grid(row=1, sticky=tk.W)
        self.programmer_button.grid(row=2, sticky=tk.W)
        dictation_button.grid(row=4, sticky=tk.W)

    def create_option_menu(self):

        languages = ["Python", "C", "HTML"]

        self.language = tk.StringVar()
        self.language.set(languages[0])

        language_option_menu = tk.OptionMenu(self.select_challenge_frame, self.language, *languages)

        language_option_menu.grid(row=3)


    def create_buttons(self):
        begin_button = tk.Button(self.select_challenge_frame, text="Begin")
        begin_button["command"] = self.begin_response

        begin_button.grid(row=5)

    def begin_response(self):
        modes = {"Standard": 0, "Dictation": 1, "Java": 2, "Python": 3, "PHP": 4, "HTML": 5, "C": 6}

        self.selected_challenge_language = None
        self.selected_challenge_type = self.challenge_type.get()
        print(self.selected_challenge_type, self.challenge_duration)
        
        if self.selected_challenge_type == "Programmer":
            self.selected_challenge_language = self.language.get()
            print(self.selected_challenge_language)
            selected_mode = modes[self.selected_challenge_language]
        else:
            selected_mode = modes[self.selected_challenge_type]

        self.hide()

        # change the duration from a string into an integer and do math on it to get seconds
        duration = self.challenge_duration.split(":")
        duration_seconds = (int(duration[0]) * 60) + int(duration[1]) # "2:00" --> [2, 0]
        self.gui.active_window = new_challenge_window.NewChallengeWindow(self.gui, selected_mode, duration_seconds)
        self.gui.active_window.show()




