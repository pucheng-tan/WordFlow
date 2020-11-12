import time as time
import tkinter as tk

class Timer(object):
    """
    Creates a frame with a timer.
    """
    def __init__(self, master):
        self.master = master
        self.frame = tk.LabelFrame(self.master)
        self.frame.grid(row=0, column=0)

        self.create_labels()
        self.create_buttons()

    def create_labels(self):
        self.duration_label = tk.Label(self.frame, text="Duration:")
        self.time_label = tk.Label(self.frame, text="2:00")

        self.duration_label.grid(row=1, column=0)
        self.time_label.grid(row=1, column=1)

    def create_buttons(self):
        self.start_button = tk.Button(self.frame, text="Begin", fg="white",
                                 bg="blue")
        self.start_button["command"] = lambda: self.countdown_button(self.time_label["text"])

        self.start_button.grid(row=2, column=0)

    def countdown_button(self, time_left):

        time_left = int(time_left[0]) * 60

        # length = 20

        self.start_button["state"] = tk.DISABLED

        while time_left >= 0:
            mins, secs = divmod(time_left, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # print(timer, end="\n")

            self.time_label.configure(text=timer)
            self.time_label.grid(row=1, column=1)
            self.frame.update()

            time.sleep(1)

            time_left = time_left - 1

        self.start_button["state"] = "normal"


root = tk.Tk()
timer = Timer(master=root)
root.mainloop()



