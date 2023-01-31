import kivy
import yaml
from pathlib import *
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder





class LoginWidget( AnchorLayout):
    def __init__(self, **kwargs):
        """
        :param pPath: полный путь к проекту вне зависимости от системы
        :param kwargs: необходимый параметр для конструктора класса AnchorLayout

        """
        
        """
        "Buider.load_file()" обязательно должен присутсвовать перед конструктором класса, для которого он
        подгружает шаблон "classname.kv". Если это условие не будет выполнено, то дизайн не отобразиться 
        """
        Builder.load_file("kv-uix/LoginWidget.kv")  # Подгружается экран авторизации
        AnchorLayout.__init__(self, **kwargs)
    def onLogin(self):
        print(f"Hello, {str(self.ids.loginTF.text)}")
    def onReg(self):
        print("Reg")

class RegWidget(AnchorLayout):
    def __init__(self, **kwargs):
        Builder.load_file("kv-uix/RegWidget.kv")  # Подгружается экран авторизации
        AnchorLayout.__init__(self, **kwargs)
    def onLog(self):
        print(f"Hello, {str(self.ids.loginTF.text)}")