import kivy

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
        logText: str = str(self.ids.loginTF.text)
        passText: str = str(self.ids.passwordTF.text)
        if logText and passText:            
            self.parent.parent.current = "main_screen"
            self.parent.parent.transition.direction = "left"
        elif not (logText and passText):
            print("Login and password is empty")
        elif not passText:
            print("Password is empty")
        elif not logText:
            print("Login is empty")
        
    def onReg(self):
        print("Reg")

class RegWidget(AnchorLayout):
    def __init__(self, **kwargs):
        Builder.load_file("kv-uix/RegWidget.kv")  # Подгружается экран авторизации
        AnchorLayout.__init__(self, **kwargs)
    def onLog(self):
        
        logText: str = str(self.ids.loginTF.text)
        passText: str = str(self.ids.passwordTF.text)
        if logText and passText:      
            print(f"Hello, {str(self.ids.loginTF.text)}")      
            self.parent.parent.current = "main_screen"
            self.parent.parent.transition.direction = "left"
        elif not (logText and passText):
            print("Login and password is empty (r)")
        elif not passText:
            print("Password is empty")
        elif not logText:
            print("Login is empty")