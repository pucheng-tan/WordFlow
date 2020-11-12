import time as time
import tkinter as tk

class Timer(object):
    """
    Creates a frame with a timer.
    """
    def __init__(self, master):
        # self.master = master
        self.frame = tk.LabelFrame(master)
        # self.frame.grid(row=0, column=0)

        self.create_labels()
        self.create_buttons()

    def create_labels(self):
        """Creates the labels for the timer frame.
        Creates both the permanent labels that do not change and the labels the
        labels that do change when a button is pressed.
        """

        self.duration_label = tk.Label(self.frame, text="Duration:", font=("TkDefaultFont", 15))
        self.time_label = tk.Label(self.frame, text="02:00", font=("TkDefaultFont", 15), borderwidth=3, relief="sunken")

        self.duration_label.grid(row=1, column=0, rowspan=2)
        self.time_label.grid(row=1, column=1, rowspan=2)

    def create_buttons(self):
        """Creates the buttons for the timer frame."""

        self.up_button = tk.Button(self.frame, text="\u25b2", fg="blue", bg="white")
        self.down_button = tk.Button(self.frame, text="\u25bc", fg="blue", bg="white")
        self.start_button = tk.Button(self.frame, text="Begin",
                                      font=("TkDefaultFont", 15), fg="white",
                                      bg="blue")


        self.up_button["command"] = self.up_button_response
        self.down_button["command"] = self.down_button_response
        self.start_button["command"] = lambda: self.countdown_button(self.time_label["text"])

        self.up_button.grid(row=1, column=2)
        self.down_button.grid(row=2, column=2)
        self.start_button.grid(row=3, column=0)

    def up_button_response(self):
        """Increases the amount of time."""
        total_time = int(self.time_label["text"][1]) + 1
        if total_time <= 5:
            self.time_label.configure(text="0"+str(total_time)+":00")
            self.frame.update()

    def down_button_response(self):
        """Decreases the amount of time."""
        total_time = int(self.time_label["text"][1]) - 1
        if total_time >= 1:
            self.time_label.configure(text="0"+str(total_time)+":00")
            self.frame.update()

    def countdown_button(self, time_left):
        """Starts counting down the timer.
        When the button with Begin is clicked, it starts indicating the amount
        of time left.
        :param time_left: The amount of time initially in the timer.
        """
        time_left = int(time_left[1]) * 60

        self.start_button["state"] = tk.DISABLED

        while time_left >= 0:
            mins, secs = divmod(time_left, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # print(timer, end="\n")

            self.time_label.configure(text=timer)
            self.time_label.grid(row=1, column=1)
            self.frame.after(1000, self.frame.update())

            # time.sleep(1)

            time_left = time_left - 1

        self.start_button["state"] = "normal"


root = tk.Tk()
timer = Timer(master=root)
timer.frame.grid(row=0,column=0)
root.mainloop()



