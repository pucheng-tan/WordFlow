#!/usr/bin/env python3
import pyttsx3

## pyttsx text to speach demo
##note: does not run on python version 2.x
engine = pyttsx3.init()

def say_something(something):
    engine.say(something)
    engine.runAndWait()
    engine.stop()
    

dialogue = str(input("Type the audio you want to here: "))

say_something(dialogue)
