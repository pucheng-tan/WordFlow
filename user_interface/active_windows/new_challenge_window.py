import tkinter as tk
import tkinter.font
from user_interface.active_windows import active_window
import threading
import time

class NewChallengeWindow(active_window.ActiveWindow):
    def __init__(self, gui, selections):
        """Creates the challenge window given the type of challenge, the challenge duration

        Args:
            gui ([type]): [the gui that this window is attached too]
            selections ([type]): [this is a list that contains the test perameters]

            selections is a list with challenge type at index 0 (challenge type = {"Standard","Programmer","Dictation"}),
            the language at index 1 (None if challenge type is not programmer), and the duration at index 2 as a int
        """

        active_window.ActiveWindow.__init__(self, gui)
        self.challenge_label = tk.Label(self.frame)
        self.challenge_label.pack()

        self.challenge_type = selections[0]
        self.challenge_language = selections[1] # if challenge_type is not "Programmer, this should be None"
        self.challenge_duration = selections[2]

        
        self._load_new_challenge()

        
    
    
    # def choose_a_typing_challenge(self):
    #     self.challenge_label['text'] = "Choose a typing challenge!"
    
    #     self.create_timer()
    
    
    #     #This variable will be set the the type of test the user wants
    #     self.challenge_type = tk.StringVar(self.frame)
    #     self.challenge_type.set("Standard")  #default will be standard
    
    #     #Create the option menu
    #     choose_challenge_dropdown = tk.OptionMenu(self.frame, self.challenge_type, "Standard", "Programming Test", "Dictation Test")
    #     choose_challenge_dropdown.pack()
    
    #     submitButton = tk.Button(self.frame, text="Start",command=self._loadTypingChallenge)
    #     submitButton.pack()
    
    # def create_timer(self):
    #     """Creates the labels for the timer frame.
    #     Creates both the permanent labels that do not change and the labels the
    #     labels that do change when a button is pressed.
    #     """
    #     self.challenge_duration = "02:00"
    
    #     #create timer labels (time_label displays time)
    #     self.timer_frame = tk.LabelFrame(self.frame, borderwidth=0)
    #     self.timer_frame.pack()
    #     self.duration_label = tk.Label(self.timer_frame, text="Duration:")
    #     self.time_label = tk.Label(self.timer_frame, text=self.challenge_duration, font=("TkDefaultFont", 15), borderwidth=3, relief="sunken")
    
    #     self.duration_label.grid(row=1, column=0,rowspan=2)
    #     self.time_label.grid(row=1, column=1, rowspan=2)
    #     #display buttons
    #     self.up_button = tk.Button(self.timer_frame, text="\u25b2", fg="blue", bg="white")
    #     self.down_button = tk.Button(self.timer_frame, text="\u25bc", fg="blue", bg="white")
    
    #     self.up_button["command"] = self._up_button_response
    #     self.down_button["command"] = self._down_button_response
    
    #     self.up_button.grid(row=1, column=2)
    #     self.down_button.grid(row=2, column=2)
    
    
    # def _up_button_response(self):
    #     """Increases the amount of time."""
    #     total_time = int(self.challenge_duration[1]) + 1
    #     if total_time <= 5:
    #         self.challenge_duration = "0"+str(total_time)+":00"
    #         self.time_label.configure(text=self.challenge_duration)
    #         self.timer_frame.update()
    # def _down_button_response(self):
    #     """Decreases the amount of time."""
    #     total_time = int(self.challenge_duration[1]) - 1
    #     if total_time >= 1:
    #         self.challenge_duration = "0"+str(total_time)+":00"
    #         self.time_label.configure(text=self.challenge_duration)
    #         self.timer_frame.update()


    


    def _load_new_challenge(self):
        """Creates a typing test based on the challenge type
        """
        if(self.challenge_type=="Standard"):
            StandardTypingChallenge(self.frame,self.challenge_duration)
        elif(self.challenge_type=="Programming"):
            ProgrammingTypingChallenge(self.frame,self.challenge_duration,self.challenge_language)
        elif(self.challenge_type=="Dictation"):
            DictationTypingChallenge(self.frame,self.challenge_duration)
        else:
            #should never get here
            print("ljsdjflkdsjflks")



class StandardTypingChallenge(object):
    """Creates a standard typing challenge
    """
    def __init__(self, master, challenge_duration): 
        self.frame = master
        #This it so be swapped a random challenge from firebase
        self.text_content = "She was in a hurry. Not the standard hurry when you're in a rush to get someplace, but a frantic hurry. The type of hurry where a few seconds could mean life or death. She raced down the road ignoring speed limits and weaving between cars. She was only a few minutes away when traffic came to a dead standstill on the road ahead."
        self.challenge_duration = challenge_duration

        self.correct_words = 0
        self.incorrect_words = 0
        self.total_words_completed = 0

        self.display_standard_challenge()

    def display_standard_challenge(self):
        """Creates the standard typing challenge
        """

        #Title label
        self.challenge_label = tk.Label(self.frame)
        self.challenge_label.pack()
        self.challenge_label["text"] = "Standard Challenge - Type anything to begin!"


        self.time_left = int(self.challenge_duration[1]) * 60

        self.time_remaining = tk.Label(self.frame,text=self.challenge_duration,font=("TkDefaultFont", 30))
        self.time_remaining.pack()

        #List of each word in the text content
        self.list_of_words = self.text_content.split(' ')

        #List of the length of each word, in the order of the words
        self.list_of_word_lengths = [len(word) for word in self.list_of_words]
        


        self.display_text_box = tk.Text(self.frame,height=20,font=("Times New Roman", 21))
        # self.display_text_box_font = tkinter.font.Font(family="Times New Roman", size=21)
        # self.display_text_box.configure(font=self.display_text_box_font)

        self.display_text_box.pack()
        self.display_text_box.insert('end', self.text_content)
        
        #Create tags
        self.display_text_box.tag_configure("correct",background="blue",foreground="white")
        self.display_text_box.tag_configure("false",background="red",foreground="white")

        self.answer_box = tk.Entry(self.frame,width=10,font=("TkDefaultFont", 50))
        self.answer_box.pack()

        def timer_countdown(challenge_window):
            """This is the function that makes the timer tick. It will be executed in a thread so it does not impact the performance of our program.

            Args:
                challenge_window ([type]): this is an instance of the new_challenge_window class (just give this function self as an argument)
            """
            while challenge_window.time_left >= 0:
                mins, secs = divmod(challenge_window.time_left, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                # print(timer, end="\n")

                challenge_window.time_remaining.configure(text=timer)
                time.sleep(1)
                challenge_window.frame.update()

                #challenge_window.frame.after(1000, challenge_window.frame.update())

                challenge_window.time_left = challenge_window.time_left - 1


            #Put stuff that happends after timer here - This might be temporary

            #Clean the screen
            for item in challenge_window.frame.pack_slaves():
                item.destroy()
            
            test_finished_label = tk.Label(challenge_window.frame,text="Test Finished!",font=("TkDefaultFont", 50))
            test_finished_label.pack()
            display_stats = tk.Text(challenge_window.frame,font=("TkDefaultFont", 23))
            display_stats.pack()
            display_stats.insert('end',"Test Summary")
            display_stats.insert('end',"Correct Words: "+str(challenge_window.correct_words)+"\n")
            display_stats.insert('end', "Incorrect Words: "+str(challenge_window.incorrect_words)+"\n")
            display_stats.insert('end', "Total words completed: "+str(challenge_window.total_words_completed)+"\n")
            display_stats.insert('end',"WPM: "+str(challenge_window.correct_words/int(challenge_window.challenge_duration[1]))+"\n")
            display_stats.insert('end',"Accuracy: "+str((challenge_window.correct_words/challenge_window.total_words_completed)*100)+"%")
            

        self.timer_thread = threading.Thread(target=timer_countdown,args=(self,))

        def on_button_press(challenge_window):
            """This function is to execute on the very first button press of the test. It will start the test.

            Args:
                challenge_window ([type]): this is an instance of the new_challenge_window class.
            """
            challenge_window.challenge_label["text"] = "Standard Challenge" #get rid of "Press any key to start the test" in the title

            #start the timer - important to put it in a thread so that performance of the test is not affected
            challenge_window.timer_thread.start()
            challenge_window._highlight_progress()
            #unmap the any key to this function
            challenge_window.answer_box.unbind('<Key>')
            
            #this line should wait for the timer to finish, however, it crashes our program.
            #thus, I put anycode that needs to be executed after the timer finished after the timer in the thread function.
            #challenge_window.timer_thread.join()
            
            

        self.answer_box.bind('<Key>',lambda a = self: on_button_press(self))



        # TODO: await for the timer to finish, then send results to challenge management #### Put this in the bottom of timer_countdown

        # timer_thread.join()


        

        

    
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



        # TODO What should we do when there is nothing left in list of words? right now there is an error once the user gets to the end of the text
        # we should probally handle that somehow
        def _on_space_key_pressed(self):
            user_input = self.answer_box.get().strip(' ')
            self.answer_box.delete(0,'end')

            if(user_input == self.list_of_words[self.progress_counter]):
                self.display_text_box.tag_add("correct", self.start_index, self.end_index)
                self.correct_words+=1
                self.total_words_completed+=1
            else:
                self.display_text_box.tag_add("false", self.start_index, self.end_index)
                self.incorrect_words+=1
                self.total_words_completed+=1

            _update_start_and_end_index(self)
            #self.displayInput.configure(state='disabled')


        self.answer_box.bind('<space>',lambda a = self: _on_space_key_pressed(self) )



#TODO implement the programming typing challenge here
class ProgrammingTypingChallenge(object):
    def __init__(self, master, challenge_duration, challenge_language):
        self.frame = master
        self.challenge_duration = challenge_duration
        self.challenge_language = challenge_language



#TODO implement the dictation typing challenge here
class DictationTypingChallenge(object):
    def __init__(self, master, challenge_duration):
        self.frame = master
        self.challenge_duration = challenge_duration
    

