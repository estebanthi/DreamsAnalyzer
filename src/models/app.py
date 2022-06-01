import sys


from PyQt5.QtWidgets import QApplication


from models.ui.main_window import MainWindow
from models.config import Config
from models.Models.datamodel import DataModel
from models.Controllers.datacontroller import DataController


class App:

    def __init__(self):
        qapp = QApplication(sys.argv)

        controller = DataController()
        model = DataModel(controller)
        try:
            window = MainWindow(controller)

            controller.model = model
            controller.view = window
            controller.connect()

            window.postInit()

            window.show()

            sys.exit(qapp.exec())
        except Exception as e:
            print(e)
