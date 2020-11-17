import tkinter as tk
import os

os.system('xset r off')

window = tk.Tk()
window.title('Typing Challenge')
window.geometry('800x500')

# create a text entry
e = tk.Entry(window,show=None)
e.pack()

def key_pressed(event):
    # change the color of key
    if event.char == '`':
        la1.configure(bg="red")
    elif event.char == '1':
        la2.configure(bg="red")
    elif event.char == '2':
        la3.configure(bg="red")
    elif event.char == '3':
        la4.configure(bg="red")
    elif event.char == '4':
        la5.configure(bg="red")
    elif event.char == '5':
        la6.configure(bg="red")
    elif event.char == '6':
        la7.configure(bg="red")
    elif event.char == '7':
        la8.configure(bg="red")
    elif event.char == '8':
        la9.configure(bg="red")
    elif event.char == '9':
        la10.configure(bg="red")
    elif event.char == '0':
        la11.configure(bg="red")
    elif event.char == '-':
        la12.configure(bg="red")
    elif event.char == '=':
        la13.configure(bg="red")

    elif event.char == 'q':
        lb2.configure(bg="red")
    elif event.char == 'w':
        lb3.configure(bg="red")
    elif event.char == 'e':
        lb4.configure(bg="red")
    elif event.char == 'r':
        lb5.configure(bg="red")
    elif event.char == 't':
        lb6.configure(bg="red")
    elif event.char == 'y':
        lb7.configure(bg="red")
    elif event.char == 'u':
        lb8.configure(bg="red")
    elif event.char == 'i':
        lb9.configure(bg="red")
    elif event.char == 'o':
        lb10.configure(bg="red")
    elif event.char == 'p':
        lb11.configure(bg="red")
    elif event.char == '[':
        lb12.configure(bg="red")
    elif event.char == ']':
        lb13.configure(bg="red")
    elif event.char == '\\':
        lb14.configure(bg="red")
    
    elif event.char == 'a':
        lc2.configure(bg="red")
    elif event.char == 's':
        lc3.configure(bg="red")
    elif event.char == 'd':
        lc4.configure(bg="red")
    elif event.char == 'f':
        lc5.configure(bg="red")
    elif event.char == 'g':
        lc6.configure(bg="red")
    elif event.char == 'h':
        lc7.configure(bg="red")
    elif event.char == 'j':
        lc8.configure(bg="red")
    elif event.char == 'k':
        lc9.configure(bg="red")
    elif event.char == 'l':
        lc10.configure(bg="red")
    elif event.char == ';':
        lc11.configure(bg="red")
    elif event.char == '\'':
        lc12.configure(bg="red")

    elif event.char == 'z':
        ld2.configure(bg="red")
    elif event.char == 'x':
        ld3.configure(bg="red")
    elif event.char == 'c':
        ld4.configure(bg="red")
    elif event.char == 'v':
        ld5.configure(bg="red")
    elif event.char == 'b':
        ld6.configure(bg="red")
    elif event.char == 'n':
        ld7.configure(bg="red")
    elif event.char == 'm':
        ld8.configure(bg="red")
    elif event.char == ',':
        ld9.configure(bg="red")
    elif event.char == '.':
        ld10.configure(bg="red")
    elif event.char == '/':
        ld11.configure(bg="red")

    elif event.char == ' ':
        le1.configure(bg="red")

def key_released(event):
    # change the color of key
    if event.char == '`':
        la1.configure(bg="powder blue")
    elif event.char == '1':
        la2.configure(bg="powder blue")
    elif event.char == '2':
        la3.configure(bg="red")
    elif event.char == '3':
        la4.configure(bg="red")
    elif event.char == '4':
        la5.configure(bg="red")
    elif event.char == '5':
        la6.configure(bg="red")
    elif event.char == '6':
        la7.configure(bg="red")
    elif event.char == '7':
        la8.configure(bg="red")
    elif event.char == '8':
        la9.configure(bg="red")
    elif event.char == '9':
        la10.configure(bg="red")
    elif event.char == '0':
        la11.configure(bg="red")
    elif event.char == '-':
        la12.configure(bg="red")
    elif event.char == '=':
        la13.configure(bg="red")

    elif event.char == 'q':
        lb2.configure(bg="red")
    elif event.char == 'w':
        lb3.configure(bg="red")
    elif event.char == 'e':
        lb4.configure(bg="red")
    elif event.char == 'r':
        lb5.configure(bg="red")
    elif event.char == 't':
        lb6.configure(bg="red")
    elif event.char == 'y':
        lb7.configure(bg="red")
    elif event.char == 'u':
        lb8.configure(bg="red")
    elif event.char == 'i':
        lb9.configure(bg="red")
    elif event.char == 'o':
        lb10.configure(bg="red")
    elif event.char == 'p':
        lb11.configure(bg="red")
    elif event.char == '[':
        lb12.configure(bg="red")
    elif event.char == ']':
        lb13.configure(bg="red")
    elif event.char == '\\':
        lb14.configure(bg="red")
    
    elif event.char == 'a':
        lc2.configure(bg="red")
    elif event.char == 's':
        lc3.configure(bg="red")
    elif event.char == 'd':
        lc4.configure(bg="red")
    elif event.char == 'f':
        lc5.configure(bg="red")
    elif event.char == 'g':
        lc6.configure(bg="red")
    elif event.char == 'h':
        lc7.configure(bg="red")
    elif event.char == 'j':
        lc8.configure(bg="red")
    elif event.char == 'k':
        lc9.configure(bg="red")
    elif event.char == 'l':
        lc10.configure(bg="red")
    elif event.char == ';':
        lc11.configure(bg="red")
    elif event.char == '\'':
        lc12.configure(bg="red")

    elif event.char == 'z':
        ld2.configure(bg="red")
    elif event.char == 'x':
        ld3.configure(bg="red")
    elif event.char == 'c':
        ld4.configure(bg="red")
    elif event.char == 'v':
        ld5.configure(bg="red")
    elif event.char == 'b':
        ld6.configure(bg="red")
    elif event.char == 'n':
        ld7.configure(bg="red")
    elif event.char == 'm':
        ld8.configure(bg="red")
    elif event.char == ',':
        ld9.configure(bg="red")
    elif event.char == '.':
        ld10.configure(bg="red")
    elif event.char == '/':
        ld11.configure(bg="red")

    elif event.char == ' ':
        le1.configure(bg="red")

window.bind("<KeyPress>", key_pressed)
window.bind("<KeyRelease>", key_released)

# create a frame and put all key buttons in the frame
#frm = tk.Frame(window)
#frm.pack()

# the virtual keyboard can be reallocate within the window by adjusting the
# following two variables
startingcoordinateX = 25
startingCoordinateY = 100

# create the first line of keys
la1 = tk.Label(window, text='`', bg="powder blue", font=('Arial', 12), width=5, height=2)
la1.place(x=startingcoordinateX, y=startingCoordinateY)
la2 = tk.Label(window, text='1', bg="powder blue", font=('Arial', 12), width=5, height=2)
la2.place(x=startingcoordinateX+50, y=startingCoordinateY)
la3 = tk.Label(window, text='2', bg="powder blue", font=('Arial', 12), width=5, height=2)
la3.place(x=startingcoordinateX+100, y=startingCoordinateY)
la4 = tk.Label(window, text='3', bg="powder blue", font=('Arial', 12), width=5, height=2)
la4.place(x=startingcoordinateX+150, y=startingCoordinateY)
la5 = tk.Label(window, text='4', bg="powder blue", font=('Arial', 12), width=5, height=2)
la5.place(x=startingcoordinateX+200, y=startingCoordinateY)
la6 = tk.Label(window, text='5', bg="powder blue", font=('Arial', 12), width=5, height=2)
la6.place(x=startingcoordinateX+250, y=startingCoordinateY)
la7 = tk.Label(window, text='6', bg="powder blue", font=('Arial', 12), width=5, height=2)
la7.place(x=startingcoordinateX+300, y=startingCoordinateY)
la8 = tk.Label(window, text='7', bg="powder blue", font=('Arial', 12), width=5, height=2)
la8.place(x=startingcoordinateX+350, y=startingCoordinateY)
la9 = tk.Label(window, text='8', bg="powder blue", font=('Arial', 12), width=5, height=2)
la9.place(x=startingcoordinateX+400, y=startingCoordinateY)
la10 = tk.Label(window, text='9', bg="powder blue", font=('Arial', 12), width=5, height=2)
la10.place(x=startingcoordinateX+450, y=startingCoordinateY)
la11 = tk.Label(window, text='0', bg="powder blue", font=('Arial', 12), width=5, height=2)
la11.place(x=startingcoordinateX+500, y=startingCoordinateY)
la12 = tk.Label(window, text='-', bg="powder blue", font=('Arial', 12), width=5, height=2)
la12.place(x=startingcoordinateX+550, y=startingCoordinateY)
la13 = tk.Label(window, text='=', bg="powder blue", font=('Arial', 12), width=5, height=2)
la13.place(x=startingcoordinateX+600, y=startingCoordinateY)
la14 = tk.Label(window, text='Delete', bg="powder blue", font=('Arial', 12), width=8, height=2)
la14.place(x=startingcoordinateX+655, y=startingCoordinateY)

# create the second line of keys
lb1 = tk.Label(window, text='Tab', bg="powder blue", font=('Arial', 12), width=8, height=2)
lb1.place(x=startingcoordinateX, y=startingCoordinateY+50)
lb2 = tk.Label(window, text='q', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb2.place(x=startingcoordinateX+75, y=startingCoordinateY+50)
lb3 = tk.Label(window, text='w', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb3.place(x=startingcoordinateX+125, y=startingCoordinateY+50)
lb4 = tk.Label(window, text='e', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb4.place(x=startingcoordinateX+175, y=startingCoordinateY+50)
lb5 = tk.Label(window, text='r', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb5.place(x=startingcoordinateX+225, y=startingCoordinateY+50)
lb6 = tk.Label(window, text='t', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb6.place(x=startingcoordinateX+275, y=startingCoordinateY+50)
lb7 = tk.Label(window, text='y', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb7.place(x=startingcoordinateX+325, y=startingCoordinateY+50)
lb8 = tk.Label(window, text='u', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb8.place(x=startingcoordinateX+375, y=startingCoordinateY+50)
lb9 = tk.Label(window, text='i', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb9.place(x=startingcoordinateX+425, y=startingCoordinateY+50)
lb10 = tk.Label(window, text='o', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb10.place(x=startingcoordinateX+475, y=startingCoordinateY+50)
lb11 = tk.Label(window, text='p', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb11.place(x=startingcoordinateX+525, y=startingCoordinateY+50)
lb12 = tk.Label(window, text='[', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb12.place(x=startingcoordinateX+575, y=startingCoordinateY+50)
lb13 = tk.Label(window, text=']', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb13.place(x=startingcoordinateX+625, y=startingCoordinateY+50)
lb14 = tk.Label(window, text='\\', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb14.place(x=startingcoordinateX+675, y=startingCoordinateY+50)

# create the third line of keys
lc1 = tk.Label(window, text='Caps', bg="powder blue", font=('Arial', 12), width=10, height=2)
lc1.place(x=startingcoordinateX, y=startingCoordinateY+100)
lc2 = tk.Label(window, text='a', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc2.place(x=startingcoordinateX+90, y=startingCoordinateY+100)
lc3 = tk.Label(window, text='s', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc3.place(x=startingcoordinateX+140, y=startingCoordinateY+100)
lc4 = tk.Label(window, text='d', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc4.place(x=startingcoordinateX+190, y=startingCoordinateY+100)
lc5 = tk.Label(window, text='f', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc5.place(x=startingcoordinateX+240, y=startingCoordinateY+100)
lc6 = tk.Label(window, text='g', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc6.place(x=startingcoordinateX+290, y=startingCoordinateY+100)
lc7 = tk.Label(window, text='h', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc7.place(x=startingcoordinateX+340, y=startingCoordinateY+100)
lc8 = tk.Label(window, text='j', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc8.place(x=startingcoordinateX+390, y=startingCoordinateY+100)
lc9 = tk.Label(window, text='k', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc9.place(x=startingcoordinateX+440, y=startingCoordinateY+100)
lc10 = tk.Label(window, text='l', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc10.place(x=startingcoordinateX+490, y=startingCoordinateY+100)
lc11 = tk.Label(window, text=';', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc11.place(x=startingcoordinateX+540, y=startingCoordinateY+100)
lc12 = tk.Label(window, text='\'', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc12.place(x=startingcoordinateX+590, y=startingCoordinateY+100)
lc13 = tk.Label(window, text='Enter', bg="powder blue", font=('Arial', 12), width=10, height=2)
lc13.place(x=startingcoordinateX+640, y=startingCoordinateY+100)

# create the fourth line of keys
ld1 = tk.Label(window, text='Shift', bg="powder blue", font=('Arial', 12), width=14, height=2)
ld1.place(x=startingcoordinateX, y=startingCoordinateY+150)
ld2 = tk.Label(window, text='z', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld2.place(x=startingcoordinateX+112, y=startingCoordinateY+150)
ld3 = tk.Label(window, text='x', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld3.place(x=startingcoordinateX+162, y=startingCoordinateY+150)
ld4 = tk.Label(window, text='c', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld4.place(x=startingcoordinateX+212, y=startingCoordinateY+150)
ld5 = tk.Label(window, text='v', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld5.place(x=startingcoordinateX+262, y=startingCoordinateY+150)
ld6 = tk.Label(window, text='b', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld6.place(x=startingcoordinateX+312, y=startingCoordinateY+150)
ld7 = tk.Label(window, text='n', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld7.place(x=startingcoordinateX+362, y=startingCoordinateY+150)
ld8 = tk.Label(window, text='m', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld8.place(x=startingcoordinateX+412, y=startingCoordinateY+150)
ld9 = tk.Label(window, text=',', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld9.place(x=startingcoordinateX+462, y=startingCoordinateY+150)
ld10 = tk.Label(window, text='.', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld10.place(x=startingcoordinateX+512, y=startingCoordinateY+150)
ld11 = tk.Label(window, text='/', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld11.place(x=startingcoordinateX+562, y=startingCoordinateY+150)
ld12 = tk.Label(window, text='Shift', bg="powder blue", font=('Arial', 12), width=14, height=2)
ld12.place(x=startingcoordinateX+612, y=startingCoordinateY+150)

# create the space key
le1 = tk.Label(window, text='Space', bg="powder blue", font=('Arial', 12), width=34, height=2)
le1.place(x=startingcoordinateX+212, y=startingCoordinateY+200)

window.mainloop()

