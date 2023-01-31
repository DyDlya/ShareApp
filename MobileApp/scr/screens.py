from kivy.uix.screenmanager import Screen
from widgets import LoginWidget
from pathlib import *
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

class LoginScreen(Screen):
    def __init__(self,  **kwargs):
        
        Screen.__init__(self ,**kwargs)
        self.logWidget = LoginWidget()
        self.add_widget(self.logWidget)
        

        
class RegScreen(Screen):
    def __init__(self,  **kwargs):
        Builder.load_file("kv-uix/RegScreen.kv")
        Screen.__init__(self ,**kwargs)

class MainScreen(Screen):
    def __init__(self,  **kwargs):
        Builder.load_file("kv-uix/MainScreen.kv")
        Screen.__init__(self ,**kwargs)