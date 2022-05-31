import shutil
import datetime as dt

from PyQt5.QtWidgets import QFileDialog

from models.ui.tabs.tab import Tab


class HomeTab(Tab):

    def setupUi(self):
        self.mainWindow.dreamTypeSelect.addItems(['Tout', 'Lucides', 'Normaux'])

    def connect(self):
        self.mainWindow.syncButton.clicked.connect(self.mainWindow.controller.sync_data)
        self.mainWindow.importJSONFileButton.clicked.connect(self.getFile)
        self.mainWindow.updateButton.clicked.connect(self.filter_dreams)
        self.mainWindow.resetButton.clicked.connect(self.mainWindow.controller.reset_filter)

    def updateData(self):
        self.mainWindow.lastLoadedDataDateTimeEdit.setDateTime(self.mainWindow.controller.model.data.date)
        self.updateDates()
        self.mainWindow.totalDreamsCounter.setValue(len(self.mainWindow.controller.model.data.dreams))
        self.mainWindow.normalDreamsCounter.setValue(
            len(self.mainWindow.controller.model.data.dreams.filter(lambda dream: not dream.lucid)))
        self.mainWindow.lucidDreamsCounter.setValue(
            len(self.mainWindow.controller.model.data.dreams.filter(lambda dream: dream.lucid)))
        self.mainWindow.hhCounter.setValue(
            len(self.mainWindow.controller.model.data.hhs))
        
    def updateDates(self):
        start = self.mainWindow.controller.model.data.dreams[0].date
        end = self.mainWindow.controller.model.data.dreams[-1].date + dt.timedelta(days=1)

        self.mainWindow.startDate.setMinimumDate(start)
        self.mainWindow.endDate.setMaximumDate(end)
        self.mainWindow.endDate.setMinimumDate(start)
        self.mainWindow.startDate.setMaximumDate(end)

        self.mainWindow.startDate.setDate(start)
        self.mainWindow.endDate.setDate(end)

    def getFile(self):
        filename = QFileDialog.getOpenFileName(self.mainWindow, 'Choisissez un fichier')[0]
        if filename:
            shutil.copy(filename, 'data/data.json')
            self.mainWindow.controller.load_last_data()

    def filter_dreams(self):
        self.mainWindow.controller.filter_dreams(self.mainWindow.startDate.date(), self.mainWindow.endDate.date(),
                                                 self.mainWindow.dreamTypeSelect.currentText())
