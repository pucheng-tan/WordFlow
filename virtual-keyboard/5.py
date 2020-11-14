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

la1 = tk.Label(window, text='`', bg="powder blue", font=('Arial', 12), width=5, height=2)
la1.place(x=25, y=100)
la2 = tk.Label(window, text='1', bg="powder blue", font=('Arial', 12), width=5, height=2)
la2.place(x=75, y=100)
la3 = tk.Label(window, text='2', bg="powder blue", font=('Arial', 12), width=5, height=2)
la3.place(x=125, y=100)
la4 = tk.Label(window, text='3', bg="powder blue", font=('Arial', 12), width=5, height=2)
la4.place(x=175, y=100)
la5 = tk.Label(window, text='4', bg="powder blue", font=('Arial', 12), width=5, height=2)
la5.place(x=225, y=100)
la6 = tk.Label(window, text='5', bg="powder blue", font=('Arial', 12), width=5, height=2)
la6.place(x=275, y=100)
la7 = tk.Label(window, text='6', bg="powder blue", font=('Arial', 12), width=5, height=2)
la7.place(x=325, y=100)
la8 = tk.Label(window, text='7', bg="powder blue", font=('Arial', 12), width=5, height=2)
la8.place(x=375, y=100)
la9 = tk.Label(window, text='8', bg="powder blue", font=('Arial', 12), width=5, height=2)
la9.place(x=425, y=100)
la10 = tk.Label(window, text='9', bg="powder blue", font=('Arial', 12), width=5, height=2)
la10.place(x=475, y=100)
la11 = tk.Label(window, text='0', bg="powder blue", font=('Arial', 12), width=5, height=2)
la11.place(x=525, y=100)
la12 = tk.Label(window, text='-', bg="powder blue", font=('Arial', 12), width=5, height=2)
la12.place(x=575, y=100)
la13 = tk.Label(window, text='=', bg="powder blue", font=('Arial', 12), width=5, height=2)
la13.place(x=625, y=100)
la14 = tk.Label(window, text='Delete', bg="powder blue", font=('Arial', 12), width=8, height=2)
la14.place(x=680, y=100)

lb1 = tk.Label(window, text='Tab', bg="powder blue", font=('Arial', 12), width=8, height=2)
lb1.place(x=25, y=150)
lb2 = tk.Label(window, text='q', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb2.place(x=100, y=150)
lb3 = tk.Label(window, text='w', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb3.place(x=150, y=150)
lb4 = tk.Label(window, text='e', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb4.place(x=200, y=150)
lb5 = tk.Label(window, text='r', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb5.place(x=250, y=150)
lb6 = tk.Label(window, text='t', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb6.place(x=300, y=150)
lb7 = tk.Label(window, text='y', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb7.place(x=350, y=150)
lb8 = tk.Label(window, text='u', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb8.place(x=400, y=150)
lb9 = tk.Label(window, text='i', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb9.place(x=450, y=150)
lb10 = tk.Label(window, text='o', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb10.place(x=500, y=150)
lb11 = tk.Label(window, text='p', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb11.place(x=550, y=150)
lb12 = tk.Label(window, text='[', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb12.place(x=600, y=150)
lb13 = tk.Label(window, text=']', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb13.place(x=650, y=150)
lb14 = tk.Label(window, text='\\', bg="powder blue", font=('Arial', 12), width=5, height=2)
lb14.place(x=700, y=150)

lc1 = tk.Label(window, text='Caps', bg="powder blue", font=('Arial', 12), width=10, height=2)
lc1.place(x=25, y=200)
lc2 = tk.Label(window, text='a', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc2.place(x=115, y=200)
lc3 = tk.Label(window, text='s', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc3.place(x=165, y=200)
lc4 = tk.Label(window, text='d', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc4.place(x=215, y=200)
lc5 = tk.Label(window, text='f', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc5.place(x=265, y=200)
lc6 = tk.Label(window, text='g', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc6.place(x=315, y=200)
lc7 = tk.Label(window, text='h', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc7.place(x=365, y=200)
lc8 = tk.Label(window, text='j', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc8.place(x=415, y=200)
lc9 = tk.Label(window, text='k', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc9.place(x=465, y=200)
lc10 = tk.Label(window, text='l', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc10.place(x=515, y=200)
lc11 = tk.Label(window, text=';', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc11.place(x=565, y=200)
lc12 = tk.Label(window, text='\'', bg="powder blue", font=('Arial', 12), width=5, height=2)
lc12.place(x=615, y=200)
lc13 = tk.Label(window, text='Enter', bg="powder blue", font=('Arial', 12), width=10, height=2)
lc13.place(x=665, y=200)

ld1 = tk.Label(window, text='Shift', bg="powder blue", font=('Arial', 12), width=14, height=2)
ld1.place(x=25, y=250)
ld2 = tk.Label(window, text='z', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld2.place(x=137, y=250)
ld3 = tk.Label(window, text='x', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld3.place(x=187, y=250)
ld4 = tk.Label(window, text='c', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld4.place(x=237, y=250)
ld5 = tk.Label(window, text='v', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld5.place(x=287, y=250)
ld6 = tk.Label(window, text='b', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld6.place(x=337, y=250)
ld7 = tk.Label(window, text='n', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld7.place(x=387, y=250)
ld8 = tk.Label(window, text='m', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld8.place(x=437, y=250)
ld9 = tk.Label(window, text=',', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld9.place(x=487, y=250)
ld10 = tk.Label(window, text='.', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld10.place(x=537, y=250)
ld11 = tk.Label(window, text='/', bg="powder blue", font=('Arial', 12), width=5, height=2)
ld11.place(x=587, y=250)
ld12 = tk.Label(window, text='Shift', bg="powder blue", font=('Arial', 12), width=14, height=2)
ld12.place(x=637, y=250)

le1 = tk.Label(window, text='Space', bg="powder blue", font=('Arial', 12), width=34, height=2)
le1.place(x=237, y=300)

window.mainloop()

