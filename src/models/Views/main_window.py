from PyQt5.QtWidgets import QMainWindow

from ui.main_window_ui import Ui_DreamsAnalyzer
from models.ui.tabs.home_tab import HomeTab
from models.ui.tabs.tags_tab import TagsTab
from models.ui.tabs.dreams_tab import DreamsTab
from models.ui.tabs.progress_tab import ProgressTab
from models.ui.tabs.statistics_tab import StatisticsTab
from models.ui.tabs.credentials_tab import CredentialsTab
from models.ui.tabs.anonyms_tab import AnonymsTab


class MainWindow(QMainWindow, Ui_DreamsAnalyzer):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.controller = controller
        self.tabs = [HomeTab(self), TagsTab(self), DreamsTab(self), ProgressTab(self), StatisticsTab(self),
                     AnonymsTab(self), CredentialsTab(self)]

    def postInit(self):
        if self.controller.model.data:
            self.updateData()
        if self.controller.get_anonyms():
            self.updateAnonyms()
        self.passwordDMInput.setText(self.controller.model.config.credentials['password'])
        self.emailDMInput.setText(self.controller.model.config.credentials['email'])

    def updateData(self):
        for tab in self.tabs:
            tab.updateData()

    def updateAnonyms(self):
        for tab in self.tabs:
            tab.updateAnonyms()

    """

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

    def get_widget_index(self, widget, layout):
        for i in range(layout.count()):
            if layout.itemAt(i).widget() == widget:
                return i
        return -1"""