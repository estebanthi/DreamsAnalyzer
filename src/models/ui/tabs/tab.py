from abc import ABC, abstractmethod
from PyQt5.QtCore import QObject


class Tab(ABC, QObject):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def connect(self):
        pass
