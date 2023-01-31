import kivy
import yaml

kivy.require('2.1.0')  # Версия Kivy

from kivymd.app import MDApp
from screens import LoginScreen, MainScreen, RegScreen
from pathlib import *
from kivy.uix.screenmanager import ScreenManager

from kivy.config import Config

Config.set("graphics", "width", "424") # Для Пк: 424
Config.set("graphics", "height", "650") # Для Пк: 860



class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        
        super().__init__(**kwargs)

    def build(self):
        sManager = ScreenManager()
        sManager.add_widget(LoginScreen(name = "login_screen"))
        sManager.add_widget(MainScreen(name = "main_screen"))
        sManager.add_widget(RegScreen(name= "reg_screen"))
        sManager.current = "login_screen"
        return sManager


def main():
    MyApp().run()


if __name__ == '__main__':
    main()
