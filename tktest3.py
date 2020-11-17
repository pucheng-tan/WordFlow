from tkinter import *

#import colorama
# from colorama import Fore, Style


class mainMenu:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master 
        self.frame = LabelFrame(self.master)
        
        self.frame.pack()
        self.mainMenuTitle = Label(self.frame,text="Main Menu").grid(row=0,column=4)
        self.typingChallengeButton = Button(self.frame, text="Typing Challenge", command=self.loadNewChallenge).grid(row=1,column=0)
        self.userManagementButton = Button(self.frame, text="User Management", command=self.loadNewUserM).grid(row=2,column=0)
        # self.label.pack()





    def loadNewUserM(self):
        self.frame.destroy()
        self.frame = None

        # use `root` with another class
        self.another = userManagement(self.master)

    def loadNewChallenge(self):
        self.frame.destroy()
        self.frame = None

        self.another = typingChallenge(self.master)

class userManagement:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master
        self.frame = LabelFrame(self.master)
        self.frame.pack()

        self.label = Label(self.frame, text="User Mangement").grid(row=0,column=0)
        self.backButton = Button(self.frame, text="Back to main menu",command=self.back).grid(row=1,column=0)
        
        # self.label.pack()
    def back(self):
        self.frame.destroy()
        self.back = mainMenu(self.master)

class typingChallenge:
    

    def __init__(self, master):
        

        def count_words_length(text_content):
            words = text_content.split(' ')
            wordlength = [len(word) for word in words]
            print(wordlength)
            return wordlength
        


        # keep `root` in `self.master`
        self.master = master
        self.frame = LabelFrame(self.master,padx=150,pady=150)
        self.frame.pack()

        self.label = Label(self.frame, text="Typing Challenge Menu").grid(row=0,column=0)
        self.backButton = Button(self.frame, text="Back to main menu",command=self.back).grid(row=3,column=0)
        # self.label.pack()
        self.randomText = "She was in a hurry. Not the standard hurry when you're in a rush to get someplace, but a frantic hurry. The type of hurry where a few seconds could mean life or death. She raced down the road ignoring speed limits and weaving between cars. She was only a few minutes away when traffic came to a dead standstill on the road ahead."
        self.words_length = count_words_length(self.randomText)
        listOfWords = self.randomText.split()


        textShow = Text(self.frame)
        textShow.grid(row=1,column=0)
        textShow.insert('end',self.randomText)
        # textShow.insert('end',"\033[0;32;47m Test1 \033[\n")

        textShow.tag_configure("correct",background="blue",foreground="white")
        textShow.tag_configure("false",background="red",foreground="white")

         

        
        #self.textShow.insert('end',self.randomText)
        #self.textShow.configure(stateq='disabled')

        textBox = Entry(self.frame,width=35,borderwidth=5)
        textBox.grid(row=2,column=0)

      
        self.start_index = "1.0"
        self.end_index = "1." + str(self.words_length[0])

        textShow.mark_set("myword", "1.1")
        #print(self.textShow.index("myword wordend"),"here")

        self.count = 0

        self.user_input = ""
        self.correct_input = ""
        self.correctness
        
        
        
        def move_mark(self):
            # cur = textShow.index("myword wordend").split('.')
            self.count = self.count + 1
            cur = self.end_index.split('.')
            
            self.start_index = cur[0]+'.'+str(int(cur[1]) + 1)
            self.end_index = cur[0]+'.'+str(int(cur[1]) + 1 + self.words_length[self.count])

        def compare(self):
            self.correct_input = 
            if(self.user_input == self.correct_input):
                return 1
            else:
                return 0


        def key_pressed(self):
            #self.displayInput.configure(state='normal')
            self.user_input = textBox.get()
            textBox.delete(0,'end')

            self.correctness = compare()

            if (self.correctness):
                textShow.tag_add("correct", self.start_index, self.end_index)
            else:
                textShow.tag_add("false", self.start_index, self.end_index)

            move_mark(self)
            #self.displayInput.configure(state='disabled')
                
    
        
        
        

        #testing inputf
        textBox.bind('<space>',lambda a = self: key_pressed(self) )

        textBox.bind('<space')

        

    
            

        
        


    def back(self):
        self.frame.destroy()
        self.back = mainMenu(self.master)






root = Tk()
root.geometry("500x500")
root.title("Word Flow - Typing Practice")
run = mainMenu(root)

root.mainloop()

print("\033[0;32;47m Test1 \033[\n")
print("test")
# print("\033[0;37;40m Normal text\n")
# print("\033[2;37;40m Underlined text\033[0;37;40m \n")
# print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
# print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
# print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
 
# print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
# print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
# print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
# print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
# print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
# print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
# print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
# print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
# print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")
 
