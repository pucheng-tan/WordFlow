import tkinter as tk
import tkinter.font
from user_interface.active_windows import active_window
import threading
import time
import datetime
from managements import challenge_management
import pyttsx3



class NewChallengeWindow(active_window.ActiveWindow):

    modes = {"Standard": 0, "Dictation": 1, "Java": 2, "Python": 3, "PHP": 4, "HTML": 5, "C": 6}

    def __init__(self, gui, selected_mode, duration_seconds):
        """Creates the challenge window given the type of challenge, the challenge duration

        Args:
            gui ([type]): [the gui that this window is attached too]

            selected_mode: An integer corresponding to the challenge mode, and prorgramming language if applicable.
            One of: {"Standard": 0, "Dictation": 1, "Java": 2, "Python": 3, "PHP": 4, "HTML": 5, "C": 6}

            duration: The duration of the challenge in seconds
        """

        active_window.ActiveWindow.__init__(self, gui)
        self.challenge_label = tk.Label(self.frame)
        self.challenge_label.pack()

        self.challenge_type = selected_mode
        self.challenge_duration = duration_seconds

        self.challenge_management = challenge_management.ChallengeManagement()
        
        self._load_new_challenge()


    def _load_new_challenge(self):
        """Creates a typing test based on the challenge type
        """

        #challenge_content = self.challenge_management.get_random_challenge_content(self.challenge_type)
        challenge_content = "hello here is a newline\nafter neline\n\tnewline then tab"
        
        if(self.challenge_type == self.modes["Standard"]):
            StandardTypingChallenge(self.frame, self.challenge_duration, challenge_content, self.challenge_type)

        elif(self.challenge_type == self.modes["Dictation"]):
            DictationTypingChallenge(self.frame, self.challenge_duration, challenge_content, self.challenge_type)

        elif(self.challenge_type in self.modes.values()):          
            ProgrammingTypingChallenge(self.frame, self.challenge_duration, challenge_content, self.challenge_type)

        
        else:
            #should never get here
            print("ljsdjflkdsjflks")


class BaseTypingChallenge(object):
    """ Base class for all of the other typing challenges
    """

    def __init__(self, master, challenge_duration, challenge_content, mode):
        self.frame = master
        self.text_content = challenge_content
        self.challenge_duration = challenge_duration
        self.mode = mode


        #each type of typing challenge stores the number of correct words, number of incorrect words, and the total words completed
        self.correct_words = 0
        self.incorrect_words = 0
        self.total_words_completed = 0

        self.correct_color="blue"
        self.incorrect_color="red"
        self.challenge_management = challenge_management.ChallengeManagement()



        self.is_challenge_finished = False

        self.display_challenge()

    def format_timer_label(self, seconds):
        """ Take in number in seconds, turn it into "2:00" format
        """
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        return timer
    def display_results(self,challenge_results):
            """Adds all the widgets to the window that display the final test results. Does not calculate the test results

            Args:
                challenge_results ([type]): [list containing the different challenge results]

            Returns:
                [type]: [description]
            """


            test_finished_label = tk.Label(self.frame,text="Challenge Finished!", font=("TkDefaultFont", 50))
            test_finished_label.pack()
            display_stats = tk.Text(self.frame, font=("TkDefaultFont", 23))
            display_stats.pack()

            # wpm = challenge_window.correct_words/int(challenge_window.challenge_duration[1])
            # accuracy = (challenge_window.correct_words/challenge_window.total_words_completed)*100

            display_stats.insert('end',"Challenge Summary" + "\n")
            #print(challenge_results)
            display_stats.insert('end',"Correct Words: " + str(self.correct_words) + "\n")
            display_stats.insert('end', "Incorrect Words: " + str(self.incorrect_words) + "\n")
            display_stats.insert('end', "Total words completed: " + str(self.total_words_completed) + "\n")
            display_stats.insert('end',"WPM: " + str(challenge_results["wpm"]) + "\n")
            display_stats.insert('end',"Accuracy: " + str(challenge_results["accuracy"])+ "%")


    def challenge_finished(self):
        """send raw stats to challenge management, get back the challenge results, then display the challenge results
        """
        duration = self.total_time_in_seconds

        #if time left is more than zero, than the test was finished before the time ran out
        if self.time_left > 0:
            duration = duration - self.time_left
        

        challenge_results = self.challenge_management.save_challenge_results(self.correct_words, 
                                                                            self.incorrect_words, 
                                                                            self.total_words_completed,
                                                                            duration, self.mode)
        self.display_results(challenge_results)
    
    def display_challenge(self):
        """ Creates the typing challenge, does everything to create the window and start the typing challenge
        """
        #Title label
        self.challenge_label = tk.Label(self.frame)
        self.challenge_label.pack()
        self.challenge_label["text"] = self.title + " Challenge - Press the space key to begin!"
        
        self.time_left = self.challenge_duration

        # TODO: remember to send to db
        self.total_time_in_seconds = self.time_left

        timer_text = self.format_timer_label(self.challenge_duration)
        self.time_remaining = tk.Label(self.frame, text=timer_text, font=("TkDefaultFont", 30))
        self.time_remaining.pack()

        #List of each word in the text content
        self.list_of_words = self.text_content.split(' ')

        #List of the length of each word, in the order of the words
        self.list_of_word_lengths = [len(word) for word in self.list_of_words]

        # the element that displays the content to be typed
        # TODO: In most challenge modes, this will display the text to be typed
        # but, in dictation, it'll have to be different
        self.display_text_box = tk.Text(self.frame, height=20, font=("Times New Roman", 21))

        #Create tags to highlight words as correct or incorrect
        self.display_text_box.tag_configure("correct", background=self.correct_color, foreground="white")
        self.display_text_box.tag_configure("false", background=self.incorrect_color, foreground="white")
        
        self.display_text_box.pack()
        self.display_text_box.insert('end', self.text_content)

        # the element that the user types into
        self.answer_box = tk.Entry(self.frame, width=10, font=("TkDefaultFont", 50))
        self.answer_box.pack()

     
    def execute_challenge(self):
        def timer_countdown(challenge_window):
            """This is the function that makes the timer tick. It will be executed in a thread so it does not impact the performance of our program.

            Args:
                challenge_window ([type]): this is an instance of the new_challenge_window class (just give this function self as an argument)
            """
            while ((challenge_window.time_left >= 0) and (not self.is_challenge_finished)):
                timer = self.format_timer_label(challenge_window.time_left)

                challenge_window.time_remaining.configure(text=timer)
                time.sleep(1)
                challenge_window.frame.update()

                challenge_window.time_left = challenge_window.time_left - 1

            


            #Put stuff that happends after timer here - This might be temporary
            #Clean the screen
            for item in challenge_window.frame.pack_slaves():
                item.destroy()
            # duration = self.total_time_in_seconds

            # challenge_results = self.challenge_management.save_challenge_results(challenge_window.correct_words, 
            #                                                                 challenge_window.incorrect_words, 
            #                                                                 challenge_window.total_words_completed,
            #                                                                 duration, self.mode)
                    

            # challenge_window.display_results(challenge_results)
            challenge_window.challenge_finished()

        #Create thread for the timer to run in
        self.timer_thread = threading.Thread(target=timer_countdown, args=(self,))

        def on_button_press(challenge_window):
            """This function is to execute on the very first button press of the test. It will start the test.

            Args:
                challenge_window ([type]): this is an instance of the new_challenge_window class.
            """
            #unmap the any key to this function
            challenge_window.answer_box.unbind('<space>')

            challenge_window.challenge_label["text"] = "Standard Challenge" #get rid of "Press any key to start the test" in the title

            #start the timer - important to put it in a thread so that performance of the test is not affected
            challenge_window.timer_thread.start()
            challenge_window._highlight_progress()
            
            
            #this line should wait for the timer to finish, however, it crashes our program.
            #thus, I put anycode that needs to be executed after the timer finished after the timer in the thread function.
            #challenge_window.timer_thread.join()

        self.answer_box.bind('<space>',lambda a = self: on_button_press(self))



class StandardTypingChallenge(BaseTypingChallenge):
    """Creates a standard typing challenge
    """
    title = "Standard"

    def __init__(self,master,challenge_duration,challenge_content,mode):
        super().__init__(master,challenge_duration,challenge_content,mode)
        self.execute_challenge()

    
    def _highlight_progress(self):
        # in charge of keaping track of users progress through the test
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
                self.correct_words+=1
                self.total_words_completed+=1
            else:
                self.display_text_box.tag_add("false", self.start_index, self.end_index)
                self.incorrect_words+=1
                self.total_words_completed+=1

            

            if(len(self.list_of_words)-1 == self.progress_counter):
                #If you've reached the end of the test
                self.is_challenge_finished = True
                self.answer_box.unbind('<space>')

            if not self.is_challenge_finished:
                _update_start_and_end_index(self)
            


        self.answer_box.bind('<space>',lambda a = self: _on_space_key_pressed(self) )



#TODO implement the programming typing challenge here
class ProgrammingTypingChallenge(BaseTypingChallenge):
    title = "Programmer"
    def __init__(self, master, challenge_duration, challenge_content, mode):
        
        super().__init__(master,challenge_duration,challenge_content,mode)
        self.execute_challenge()




#TODO implement the dictation typing challenge here
class DictationTypingChallenge(BaseTypingChallenge):
    title = "Dictation"

    def __init__(self, master, challenge_duration, challenge_content, mode):
        super().__init__(master,challenge_duration,challenge_content,mode)
        self.display_text_box.configure(foreground="white")
        
        self.execute_challenge()




    # def execute_challenge(self):
        # def timer_countdown(challenge_window):
        #     """This is the function that makes the timer tick. It will be executed in a thread so it does not impact the performance of our program.

        #     Args:
        #         challenge_window ([type]): this is an instance of the new_challenge_window class (just give this function self as an argument)
        #     """
        #     while ((challenge_window.time_left >= 0) and (not self.is_challenge_finished)):
        #         timer = self.format_timer_label(challenge_window.time_left)

        #         challenge_window.time_remaining.configure(text=timer)
        #         time.sleep(1)
        #         challenge_window.frame.update()

        #         challenge_window.time_left = challenge_window.time_left - 1

            


        #     #Put stuff that happends after timer here - This might be temporary
        #     #Clean the screen
        #     for item in challenge_window.frame.pack_slaves():
        #         item.destroy()
        #     # duration = self.total_time_in_seconds

        #     # challenge_results = self.challenge_management.save_challenge_results(challenge_window.correct_words, 
        #     #                                                                 challenge_window.incorrect_words, 
        #     #                                                                 challenge_window.total_words_completed,
        #     #                                                                 duration, self.mode)
                    

        #     # TODO: Does not account for if they finished it early!

        #     # challenge_window.display_results(challenge_results)
        #     challenge_window.challenge_finished()

        # #Create thread for the timer to run in
        # self.timer_thread = threading.Thread(target=timer_countdown, args=(self,))

        # def on_button_press(challenge_window):
        #     """This function is to execute on the very first button press of the test. It will start the test.

        #     Args:
        #         challenge_window ([type]): this is an instance of the new_challenge_window class.
        #     """
        #     challenge_window.challenge_label["text"] = "Standard Challenge" #get rid of "Press any key to start the test" in the title

        #     #start the timer - important to put it in a thread so that performance of the test is not affected
        #     challenge_window.timer_thread.start()
        #     challenge_window._highlight_progress()
        #     #unmap the any key to this function
        #     challenge_window.answer_box.unbind('<Key>')
            
        #     #this line should wait for the timer to finish, however, it crashes our program.
        #     #thus, I put anycode that needs to be executed after the timer finished after the timer in the thread function.
        #     #challenge_window.timer_thread.join()

        # self.answer_box.bind('<Key>',lambda a = self: on_button_press(self))

    

    #These need to be globals so you can access them inside of a thread
    next_word = ""
    run_next = True

    def _highlight_progress(self):
        """Keaps track of the user's progress through the typing challenge
        """
        global next_word
        global run_next
        
        self.start_index = "1.0"
        self.end_index = "1." + str(self.list_of_word_lengths[0])


        
        self.display_text_box.mark_set("myword", "1.1")
        
        self.progress_counter = 0

        next_word = self.list_of_words[self.progress_counter]
        run_next = True
        
        def say_something():
            """This function will use tts to say something. Ran inside a thread so the tts does not block

            Args:
                tts ([type]): [the string that the tts will read out loud]
            """
            global next_word
            global run_next
            run_next = True
            space_pressed = False

            #Following code is a workaround for a bug on mac
            #This is important to allow mac users to run tts inside of a thread. say_something is a function that will be executed inside of a thread
            #NOTE: If you are having issues running this, then change the Popen line to how you would run speak.py in command line (change python3)
            import subprocess
            while True:
                if run_next:  
                    run_next = False
                    
                    phrase = next_word
                    child_process = subprocess.Popen(args=["python3", "speak.py", phrase],stdout=subprocess.PIPE)

                    #this will continue until process is finished
                    while child_process.poll() is None:

                        if run_next:   #run next is set to true when the user presses space bar. This means that we can end the pronounciation of the word when the user submits there word
                            child_process.terminate()

        self.new_thread = threading.Thread(target=say_something,args=(),daemon=True).start()
        
        #move start_index to the start of the next word, and move end_index to the end of the next word
        def _update_start_and_end_index(self):
            
            self.progress_counter = self.progress_counter + 1
            cur = self.end_index.split('.')
            
            self.start_index = cur[0]+'.'+str(int(cur[1]) + 1)
            self.end_index = cur[0]+'.'+str(int(cur[1]) + 1 + self.list_of_word_lengths[self.progress_counter])

        


        def _on_space_key_pressed(self):
            """Behavior on a space keypress
            """
            global next_word
            global run_next
            
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

            
            #If you've reached the end of the test
            if(len(self.list_of_words)-1 == self.progress_counter):
                self.is_challenge_finished = True
                self.answer_box.unbind('<space>')

            if not self.is_challenge_finished:
                _update_start_and_end_index(self)
                
                next_word = self.list_of_words[self.progress_counter]
                run_next = True
            
        
            


        self.answer_box.bind('<space>',lambda a = self: _on_space_key_pressed(self) )

        
        



    

    

