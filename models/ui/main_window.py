import datetime as dt
import shutil

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QLabel, QPushButton

from ui.main_window_ui import Ui_MainWindow
from models.filesystem import Filesystem
from models.dreams.dream import Dream
from models.time.daterange import Daterange
from models.time.timerange import TimeResolution
from models.config import Config
from models.dreams.dreams_collection import DreamsCollection
from models.ui.dream_widget import DreamWidget
from models.ui.night_widget import NightWidget
from models.template import Template
from models.ui.new_template_popup import NewTemplatePopup


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
        self.resolutionSelect.addItems(['Jour', 'Semaine', 'Mois'])
        self.dreamTypeSelect.addItems(['Tout', 'Lucides', 'Normaux'])
        self.dream_type = 'Tout'
        self.selectedTemplate = None
        self.template = None

    def loadDreamManagerData(self):
        filesystem = Filesystem()
        pathname = f"{self.config['data_pathname']}/{self.config['dream_manager_data_filename']}.json"
        dream_manager_data = filesystem.load_data(pathname)
        self.dream_manager_data = dream_manager_data

    def connect(self):
        self.importJSONFileButton.clicked.connect(self.getFile)
        self.updateButton.clicked.connect(self.onUpdateButtonClick)
        self.resetButton.clicked.connect(self._update)
        self.updateButton2.clicked.connect(self.onUpdateButtonClick)
        self.loadTemplateButton.clicked.connect(self.getTemplate)
        self.newTemplateButton.clicked.connect(self.openNewTemplatePopup)
        self.editTemplateButton.clicked.connect(self.openNewTemplatePopup)

    def onUpdateButtonClick(self):
        self.updateDates()
        self.updateDreamType()
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

        end_date = dt.datetime.now()
        self.endDate.setDate(end_date)

        self.startDate.setMaximumDate(end_date)
        self.startDate.setMinimumDate(start_date)
        self.endDate.setMaximumDate(end_date)
        self.endDate.setMinimumDate(start_date)

        self.start_date = start_date
        self.end_date = end_date

    def updateDates(self):
        start_date_value = self.startDate.date().getDate()
        start_date = dt.datetime(start_date_value[0], start_date_value[1], start_date_value[2])

        end_date_value = self.endDate.date().getDate()
        end_date = dt.datetime(end_date_value[0], end_date_value[1], end_date_value[2])

        self.start_date = start_date
        self.end_date = end_date

    def updateDreamType(self):
        self.dream_type = self.dreamTypeSelect.currentText()

    def updateIfData(self):
        data = self.dream_manager_data

        date = str(dt.datetime.fromtimestamp(data['timestamp']))
        self.lastLoadedFileDate.setText(date)

        json_dreams = list(data['dreams'].values())
        json_tags = data['tags']

        self.dreams_and_hh = [Dream.parse(json_dream, json_tags) for json_dream in json_dreams]

        self.dreams_and_hh = list(filter(lambda dream: self.start_date <= dream.date <= self.end_date, self.dreams_and_hh))

        if self.dream_type == 'Tout':
            pass
        if self.dream_type == 'Lucides':
            self.dreams_and_hh = list(filter(lambda dream: dream.lucid, self.dreams_and_hh))
        if self.dream_type == 'Normaux':
            self.dreams_and_hh = list(filter(lambda dream: not dream.lucid, self.dreams_and_hh))

        self.dreams = DreamsCollection([dream for dream in self.dreams_and_hh if not dream.is_hh])
        self.hh = DreamsCollection([dream for dream in self.dreams_and_hh if dream.is_hh])

        self.lucid_dreams = DreamsCollection([dream for dream in self.dreams if dream.lucid])
        self.normal_dreams = DreamsCollection([dream for dream in self.dreams if not dream.lucid])

        self.update_homepage()
        self.update_tags_page()
        self.update_plot_pages()
        self.update_dreams_page()
        self.update_statistics_page()
        self.update_as_page()

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
        self.clearLayout(self.tagsCounters)
        tags_counter = self.dreams.get_tags_counter()
        for tag, count in tags_counter:
            qlabel = QLabel(tag.label)
            qline = QLineEdit(str(count))
            qline.setReadOnly(True)
            self.tagsCounters.addRow(qlabel, qline)

        self.clearLayout(self.categoriesCounters)
        categories_counter = self.dreams.get_categories_counter()
        for category, count in categories_counter:
            qlabel = QLabel(category.label) if category else QLabel("Sans catégorie")
            qline = QLineEdit(str(count))
            qline.setReadOnly(True)
            self.categoriesCounters.addRow(qlabel, qline)

    def update_dreams_page(self):
        for dream in sorted(self.dreams, key=lambda dream: dream.date, reverse=True):
            self.dreamsLayoutVertical.addWidget(DreamWidget(dream))

    def update_plot_pages(self):
        dates = [dream.date.round(TimeResolution.DAYS.value) for dream in self.dreams]
        sorted_dates = sorted(dates)

        start = sorted_dates[0]
        resolution = self.get_plot_resolution()

        daterange = Daterange(start, dt.datetime.now(), resolution)
        x = [date for date in daterange]
        time_intervals = daterange.split(resolution)

        total_dreams_values = self.get_dreams_collection_values_over_time(self.dreams, time_intervals, 'count_dreams')
        self.totalDreamsPlot.clear()
        self.totalDreamsPlot.plot(x, total_dreams_values, 'black')
        self.format_mplWidget(self.totalDreamsPlot, 'Total rêves', x, total_dreams_values, 4)

        total_lucid_dreams_values = self.get_dreams_collection_values_over_time(self.lucid_dreams, time_intervals, \
                                                                                'count_dreams')
        self.lucidDreamsPlot.clear()
        self.lucidDreamsPlot.plot(x, total_lucid_dreams_values, 'blue')
        self.format_mplWidget(self.lucidDreamsPlot, 'Total rêves lucies', x, total_lucid_dreams_values, 4)

        average_dreams_per_night_values = self.get_dreams_collection_values_over_time(self.dreams, time_intervals, \
                                                                                      "get_average_dreams_per_nights")
        self.averageDreamsPerNightPlot.clear()
        self.averageDreamsPerNightPlot.plot(x, average_dreams_per_night_values, 'black')
        self.format_mplWidget(self.averageDreamsPerNightPlot, "Rêves par nuit", x, average_dreams_per_night_values, 4)

        lucid_dreams_rate_values = self.get_dreams_collection_values_over_time(self.dreams, time_intervals,
                                                                               'get_lucid_dreams_rate')
        self.lucidDreamsRatePlot.clear()
        self.lucidDreamsRatePlot.plot(x, lucid_dreams_rate_values, 'blue')
        self.format_mplWidget(self.lucidDreamsRatePlot, 'Taux de rêves lucides (en %)', x, lucid_dreams_rate_values, 4)

        clear_values = self.get_dreams_collection_values_over_time(self.dreams, time_intervals, 'get_average_clear')
        self.averageClearPlot.clear()
        self.averageClearPlot.plot(x, clear_values, 'red')
        self.format_mplWidget(self.averageClearPlot, 'Clareté moyenne', x, clear_values, 4)

        mood_values = self.get_dreams_collection_values_over_time(self.dreams, time_intervals, 'get_average_mood')
        self.averageMoodPlot.clear()
        self.averageMoodPlot.plot(x, mood_values, 'red')
        self.format_mplWidget(self.averageMoodPlot, 'Mood moyen', x, mood_values, 4)

        lucidity_values = self.get_dreams_collection_values_over_time(self.dreams, time_intervals,
                                                                      'get_average_lucidity')
        self.averageLucidityPlot.clear()
        self.averageLucidityPlot.plot(x, lucidity_values, 'red')
        self.format_mplWidget(self.averageLucidityPlot, 'Lucidité moyenne', x, lucidity_values, 4)

        dreams_lengths_values = self.get_dreams_collection_values_over_time(self.dreams, time_intervals,
                                                                      'get_average_dreams_length')
        self.averageDreamLengtPlot.clear()
        self.averageDreamLengtPlot.plot(x, dreams_lengths_values, 'green')
        self.format_mplWidget(self.averageDreamLengtPlot, 'Longueur de rêve moyenne (en mots)', x, dreams_lengths_values, 4)

    def get_plot_resolution(self):
        selected_resolution = self.resolutionSelect.currentText()
        resolution = TimeResolution.DAYS.value
        if selected_resolution == 'Semaine':
            resolution = TimeResolution.WEEKS.value
        if selected_resolution == 'Mois':
            resolution = TimeResolution.MONTHS.value
        return resolution

    def update_statistics_page(self):
        dreams_by_day = self.dreams.group_by_day()
        lucid_dreams_by_day = {day: len(list(filter(lambda dream: dream.lucid, dreams_by_day[day]))) for day in dreams_by_day.keys()}
        normal_dreams_by_days = {day: len(list(filter(lambda dream: not dream.lucid, dreams_by_day[day]))) for day in
                               dreams_by_day.keys()}
        hh_by_days = self.hh.group_by_day()
        hh = {day: len(hh_by_days[day]) for day in hh_by_days.keys()}
        vivid_per_day = self.dreams.filter(lambda dream: dream.clear == 4).group_by_day()

        labels = ['RN', 'RL', 'VIVID', 'HH']
        colors = ['green', 'blue', 'orange', 'purple']


        days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        width = 0.2


        self.dreamsByDayPlot.clear()
        self.dreamsByDayPlot.bar(days, list(normal_dreams_by_days.values()), width=width, color='green', label='RN')
        self.dreamsByDayPlot.bar(days, list(lucid_dreams_by_day.values()), width=width, space=width, color='blue', label='RL')
        self.dreamsByDayPlot.bar(days, [len(dreams) for dreams in vivid_per_day.values()], width=width,
                                   space=width * 2, color='orange', label='VIVID')
        self.dreamsByDayPlot.bar(days, list(hh.values()), width=width, space=width*3, color='purple', label='HH',
                                 legend=True, ylabel='Quantité')

        self.inductionsPlot.clear()
        wilds_nb = len(self.lucid_dreams.get_wilds())
        dilds_nb = len(self.lucid_dreams.get_dilds())
        self.inductionsPlot.pie([dilds_nb, wilds_nb], colors=['teal', 'brown'], legend_labels=['WILD', 'DILD'])
        self.inductionsPlot.setTitle("Méthodes d'inductions")

        self.wbtbPlot.clear()
        wbtb_nb = len(self.lucid_dreams.get_dreams_containing_tag('WBTB'))
        non_wbtb_nb = len(self.lucid_dreams.get_dreams_not_containing_tag('WBTB'))
        self.wbtbPlot.pie([wbtb_nb, non_wbtb_nb], colors=['aquamarine', 'mediumseagreen'], legend_labels=['WBTB', ' Pas WBTB'])
        self.wbtbPlot.setTitle('Proportion de RL WBTB')

        self.vividDreamsPlot.clear()
        vivid_nb = len(list(filter(lambda dream: dream.clear == 4, self.dreams)))
        non_vivid_nb = len(list(filter(lambda dream: dream.clear != 4, self.dreams)))
        self.vividDreamsPlot.pie([vivid_nb, non_vivid_nb], colors=['orange', 'brown'], legend_labels=['VIVID', 'Pas VIVID'])
        self.vividDreamsPlot.setTitle('Proportion de rêves VIVID')

        normal_dreams_per_hour = self.dreams.filter(lambda dream: not dream.lucid).group_by_hour()
        lucid_dreams_per_hour = self.dreams.filter(lambda dream: dream.lucid).group_by_hour()
        hh_per_hour = self.hh.group_by_hour()
        vivid_per_hour = self.dreams.filter(lambda dream: dream.clear == 4).group_by_hour()

        width = 0.2
        hours = [f"{h}H" for h in range(24)]
        self.dreamsPerHourPlot.clear()
        self.dreamsPerHourPlot.bar(hours, [len(dreams) for dreams in normal_dreams_per_hour.values()], width=width, color='green', label='RN')
        self.dreamsPerHourPlot.bar(hours, [len(dreams) for dreams in lucid_dreams_per_hour.values()], width=width, space=width, color='blue', label='RL')
        self.dreamsPerHourPlot.bar(hours, [len(dreams) for dreams in vivid_per_hour.values()], width=width,
                                   space=width * 2, color='orange', label='VIVID')
        self.dreamsPerHourPlot.bar(hours, [len(dreams) for dreams in hh_per_hour.values()], width=width, space=width*3, color='purple', label='HH',
                                 legend=True, ylabel='Quantité')

    def update_as_page(self):
        nights = self.dreams.get_nights()
        for night in sorted(nights, key=lambda night: night.date, reverse=True):
            self.nightsLayout.addWidget(NightWidget(night, self.template))

    @staticmethod
    def get_dream_counts_values(dreams, time_intervals):
        values = []
        for interval in time_intervals:
            daily_value = 0
            for dream in dreams:
                if dream.date in interval:
                    daily_value += 1
            values.append(daily_value + values[-1]) if values else \
                values.append(daily_value)
        return values

    @staticmethod
    def get_dreams_collection_values_over_time(dreams, time_intervals, method):
        values = []
        dreams_collection = DreamsCollection()
        for interval in time_intervals:
            for dream in dreams:
                if dream.date in interval:
                    dreams_collection.append(dream)
            values.append(getattr(dreams_collection, method)())
        return values

    def format_mplWidget(self, mplWidget, title, x, y, xticks_nb):
        xticks = mplWidget.canvas.ax.get_xticks()
        mplWidget.canvas.ax.set_xticks(xticks[::len(xticks) // xticks_nb])
        if len(xticks) <= 8:
            mplWidget.canvas.ax.set_xticks(xticks[::2])
        mplWidget.canvas.ax.margins(x=0)
        mplWidget.canvas.ax.set_title(title)
        mplWidget.canvas.draw()

    def clearLayout(self, layout):
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

    def getTemplate(self):
        filename = QFileDialog.getOpenFileName(self, 'Choisissez un template', directory='./templates', filter="Templates (*.tp)")
        if filename[0]:
            template = Template.load(filename[0])
            self.selectedTemplateEdit.setText(filename[0])
            self.template = template
            self.update_as_page()

    def openNewTemplatePopup(self):
        self.newTemplatePopup = NewTemplatePopup(self.selectedTemplate)
        self.newTemplatePopup.show()
