from models.ui.qt_utils import clearLayout
from models.ui.tabs.tab import Tab
from models.dreams_analyzer import DreamsAnalyzer
from mplwidget import MplWidget


class ProgressTab(Tab):

    def setupUi(self):
        self.mainWindow.resolutionSelect.addItems(['Jour', 'Semaine', 'Mois'])

        self.mplWidgets = [
            ['Total rêves', 'count_dreams', 'black'],
            ['Total rêves lucides', 'count_lucid_dreams', 'blue'],
            ['Rêves par nuit', 'get_average_dreams_per_nights', 'black'],
            ['Taux de rêves lucides (en %)', 'get_lucid_dreams_rate', 'blue'],
            ['Longueur de rêve moyenne (en mots)', 'get_average_dreams_length', 'green']
        ]

    def connect(self):
        self.mainWindow.resolutionSelect.currentTextChanged.connect(self.mainWindow.controller.handle_resolution_changed)

    def updateData(self):
        clearLayout(self.mainWindow.dreamsPlotLayout)
        clearLayout(self.mainWindow.metaPlotLayout)

        resolutionText = self.mainWindow.resolutionSelect.currentText()
        resolution = self.mainWindow.controller.parse_resolution(resolutionText)
        x, timeranges = self.mainWindow.controller.get_plot_params(resolution)

        self.addMplWidgets(self.mplWidgets, resolution, self.mainWindow.dreamsPlotLayout)
        self.addMetasMplWidgets(resolution, self.mainWindow.metaPlotLayout)

    def addMplWidgets(self, widgets, resolution, layout):
        for widget in widgets:
            self.addMplWidget(widget, resolution, layout)

    def addMplWidget(self, mplWidget, resolution, layout):
        x, timeranges = self.mainWindow.controller.get_plot_params(resolution)
        values = self.mainWindow.controller.get_values_over_time(resolution, mplWidget[1])

        widget = MplWidget()
        widget.setFixedSize(350, 350)


        widget.clear()
        widget.plot(x, values, mplWidget[2])
        widget.format(mplWidget[0], x, values, 3)

        layout.addWidget(widget)

    def addMetasMplWidgets(self, resolution, layout):
        metas = self.mainWindow.controller.get_metas_over_time(resolution)
        for name, values in metas.items():
            self.addMetaMplWidget(name, values, resolution, layout)

    def addMetaMplWidget(self, name, values, resolution, layout):
        x, timeranges = self.mainWindow.controller.get_plot_params(resolution)

        widget = MplWidget()
        widget.setFixedSize(350, 350)

        widget.clear()
        widget.plot(x, values, 'red')
        widget.format(f"{name} (moyenne)", x, values, 3)

        layout.addWidget(widget)
