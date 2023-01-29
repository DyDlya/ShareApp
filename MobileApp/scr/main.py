import kivy
import yaml
import os
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from widgets import RootContainer




class MyApp(App):

    def build(self):
        return RootContainer()

def _SavePaths():

    
    project_dir:str = os.path.dirname(os.path.dirname(__file__))

    # ProjectPath - полный путь проекта
    # ScriptsPath - путь к папке со скриптами 
    # UixTemplatesPath - путь к файлам разметки языка Kv
    paths = {
        "ProjectPath" : str(project_dir),
        "ScriptsPath" : str(os.path.dirname(__file__)),
        "UixTemplatesPath" : str(project_dir + "/kv-uix")
    }

    with open(paths["ScriptsPath"]+"/paths.yaml", 'w') as file:
        yaml.dump(paths, file)

def main():
    _SavePaths()
    MyApp().run()

if __name__ == '__main__':
    main()