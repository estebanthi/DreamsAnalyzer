import datetime as dt
import shutil

from PyQt5.QtWidgets import QMainWindow, QFileDialog


from ui.main_window_ui import Ui_MainWindow
from models.filesystem import Filesystem
from services.dreams import get_dreams
from services.config import load_config


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.config = load_config('config.yml')
        self.initialSetup()
        self.connect()
        self._update()

    def initialSetup(self):
        self.loadDreamManagerData()

    def loadDreamManagerData(self):
        filesystem = Filesystem()
        dream_manager_data = filesystem.load_data()
        self.dream_manager_data = dream_manager_data

    def connect(self):
        self.import_json_button.clicked.connect(self.getFile)

    def _update(self):
        if self.dream_manager_data:
            self.updateIfData()
        else:
            self.updateIfNoData()

    def updateIfData(self):
        date = str(dt.datetime.fromtimestamp(self.dream_manager_data['timestamp']))
        self.last_file_loaded_label.setText(date)

    def updateIfNoData(self):
        self.last_file_loaded_label.setText('Aucun fichier')

    def getFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Choisissez un fichier')[0]
        shutil.copy(filename, f"{self.config['data_pathname']}/{self.config['dream_manager_data_filename']}.json")
        self.loadDreamManagerData()
        self._update()
