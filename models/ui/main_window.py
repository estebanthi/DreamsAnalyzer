import datetime as dt
import shutil

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QLabel


from ui.main_window_ui import Ui_MainWindow
from models.filesystem import Filesystem
from models.dreams.dream import Dream
from models.config import Config
from models.dreams.dreams_collection import DreamsCollection


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.config = Config()
        self.initialSetup()
        self.connect()
        self._update()

    def initialSetup(self):
        self.loadDreamManagerData()

    def loadDreamManagerData(self):
        filesystem = Filesystem()
        pathname = f"{self.config['data_pathname']}/{self.config['dream_manager_data_filename']}.json"
        dream_manager_data = filesystem.load_data(pathname)
        self.dream_manager_data = dream_manager_data

    def connect(self):
        self.importJSONFileButton.clicked.connect(self.getFile)
        self.updateButton.clicked.connect(self.onUpdateButtonClick)
        self.resetButton.clicked.connect(self._update)

    def onUpdateButtonClick(self):
        self.updateDates()
        if self.dream_manager_data:
            self.updateIfData()
        else:
            self.updateIfNoData()

    def _update(self):
        if self.dream_manager_data:
            self.updateWhenLoadingData()
            self.updateIfData()
        else:
            self.updateIfNoData()

    def updateWhenLoadingData(self):
        data = self.dream_manager_data
        json_dreams = list(data['dreams'].values())
        json_tags = data['tags']

        start_date = Dream.parse(json_dreams[0], json_tags).date
        self.startDate.setDate(start_date)
        self.startDate.setDate(start_date)

        end_date = dt.datetime.now()
        self.endDate.setDate(end_date)
        self.endDate.setMaximumDate(end_date)

        self.start_date = start_date
        self.end_date = end_date

    def updateDates(self):
        start_date_value = self.startDate.date().getDate()
        start_date = dt.datetime(start_date_value[0], start_date_value[1], start_date_value[2])

        end_date_value = self.endDate.date().getDate()
        end_date = dt.datetime(end_date_value[0], end_date_value[1], end_date_value[2])

        self.start_date = start_date
        self.end_date = end_date

    def updateIfData(self):
        data = self.dream_manager_data

        date = str(dt.datetime.fromtimestamp(data['timestamp']))
        self.lastLoadedFileDate.setText(date)

        json_dreams = list(data['dreams'].values())
        json_tags = data['tags']

        self.dreams_and_hh = [Dream.parse(json_dream, json_tags) for json_dream in json_dreams]

        self.dreams_and_hh = filter(lambda dream: self.start_date <= dream.date <= self.end_date, self.dreams_and_hh)

        self.dreams = DreamsCollection([dream for dream in self.dreams_and_hh if not dream.is_hh])
        self.hh = DreamsCollection([dream for dream in self.dreams_and_hh if dream.is_hh])

        self.lucid_dreams = DreamsCollection([dream for dream in self.dreams if dream.lucid])
        self.normal_dreams = DreamsCollection([dream for dream in self.dreams if not dream.lucid])

        self.update_homepage()
        self.update_tags_page()

    def update_homepage(self):
        self.totalDreamsCounter.setText(str(len(self.dreams)))
        self.lucidDreamsCounter.setText(str(len(self.lucid_dreams)))
        self.normalDreamsCounter.setText(str(len(self.normal_dreams)))
        self.hhCounter.setText(str(len(self.hh)))

        self.averageMood.setText(str(self.dreams.get_average_meta('mood')))
        self.averageLucidity.setText(str(self.dreams.get_average_meta('lucidity')))
        self.averageClear.setText(str(self.dreams.get_average_meta('clear')))
        self.lucidDreamsRate.setText(f"{round(len(self.lucid_dreams) / len(self.dreams) * 100, 2)}%")

        self.averageDreamsPerNight.setText(str(self.dreams.get_average_dreams_per_nights()))
        self.averageLength.setText(str(self.dreams.get_average_dreams_length()))

        self.mostFrequentTag.setText(self.dreams.get_most_frequent_tag().label)
        self.mostFrequentCategory.setText(self.dreams.get_most_frequent_category().label)

        self.totalWords.setText(str(self.dreams.get_total_words()))
        self.mostFrequentHour.setText(str(self.dreams.get_most_frequent_hour()))

    def update_tags_page(self):
        self.clear_layout(self.tagsCounters)
        tags_counter = self.dreams.get_tags_counter()
        for tag, count in tags_counter:
            qlabel = QLabel(tag.label)
            qline = QLineEdit(str(count))
            qline.setReadOnly(True)
            self.tagsCounters.addRow(qlabel, qline)

        self.clear_layout(self.categoriesCounters)
        categories_counter = self.dreams.get_categories_counter()
        for category, count in categories_counter:
            qlabel = QLabel(category.label) if category else QLabel("Sans catégorie")
            qline = QLineEdit(str(count))
            qline.setReadOnly(True)
            self.categoriesCounters.addRow(qlabel, qline)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def updateIfNoData(self):
        self.lastLoadedFileDate.setText('Aucun fichier')

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
