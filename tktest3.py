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
        self.listOfWords = self.randomText.split(' ')


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
        
        
        
        
        def move_mark(self):
            # cur = textShow.index("myword wordend").split('.')
            self.count = self.count + 1
            cur = self.end_index.split('.')
            
            self.start_index = cur[0]+'.'+str(int(cur[1]) + 1)
            self.end_index = cur[0]+'.'+str(int(cur[1]) + 1 + self.words_length[self.count])




        def key_pressed(self):
            #self.displayInput.configure(state='normal')
            self.user_input = textBox.get().strip(' ')
            textBox.delete(0,'end')

            
            print(self.user_input, self.listOfWords[self.count])
            if(self.user_input == self.listOfWords[self.count]):
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

