from models.ui.tabs.tab import Tab
from models.ui.widgets.dream_widget import DreamWidget
from models.qt_utils import clearLayout


class DreamsTab(Tab):

    def setupUi(self):
        pass

    def connect(self):
        pass

    def updateData(self):
        clearLayout(self.mainWindow.dreamsLayoutVertical)
        for dream in sorted(self.mainWindow.controller.model.data.dreams, key=lambda dream: dream.date, reverse=True):
            self.mainWindow.dreamsLayoutVertical.addWidget(DreamWidget(dream))
