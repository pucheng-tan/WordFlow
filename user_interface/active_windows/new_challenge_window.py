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

        challenge_content = self.challenge_management.get_random_challenge_content(self.challenge_type)
        
        if(self.challenge_type == self.modes["Standard"]):
            StandardTypingChallenge(self.frame, self.challenge_duration, challenge_content, self.challenge_type)

        elif(self.challenge_type == self.modes["Dictation"]):
            DictationTypingChallenge(self.frame, self.challenge_duration, challenge_content, self.challenge_type)

        elif(self.challenge_type in self.modes):          
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
            """

            Args:
                challenge_results ([type]): [description]

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
        duration = self.total_time_in_seconds

        if self.time_left > 0:
            duration = duration - self.time_left
        

        challenge_results = self.challenge_management.save_challenge_results(self.correct_words, 
                                                                            self.incorrect_words, 
                                                                            self.total_words_completed,
                                                                            duration, self.mode)
        self.display_results(challenge_results)
    
    def display_challenge(self):
        """ Creates the typing challenge
        """
        #Title label
        self.challenge_label = tk.Label(self.frame)
        self.challenge_label.pack()
        self.challenge_label["text"] = self.title + " Challenge - Type anything to begin!"
        
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
                    

            # TODO: Does not account for if they finished it early!

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
            challenge_window.answer_box.unbind('<Key>')

            challenge_window.challenge_label["text"] = "Standard Challenge" #get rid of "Press any key to start the test" in the title

            #start the timer - important to put it in a thread so that performance of the test is not affected
            challenge_window.timer_thread.start()
            challenge_window._highlight_progress()
            
            
            #this line should wait for the timer to finish, however, it crashes our program.
            #thus, I put anycode that needs to be executed after the timer finished after the timer in the thread function.
            #challenge_window.timer_thread.join()

        self.answer_box.bind('<Key>',lambda a = self: on_button_press(self))



class _TTS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()



class StandardTypingChallenge(BaseTypingChallenge):
    """Creates a standard typing challenge
    """
    title = "Standard"

    def __init__(self,master,challenge_duration,challenge_content,mode):
        super().__init__(master,challenge_duration,challenge_content,mode)
        self.execute_challenge()

    
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

            

            if(len(self.list_of_words)-1 == self.progress_counter):
                #If you've reached the end of the test
                self.is_challenge_finished = True
                self.answer_box.unbind('<space>')

            if not self.is_challenge_finished:
                _update_start_and_end_index(self)
            


        self.answer_box.bind('<space>',lambda a = self: _on_space_key_pressed(self) )



#TODO implement the programming typing challenge here
class ProgrammingTypingChallenge(BaseTypingChallenge):
    def __init__(self, master, challenge_duration, challenge_language):
        self.frame = master
        self.challenge_duration = challenge_duration
        self.challenge_language = challenge_language



#TODO implement the dictation typing challenge here
class DictationTypingChallenge(BaseTypingChallenge):
    title = "Dictation"

    def __init__(self, master, challenge_duration, challenge_content, mode):
        super().__init__(master,challenge_duration,challenge_content,mode)
        #self.engine = pyttsx3.init()
        self.tts = _TTS()
        self.display_text_box.configure(foreground="white")
        
        self.execute_challenge()

    # def say_something(self, something):
    #         self.engine.say(something)
    #         self.engine.runAndWait()

    def say_something(self,tts):
        # global self.next_word
        # global self.run_next
        from subprocess import call
        while True:
            if self.run_next == True:
                
                phrase = self.next_word
                call(["python3", "speak.py", phrase])
                self.run_next = False
            

    

    def say_something_thread(self, something):
        self.run_next = True
        self.next_word=something

        self.new_thread = threading.Thread(target=self.say_something,args=(self.tts,),daemon=True)

        self.new_thread.start()




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

    


    next_word = ""
    run_next = True
    def _highlight_progress(self):
        global next_word
        global run_next
        
        self.start_index = "1.0"
        self.end_index = "1." + str(self.list_of_word_lengths[0])


        #what is this??
        self.display_text_box.mark_set("myword", "1.1")
        
        self.progress_counter = 0

        next_word = self.list_of_words[self.progress_counter]
        run_next = True
        
        def say_something(tts):
            global next_word
            global run_next
            run_next = True
            from subprocess import call
            while True:
                if run_next == True:
                    
                    phrase = next_word
                    call(["python3", "speak.py", phrase])
                    run_next = False

        self.new_thread = threading.Thread(target=say_something,args=(self.tts,),daemon=True).start()
        
        #move start_index to the start of the next word, and move end_index to the end of the next word
        def _update_start_and_end_index(self):
            
            self.progress_counter = self.progress_counter + 1
            cur = self.end_index.split('.')
            
            self.start_index = cur[0]+'.'+str(int(cur[1]) + 1)
            self.end_index = cur[0]+'.'+str(int(cur[1]) + 1 + self.list_of_word_lengths[self.progress_counter])

        print("here2")



        # TODO What should we do when there is nothing left in list of words? right now there is an error once the user gets to the end of the text
        # we should probally handle that somehow
        def _on_space_key_pressed(self):
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

            

            if(len(self.list_of_words)-1 == self.progress_counter):
                #If you've reached the end of the test
                self.is_challenge_finished = True
                self.answer_box.unbind('<space>')

            if not self.is_challenge_finished:
                _update_start_and_end_index(self)
                print("sjsjjsjs")
                next_word = self.list_of_words[self.progress_counter]
                run_next = True
            
        
            


        self.answer_box.bind('<space>',lambda a = self: _on_space_key_pressed(self) )

        
        



    

    

