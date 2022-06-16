from models.ui.tabs.tab import Tab
from models.ui.qt_utils import clearLayout
from models.ui.widgets.custom_chart_widget import CustomChartWidget
from models.ui.popups.custom_chart_popup import CustomChartPopup


class CustomChartsTab(Tab):

    def setupUi(self):
        pass

    def connect(self):
        self.mainWindow.addGraphButton.clicked.connect(self.openNewChartPopup)

    def updateData(self):
        pass

    def updateCharts(self):
        clearLayout(self.mainWindow.customChartsLayout)
        charts = self.mainWindow.controller.get_other_plots()

        for chart in charts:
            self.mainWindow.customChartsLayout.addWidget(CustomChartWidget(self.mainWindow.controller, chart))

    def openNewChartPopup(self):
        self.mainWindow.controller.open_edit_chart_popup(None)
