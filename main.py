from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty

from kivy.clock import Clock

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
def isMatchWord(text,word):
    return text == word[0:len(text)]



class MenuScreen(Screen):
    pass

class TypingScreen(Screen):
    pass

class UserInfo(BoxLayout):
    pass

class Timer(Widget):
        count = NumericProperty(0)
        timetext = StringProperty()
        def addSecond(self,a):
            self.count += 1
            self.timetext = str(self.count)
        def build(self):
            Clock.schedule_interval(self.addSecond,1.0)
        
class TypingField(BoxLayout):
    pass

class KeyboardPic(BoxLayout):
    pass





class TypingSampleApp(App):
    
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name = 'menu'))
        self.sm.add_widget(TypingScreen(name = 'typing'))
        return self.sm




TypingSampleApp().run()