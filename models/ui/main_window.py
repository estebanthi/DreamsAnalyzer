import datetime as dt
import shutil

from PyQt5.QtWidgets import QMainWindow, QFileDialog


from ui.main_window_ui import Ui_MainWindow
from models.filesystem import Filesystem
from services.dreams import get_dreams, get_lucid_dreams, get_normal_dreams, get_hh
from services.dreams import get_average_meta, get_average_dreams_per_nights, get_most_frequent_tag, \
    get_average_dreams_length
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
        data = self.dream_manager_data

        date = str(dt.datetime.fromtimestamp(data['timestamp']))
        self.last_file_loaded_label.setText(date)

        self.dreams = get_dreams(data)
        for dream in self.dreams:
            dream.set_tags(data['tags'])

        self.lucid_dreams = get_lucid_dreams(self.dreams)
        self.normal_dreams = get_normal_dreams(self.dreams)
        self.hh = get_hh(data)

        self.dreams_total_value.setText(str(len(self.dreams)))
        self.dreams_lucid_value.setText(str(len(self.lucid_dreams)))
        self.dreams_normal_value.setText(str(len(self.normal_dreams)))
        self.dreams_hh_value.setText(str(len(self.hh)))

        self.mood_mean.setText(str(get_average_meta('note', self.dreams)))
        self.lucidity_mean.setText(str(get_average_meta('color', self.dreams)))
        self.clear_mean.setText(str(get_average_meta('clear', self.dreams)))
        self.rl_percent_value.setText(f"{round(len(self.lucid_dreams)/len(self.dreams)*100, 2)}%")

        self.dreams_per_night_mean.setText(str(get_average_dreams_per_nights(self.dreams)))
        self.length_mean.setText(str(get_average_dreams_length(self.dreams)))


    def updateIfNoData(self):
        self.last_file_loaded_label.setText('Aucun fichier')

        self.dreams = []
        self.lucid_dreams = []
        self.normal_dreams = []
        self.hh = []

    def getFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Choisissez un fichier')[0]
        if filename:
            shutil.copy(filename, f"{self.config['data_pathname']}/{self.config['dream_manager_data_filename']}.json")
            self.loadDreamManagerData()
            self._update()
