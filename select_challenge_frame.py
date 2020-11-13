import tkinter as tk

class SelectChallengeFrame(object):
    def __init__(self, master):
        self.frame = tk.LabelFrame(master)
        self.frame.grid(row=0, column=0)
        self.challenge_type = tk.StringVar()

        self.create_labels()
        self.create_radio_buttons()
        self.create_option_menu()

        self.create_buttons()

    def create_labels(self):
        challenge_type_label = tk.Label(self.frame, text="Challenge Type:")
        challenge_type_label.grid(row=0)

    def create_radio_buttons(self):

        self.challenge_type = tk.StringVar()
        self.challenge_type.set("Standard")

        standard_button = tk.Radiobutton(self.frame, text="Standard", variable=self.challenge_type,
                                         value="Standard")
        self.programmer_button = tk.Radiobutton(self.frame, text="Programmer", variable=self.challenge_type,
                                           value="Programmer")
        dictation_button = tk.Radiobutton(self.frame, text="Dictation", variable=self.challenge_type,
                                          value="Dictation")

        standard_button.grid(row=1, sticky=tk.W)
        self.programmer_button.grid(row=2, sticky=tk.W)
        dictation_button.grid(row=4, sticky=tk.W)

    def create_option_menu(self):

        languages = ["Python","C", "HTML"]

        self.language = tk.StringVar()
        self.language.set(languages[0])

        language_option_menu = tk.OptionMenu(self.frame, self.language, *languages)

        language_option_menu.grid(row=3)


    def create_buttons(self):
        begin_button = tk.Button(self.frame, text="Begin")
        begin_button["command"] = lambda: self.clicked(self.challenge_type.get())

        begin_button.grid(row=5)

    def clicked(self, value):
        print(value)
        if value == "Programmer":
            print(self.language.get())


root = tk.Tk()
select_challenge = SelectChallengeFrame(root)
root.mainloop()
