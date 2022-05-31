from abc import abstractmethod
from PyQt5.QtCore import QObject


class Tab(QObject):

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.setupUi()
        self.connect()

    @abstractmethod
    def setupUi(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def updateData(self):
        pass