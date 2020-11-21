import tkinter as tk
import tkinter.font
from user_interface.active_windows import active_window
import asyncio
import threading

class NewChallengeWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # // TODO Make the New Challenge Window
        self.label = tk.Label(self.frame, text="New Challenge")
        self.label.pack()
        self.choose_a_typing_challenge()


    def choose_a_typing_challenge(self):
        self.label['text'] = "Choose a typing challenge!"

        self.create_timer()

        
        #This variable will be set the the type of test the user wants
        self.challenge_type = tk.StringVar(self.frame)
        self.challenge_type.set("Standard")  #default will be standard

        #Create the option menu
        choose_challenge_dropdown = tk.OptionMenu(self.frame, self.challenge_type, "Standard", "Programming Test", "Dictation Test")
        choose_challenge_dropdown.pack()
    
        submitButton = tk.Button(self.frame, text="Start",command=self._loadTypingChallenge)
        submitButton.pack()

    def create_timer(self):
        """Creates the labels for the timer frame.
        Creates both the permanent labels that do not change and the labels the
        labels that do change when a button is pressed.
        """
        self.challenge_duration = "02:00"

        #create timer labels (time_label displays time)
        self.timer_frame = tk.LabelFrame(self.frame, borderwidth=0)
        self.timer_frame.pack()
        self.duration_label = tk.Label(self.timer_frame, text="Duration:")
        self.time_label = tk.Label(self.timer_frame, text=self.challenge_duration, font=("TkDefaultFont", 15), borderwidth=3, relief="sunken")

        self.duration_label.grid(row=1, column=0,rowspan=2)
        self.time_label.grid(row=1, column=1, rowspan=2)
        #display buttons
        self.up_button = tk.Button(self.timer_frame, text="\u25b2", fg="blue", bg="white")
        self.down_button = tk.Button(self.timer_frame, text="\u25bc", fg="blue", bg="white")

        self.up_button["command"] = self._up_button_response
        self.down_button["command"] = self._down_button_response

        self.up_button.grid(row=1, column=2)
        self.down_button.grid(row=2, column=2)

        
    def _up_button_response(self):
        """Increases the amount of time."""
        total_time = int(self.challenge_duration[1]) + 1
        if total_time <= 5:
            self.challenge_duration = "0"+str(total_time)+":00"
            self.time_label.configure(text=self.challenge_duration)
            self.timer_frame.update()
    def _down_button_response(self):
        """Decreases the amount of time."""
        total_time = int(self.challenge_duration[1]) - 1
        if total_time >= 1:
            self.challenge_duration = "0"+str(total_time)+":00"
            self.time_label.configure(text=self.challenge_duration)
            self.timer_frame.update()


    def _loadTypingChallenge(self):
        
        # delete all the current widges except for our label
        for item in self.frame.pack_slaves():
            if (item != self.label):
                item.destroy()
        # TODO: put an if statement here that starts a test depending on the value of self.challenge_type
        random_text = "She was in a hurry. Not the standard hurry when you're in a rush to get someplace, but a frantic hurry. The type of hurry where a few seconds could mean life or death. She raced down the road ignoring speed limits and weaving between cars. She was only a few minutes away when traffic came to a dead standstill on the road ahead."
        self.display_standard_challenge(random_text)



    def display_standard_challenge(self, text_content):

        self.label["text"] = self.challenge_type.get()

        self.time_left = int(self.challenge_duration[1]) * 60

        self.time_remaining = tk.Label(self.frame,text=self.challenge_duration,font=("TkDefaultFont", 30))
        self.time_remaining.pack()
        
        self.text_content = text_content
        self.list_of_words = self.text_content.split(' ')
        self.list_of_word_lengths = [len(word) for word in self.list_of_words]
        


        self.display_text_box = tk.Text(self.frame)
        self.display_text_box_font = tkinter.font.Font(family="Times New Roman", size=21)
        self.display_text_box.configure(font=self.display_text_box_font)

        self.display_text_box.pack()
        self.display_text_box.insert('end', self.text_content)
        

        self.display_text_box.tag_configure("correct",background="blue",foreground="white")
        self.display_text_box.tag_configure("false",background="red",foreground="white")

         

        

        self.answer_box = tk.Entry(self.frame,width=35,borderwidth=5)
        self.answer_box.pack()

        def timer_countdown(challenge_window):
            while challenge_window.time_left >= 0:
                mins, secs = divmod(challenge_window.time_left, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                # print(timer, end="\n")

                challenge_window.time_remaining.configure(text=timer)
                challenge_window.frame.after(1000, challenge_window.frame.update())

                # time.sleep(1)

                challenge_window.time_left = challenge_window.time_left - 1
        
        #asyncio.run(timer_countdown())

        timer_thread = threading.Thread(target=timer_countdown,args=(self,))

        #timer_thread.start()

        highlight_thread = threading.Thread(target=(lambda: self._highlight_progress()))

        #self._highlight_progress()
        highlight_thread.start()

        

        

    
    def _highlight_progress(self):
        self.start_index = "1.0"
        self.end_index = "1." + str(self.list_of_word_lengths[0])


        #what is this??
        self.display_text_box.mark_set("myword", "1.1")
        
        self.progress_counter = 0
        
        #move start_index to the start of the next word, and move end_index to the end of the next word
        def _update_start_and_end_index(self):
            
            self.progress_counter = self.progress_counter + 1
            cur = self.end_index.split('.')
            
            self.start_index = cur[0]+'.'+str(int(cur[1]) + 1)
            self.end_index = cur[0]+'.'+str(int(cur[1]) + 1 + self.list_of_word_lengths[self.progress_counter])




        def _on_space_key_pressed(self):
            user_input = self.answer_box.get().strip(' ')
            self.answer_box.delete(0,'end')

            if(user_input == self.list_of_words[self.progress_counter]):
                self.display_text_box.tag_add("correct", self.start_index, self.end_index)
            else:
                self.display_text_box.tag_add("false", self.start_index, self.end_index)

            _update_start_and_end_index(self)
            #self.displayInput.configure(state='disabled')


        self.answer_box.bind('<space>',lambda a = self: _on_space_key_pressed(self) )

