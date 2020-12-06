import sys
import pyttsx3

#   These methods will be ran in a seperate process inside the dictation typing challenge
#   This is used as a workaround for running tts inside a thread on mac and having it crash


def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate',250)
    return engine

def say(s):
    engine.say(s)
    engine.runAndWait() #blocks

engine = init_engine()
say(str(sys.argv[1]))