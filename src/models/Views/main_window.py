from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon

from ui.main_window_ui import Ui_DreamsAnalyzer
from models.ui.tabs.home_tab import HomeTab
from models.ui.tabs.tags_tab import TagsTab
from models.ui.tabs.dreams_tab import DreamsTab
from models.ui.tabs.progress_tab import ProgressTab
from models.ui.tabs.statistics_tab import StatisticsTab
from models.ui.tabs.credentials_tab import CredentialsTab
from models.ui.tabs.anonyms_tab import AnonymsTab
from models.ui.tabs.forum_tab import ForumTab


class MainWindow(QMainWindow, Ui_DreamsAnalyzer):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.controller = controller
        self.tabs = [HomeTab(self), TagsTab(self), DreamsTab(self), ProgressTab(self), StatisticsTab(self),
                     AnonymsTab(self), CredentialsTab(self), ForumTab(self)]

    def postInit(self):
        if self.controller.get_templates():
            self.updateTemplates()
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

    def updateTemplates(self):
        for tab in self.tabs:
            tab.updateTemplates()

    """

    def update_as_page(self):
        nights = self.dreams.get_nights()
        for night in sorted(nights, key=lambda night: night.date, reverse=True):
            self.nightsLayout.addWidget(NightWidget(night))
"""