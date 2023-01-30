import kivy
import yaml
from pathlib import *
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder


class WidgetsFound:
    """
    Класс-фундамент для возможности обращения любого виджета программы к project's paths
    """

    projectPath: Path
    uixDir: str = "kv-uix"
    uixPath: Path

    def __init__(self, pPath: Path):  # (путь к проекту, путь к шаблонам)
        self.projectPath = pPath
        self.uixPath = pPath / self.uixDir


class RootContainer(WidgetsFound, AnchorLayout):
    def __init__(self, pPath: Path, **kwargs):
        """
        :param pPath: полный путь к проекту вне зависимости от системы
        :param kwargs: необходимый параметр для конструктора класса AnchorLayout

        """
        WidgetsFound.__init__(self, pPath)  # Обращаемся к конструктору класса WidgetsFound
        """
        "Buider.load_file()" обязательно должен присутсвовать перед конструктором класса, для которого он
        подгружает шаблон "classname.kv". Если это условие не будет выполнено, то дизайн не отобразиться 
        """
        Builder.load_file(str(self.uixPath / "RootContainer.kv"))  # Подгружается экран авторизации
        AnchorLayout.__init__(self, **kwargs)
    def onLogin(self):
        print(f"Hello, {str(self.app.root.ids.loginTF.text)}")