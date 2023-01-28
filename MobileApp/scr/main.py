import kivy
import yaml

kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App

from widgets import RootContainer




class MyApp(App):

    def build(self):
        return RootContainer()



def main():
    
    MyApp().run()

if __name__ == '__main__':
    main()