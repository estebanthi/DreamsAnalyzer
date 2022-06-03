from PyQt5.QtWidgets import QMainWindow

from ui.main_window_ui import Ui_DreamsAnalyzer
from models.ui.tabs.home_tab import HomeTab
from models.ui.tabs.tags_tab import TagsTab
from models.ui.tabs.dreams_tab import DreamsTab
from models.ui.tabs.progress_tab import ProgressTab
from models.ui.tabs.statistics_tab import StatisticsTab


class MainWindow(QMainWindow, Ui_DreamsAnalyzer):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.controller = controller
        self.tabs = [HomeTab(self), TagsTab(self), DreamsTab(self), ProgressTab(self), StatisticsTab(self)]

    def postInit(self):
        if self.controller.model.data:
            self.updateData()

    def updateData(self):
        for tab in self.tabs:
            tab.updateData()

    def connect(self):
        self.importJSONFileButton.clicked.connect(self.getFile)
        self.updateButton.clicked.connect(self.onUpdateButtonClick)
        self.resetButton.clicked.connect(self._update)
        self.updateButton2.clicked.connect(self.onUpdateButtonClick)
        self.loadTemplateButton.clicked.connect(self.getTemplate)
        self.newTemplateButton.clicked.connect(self.openNewTemplatePopup)
        self.saveAnonymsButton.clicked.connect(self.saveAnonyms)
        self.addAnonymButton.clicked.connect(self.addAnonym)


    """

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
            self.nightsLayout.addWidget(NightWidget(night))

    def update_anonyms_page(self):
        anonymisator = Anonymisator()
        records = anonymisator.get_records()
        for record in records:
            for real, anonym in record.items():
                anonym_widget = AnonymWidget(real, anonym)
                self.anonymLayout_2.addWidget(anonym_widget)


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

        self.dreams = []
        self.lucid_dreams = []
        self.normal_dreams = []
        self.hh = []

    def getFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Choisissez un fichier')[0]
        config = Config()
        if filename:
            shutil.copy(filename, config['dream_manager_data_pathname'])
            self.loadDreamManagerData()
            self._update()

    def getTemplate(self):
        config = Config()
        temp_template_pathname = config['temp_template_pathname']
        templates_directory = config['templates_directory']
        filename = QFileDialog.getOpenFileName(self, 'Choisissez un template', directory=templates_directory, filter="Templates (*.tp)")
        if filename[0]:
            self.selectedTemplateEdit.setText(filename[0])
            shutil.copy(filename[0], temp_template_pathname)
            self.update_as_page()

    def openNewTemplatePopup(self):
        self.newTemplatePopup = NewTemplatePopup(self.selectedTemplate)
        self.newTemplatePopup.show()

    def saveAnonyms(self):
        anonymisator = Anonymisator()

        records = [self.anonymLayout_2.itemAt(i).widget().get_record() for i in range(self.anonymLayout_2.count())]
        anonymisator.save_records(records)

    def addAnonym(self):
        anonym_widget = AnonymWidget()
        self.anonymLayout_2.addWidget(anonym_widget)

    def get_widget_index(self, widget, layout):
        for i in range(layout.count()):
            if layout.itemAt(i).widget() == widget:
                return i
        return -1"""