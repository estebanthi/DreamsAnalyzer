import sys


from PyQt5.QtWidgets import QApplication


from models.Views.main_window import MainWindow
from models.Models.datamodel import DataModel
from models.Controllers.datacontroller import DataController
from models.config import Config


class App:

    def __init__(self):
        qapp = QApplication(sys.argv)

        Config.initial_config()

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


if __name__ == '__main__':
    app = App()
