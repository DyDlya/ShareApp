import kivy
import yaml

kivy.require('2.1.0')  # Версия Kivy

from kivymd.app import MDApp
from widgets import RootContainer
from pathlib import *

from kivy.config import Config

Config.set("graphics", "width", "424") # Для Пк: 424
Config.set("graphics", "height", "650") # Для Пк: 860



class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        
        super().__init__(**kwargs)

    def build(self):
        return RootContainer(Path.cwd().parent)


def main():
    MyApp().run()


if __name__ == '__main__':
    main()
