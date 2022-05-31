import sys


from PyQt5.QtWidgets import QApplication


from models.ui.main_window import MainWindow
from models.config import Config
from models.Models.datamodel import DataModel
from models.Controllers.datacontroller import DataController


class App:

    def __init__(self):

        Config.initial_config()

        self.config = Config()
        initial_config = self.setup()

        qapp = QApplication(sys.argv)

        controller = DataController()
        model = DataModel(controller)
        window = MainWindow(controller, initial_config)

        controller.model = model
        controller.view = window
        controller.connect()

        window.postInit()

        window.show()

        sys.exit(qapp.exec())

    def setup(self):
        template = self.config.template
        anonyms = self.config.anonyms
        metas = self.config.metas

        return {'template': template, 'anonyms': anonyms, 'metas': metas}
