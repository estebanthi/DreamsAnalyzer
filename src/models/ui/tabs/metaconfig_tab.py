from PyQt5.QtWidgets import QLabel, QLineEdit


from models.ui.qt_utils import clearLayout
from models.ui.tabs.tab import Tab
from models.ui.widgets.metaconfig_widget import MetaconfigWidget


class MetaconfigTab(Tab):

    def setupUi(self):
        pass

    def connect(self):
        self.mainWindow.addMetaButton.clicked.connect(self.addMeta)

    def updateData(self):
        pass

    def updateMetas(self):
        clearLayout(self.mainWindow.metadatasLayout)
        metas = self.mainWindow.controller.get_metas()

        for meta in metas:
            widget = MetaconfigWidget(self.mainWindow.controller, meta)
            self.mainWindow.metadatasLayout.addWidget(widget)

    def addMeta(self):
        self.mainWindow.controller.add_meta()
