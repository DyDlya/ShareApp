import kivy
import yaml

kivy.require('2.1.0')  # Версия Kivy

from kivy.app import App
from widgets import RootContainer
from pathlib import *

from kivy.config import Config

Config.set("graphics", "width", "424")
Config.set("graphics", "height", "860")



class MyApp(App):

    def build(self):
        return RootContainer(Path.cwd().parent)


def main():
    MyApp().run()


if __name__ == '__main__':
    main()
