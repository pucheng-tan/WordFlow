import tkinter as tk

#from functolls import partial
from tkinter import *
import tkinter

Keyboard_App = tkinter.Tk()
Keyboard_App.title("Typing Challenge")
Keyboard_App ['bg'] = 'sky blue'
Keyboard_App.resizable(0,0)

def key_pressed(event):
    print(event.char)

def select(value):
    if value == " Space ":
        entry.insert(tkinter.END, ' ')
    elif value == "Tab":
        entry.insert(tkinter.END, '    ')
    else:
        entry.insert(tkinter.END, value)

label1 = Label(Keyboard_App, text="Typing Challenge", font=('arial', 30, 'bold'),bg='powder blue', fg="#000000").grid(row=0, columnspan=40)
entry = Text(Keyboard_App, width=138, font=('arial', 12, 'bold'))
entry.grid(row=1, columnspan=40)

buttons = [
    '`','1','2','3','4','5','6','7','8','9','0','-','=',' <- ',
    'Tab','q','w','e','r','t','y','u','i','o','p','[',']','\\',
    'Caps','a','s','d','f','g','h','j','k','l',';','\'','Enter',' ',
    ' ','Shift','z','x','c','v','b','n','m',',','.','/','Shift',' ',
    ' Space '
]
varRow = 3
varColumn = 0

for button in buttons:
    command = lambda x=button: select(x)
    if button != " Space ":
        tkinter.Button(Keyboard_App, text=button, 
        width=5, padx=3, pady=3, bd=12, font=('arial', 12, 'bold'),
        activebackground="#000990", relief = 'raised', 
        command = command).grid(row=varRow, column=varColumn)
    if button == "Tab":
        tkinter.Button(Keyboard_App, text=button, 
        width=8, padx=3, pady=3, bd=12, font=('arial', 12, 'bold'),
        activebackground="#000990", relief = 'raised', 
        command = command).grid(row=varRow, column=varColumn)
    if button == " Space ":
        tkinter.Button(Keyboard_App, text=button, 
        width=118, padx=3, pady=3, bd=12, font=('arial', 12, 'bold'),
        activebackground="#000990", relief = 'raised', 
        command = command).grid(row=6, columnspan=16)

    varColumn += 1
    if varColumn > 13 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 13 and varRow == 4:
        varColumn = 0
        varRow += 1

Keyboard_App.bind("<Key>", key_pressed)

Keyboard_App.mainloop()