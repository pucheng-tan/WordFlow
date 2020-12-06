import tkinter as tk
import os

os.system('xset r off')

# window1 = tk.Tk()
# window1.title('Typing Challenge')
# window1.geometry('900x500')

# f = tk.LabelFrame(window1)
# f.pack()
# #f.pack_propagate(0)

# # # create a text entry
# e = tk.Entry(f,show=None)
# e.pack()





def create_onscreen_keyboard(window,e):
    #os.system('xset r off')
    # Global Variables
    Key_row1 = ['`', '1', '2', '3', '4','5','6','7','8','9','0','-', '=', 'BackSpace']
    Key_row2 = ['\t', 'q', 'w', 'e', 'r', 't','y', 'u', 'i', 'o', 'p', '[', ']', '\\']
    Key_row3 = ['Caps_Lock', 'a', 's', 'd', 'f', 'g','h','j','k','l',';','\'', '\r']
    Key_row4 = ['shift', 'z', 'x', 'c', 'v', 'b','n','m',',','.','/', 'shift']
    Key_row5 = [' ']
    keys = Key_row1 + Key_row2 + Key_row3 + Key_row4 + Key_row5


    default_color = "powder blue"
    keypressed_color = "green"

    # labels = {}

    # create a list of list in which each list contains all the keys in a certain row
    def key_of_keys():
        new_dict = []
        new_dict.append(Key_row1)
        new_dict.append(Key_row2)
        new_dict.append(Key_row3)
        new_dict.append(Key_row4)
        new_dict.append(Key_row5)
        return new_dict


    def all_keys():
        new_dict = Key_row1 + Key_row2 + Key_row3 + Key_row4 + Key_row5
        return new_dict


    def map_to_dictionary(keys):
        keys_dict = {}

        for i in range(len(keys)):
            keys_dict[keys[i]] = "L" + str(i)

        # print(keys_dict)
        # key_dict = {'`': 'L0', '1': 'L1', '2': 'L2'}
        return keys_dict


    keys_dict = map_to_dictionary(keys)


    def key_pressed_new(event):
        # if (event.BackSpace):
        #     labels["BackSpace"].configure(bg=keypressed_color)
        # elif (event.Capslock):
        #     labels["Caps"].configure(bg=keypressed_color)
        # elif (event.Shift):
        #     labels["shift"].configure(bg=keypressed_color)
        if (event.char.lower() in keys):
            # Use the key pressed to get the label
            label = keys_dict[event.char.lower()]
            # Use the label to get the tkinter object
            labels[label].configure(bg=keypressed_color)
        

    def key_released_new(event):
        # if (event.BackSpace):
        #     labels["BackSpace"].configure(bg=default_color)
        # elif (event.Capslock):
        #     labels["Caps"].configure(bg=default_color)
        # elif (event.Shift):
        #     labels["shift"].configure(bg=default_color)
        if (event.char.lower() in keys):
            label = keys_dict[event.char.lower()]
            labels[label].configure(bg=default_color)

    e.bind("<KeyPress>", key_pressed_new)
    e.bind("<KeyRelease>", key_released_new)

    def key_pressed_shift_l(event):
        labels["L41"].configure(bg=keypressed_color)    
    def key_released_shift_l(event):
        labels["L41"].configure(bg=default_color) 

    e.bind("<KeyPress-Shift_L>", key_pressed_shift_l)
    e.bind("<KeyRelease-Shift_L>", key_released_shift_l)

    def key_pressed_shift_r(event):
        labels["L52"].configure(bg=keypressed_color)    
    def key_released_shift_r(event):
        labels["L52"].configure(bg=default_color) 

    e.bind("<KeyPress-Shift_R>", key_pressed_shift_r)
    e.bind("<KeyRelease-Shift_R>", key_released_shift_r)

    def key_pressed_backspace(event):
        labels["L13"].configure(bg=keypressed_color)    
    def key_released_backspace(event):
        labels["L13"].configure(bg=default_color) 

    e.bind("<KeyPress-BackSpace>", key_pressed_backspace)
    e.bind("<KeyRelease-BackSpace>", key_released_backspace)

    def key_pressed_caps(event):
        labels["L28"].configure(bg=keypressed_color)    
    def key_released_caps(event):
        labels["L28"].configure(bg=default_color) 

    e.bind("<KeyPress-Caps_Lock>", key_pressed_caps)
    e.bind("<KeyRelease-Caps_Lock>", key_released_caps)

    def create_labels():
        keys = key_of_keys()
        startingcoordinateX = 25
        startingCoordinateY = 100
        counter = 0

        global labels
        labels = {}

        for i in range(len(keys)):
            for j in range(len(keys[i])):

                key = "L" + str(counter)
                if (keys[i][j] == 'BackSpace'):
                    # Create the backspace label
                    labels[key] = tk.Label(window, text="Backspace", bg=default_color, font=('Arial', 12), width=10, height=2)
                    labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
                    #startingcoordinateX += 5
                elif (keys[i][j] == "\t"):
                    # Create the backspace label
                    labels[key] = tk.Label(window, text="Tab", bg=default_color, font=('Arial', 12), width=10, height=2)
                    labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
                    startingcoordinateX += 45
                elif (keys[i][j] == 'Caps_Lock'):
                    # Create the Capslock label
                    startingcoordinateX -= 45
                    labels[key] = tk.Label(window, text="Caps", bg=default_color, font=('Arial', 12), width=10, height=2)
                    labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
                    startingcoordinateX += 45
                elif (keys[i][j] == '\r'):
                    # Create the Enter label
                    labels[key] = tk.Label(window, text="Enter", bg=default_color, font=('Arial', 12), width=11, height=2)
                    labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
                    startingcoordinateX -= 45
                elif (keys[i][j] == 'shift'):
                    # Create the Shift label
                    labels[key] = tk.Label(window, text="Shift", bg=default_color, font=('Arial', 12), width=13, height=2)
                    labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
                    startingcoordinateX += 72
                elif (keys[i][j] == ' '):
                    # Create the Space label
                    startingcoordinateX += 132
                    labels[key] = tk.Label(window, text="Space", bg=default_color, font=('Arial', 12), width=30, height=2)
                    labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
                else:
                    labels[key] = tk.Label(window, text=keys[i][j], bg=default_color, font=('Arial', 12), width=5, height=2)
                    labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))

                # Increment Counter
                counter += 1

        # print(labels)
        # labels = {'L0': <tkinter.Label object .!label>, 'L1': <tkinter.Label object .!label2>}


    create_labels()
    #
#os.system('xset r off')

# # Global Variables
# Key_row1 = ['`', '1', '2', '3', '4','5','6','7','8','9','0','-', '=', 'BackSpace']
# Key_row2 = ['\t', 'q', 'w', 'e', 'r', 't','y', 'u', 'i', 'o', 'p', '[', ']', '\\']
# Key_row3 = ['Caps_Lock', 'a', 's', 'd', 'f', 'g','h','j','k','l',';','\'', '\r']
# Key_row4 = ['shift', 'z', 'x', 'c', 'v', 'b','n','m',',','.','/', 'shift']
# Key_row5 = [' ']
# keys = Key_row1 + Key_row2 + Key_row3 + Key_row4 + Key_row5


# default_color = "powder blue"
# keypressed_color = "green"

# # labels = {}

# # create a list of list in which each list contains all the keys in a certain row
# def key_of_keys():
#     new_dict = []
#     new_dict.append(Key_row1)
#     new_dict.append(Key_row2)
#     new_dict.append(Key_row3)
#     new_dict.append(Key_row4)
#     new_dict.append(Key_row5)
#     return new_dict


# def all_keys():
#     new_dict = Key_row1 + Key_row2 + Key_row3 + Key_row4 + Key_row5
#     return new_dict


# def map_to_dictionary(keys):
#     keys_dict = {}

#     for i in range(len(keys)):
#         keys_dict[keys[i]] = "L" + str(i)

#     # print(keys_dict)
#     # key_dict = {'`': 'L0', '1': 'L1', '2': 'L2'}
#     return keys_dict


# keys_dict = map_to_dictionary(keys)


# def key_pressed_new(event):
#     # if (event.BackSpace):
#     #     labels["BackSpace"].configure(bg=keypressed_color)
#     # elif (event.Capslock):
#     #     labels["Caps"].configure(bg=keypressed_color)
#     # elif (event.Shift):
#     #     labels["shift"].configure(bg=keypressed_color)
#     if (event.char.lower() in keys):
#         # Use the key pressed to get the label
#         label = keys_dict[event.char.lower()]
#         # Use the label to get the tkinter object
#         labels[label].configure(bg=keypressed_color)
    

# def key_released_new(event):
#     # if (event.BackSpace):
#     #     labels["BackSpace"].configure(bg=default_color)
#     # elif (event.Capslock):
#     #     labels["Caps"].configure(bg=default_color)
#     # elif (event.Shift):
#     #     labels["shift"].configure(bg=default_color)
#     if (event.char.lower() in keys):
#         label = keys_dict[event.char.lower()]
#         labels[label].configure(bg=default_color)

# window.bind("<KeyPress>", key_pressed_new)
# window.bind("<KeyRelease>", key_released_new)

# def key_pressed_shift_l(event):
#     labels["L41"].configure(bg=keypressed_color)    
# def key_released_shift_l(event):
#     labels["L41"].configure(bg=default_color) 

# window.bind("<KeyPress-Shift_L>", key_pressed_shift_l)
# window.bind("<KeyRelease-Shift_L>", key_released_shift_l)

# def key_pressed_shift_r(event):
#     labels["L52"].configure(bg=keypressed_color)    
# def key_released_shift_r(event):
#     labels["L52"].configure(bg=default_color) 

# window.bind("<KeyPress-Shift_R>", key_pressed_shift_r)
# window.bind("<KeyRelease-Shift_R>", key_released_shift_r)

# def key_pressed_backspace(event):
#     labels["L13"].configure(bg=keypressed_color)    
# def key_released_backspace(event):
#     labels["L13"].configure(bg=default_color) 

# window.bind("<KeyPress-BackSpace>", key_pressed_backspace)
# window.bind("<KeyRelease-BackSpace>", key_released_backspace)

# def key_pressed_caps(event):
#     labels["L28"].configure(bg=keypressed_color)    
# def key_released_caps(event):
#     labels["L28"].configure(bg=default_color) 

# window.bind("<KeyPress-Caps_Lock>", key_pressed_caps)
# window.bind("<KeyRelease-Caps_Lock>", key_released_caps)

# def create_labels():
#     keys = key_of_keys()
#     startingcoordinateX = 25
#     startingCoordinateY = 100
#     counter = 0

#     global labels
#     labels = {}

#     for i in range(len(keys)):
#         for j in range(len(keys[i])):

#             key = "L" + str(counter)
#             if (keys[i][j] == 'BackSpace'):
#                 # Create the backspace label
#                 labels[key] = tk.Label(window, text="Backspace", bg=default_color, font=('Arial', 12), width=10, height=2)
#                 labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
#                 #startingcoordinateX += 5
#             elif (keys[i][j] == "\t"):
#                 # Create the backspace label
#                 labels[key] = tk.Label(window, text="Tab", bg=default_color, font=('Arial', 12), width=10, height=2)
#                 labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
#                 startingcoordinateX += 45
#             elif (keys[i][j] == 'Caps_Lock'):
#                 # Create the Capslock label
#                 startingcoordinateX -= 45
#                 labels[key] = tk.Label(window, text="Caps", bg=default_color, font=('Arial', 12), width=10, height=2)
#                 labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
#                 startingcoordinateX += 45
#             elif (keys[i][j] == '\r'):
#                 # Create the Enter label
#                 labels[key] = tk.Label(window, text="Enter", bg=default_color, font=('Arial', 12), width=11, height=2)
#                 labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
#                 startingcoordinateX -= 45
#             elif (keys[i][j] == 'shift'):
#                 # Create the Shift label
#                 labels[key] = tk.Label(window, text="Shift", bg=default_color, font=('Arial', 12), width=13, height=2)
#                 labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
#                 startingcoordinateX += 72
#             elif (keys[i][j] == ' '):
#                 # Create the Space label
#                 startingcoordinateX += 132
#                 labels[key] = tk.Label(window, text="Space", bg=default_color, font=('Arial', 12), width=30, height=2)
#                 labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))
#             else:
#                 labels[key] = tk.Label(window, text=keys[i][j], bg=default_color, font=('Arial', 12), width=5, height=2)
#                 labels[key].place(x=startingcoordinateX + (j*55), y=startingCoordinateY + (i*50))

#             # Increment Counter
#             counter += 1

#     # print(labels)
#     # labels = {'L0': <tkinter.Label object .!label>, 'L1': <tkinter.Label object .!label2>}


# create_labels()
# os.system('xset r off')
# window.mainloop()
# create_onscreen_keyboard(f,e)
# window1.mainloop()