from models.ui.tabs.tab import Tab
from models.ui.widgets.anonym_widget import AnonymWidget
from models.ui.qt_utils import clearLayout


class AnonymsTab(Tab):

    def setupUi(self):
        pass

    def connect(self):
        self.mainWindow.addAnonymButton.clicked.connect(self.addAnonym)

    def updateData(self):
        pass

    def updateAnonyms(self):
        anonyms = self.mainWindow.controller.get_anonyms()

        clearLayout(self.mainWindow.anonymLayout_2)

        for anonym in anonyms:
            widget = AnonymWidget(self.mainWindow.controller, anonym['id_'], anonym['real'], anonym['anonym'])
            self.mainWindow.anonymLayout_2.addWidget(widget)

    def addAnonym(self):
        _id = self.mainWindow.controller.add_anonym()
        anonym_widget = AnonymWidget(self.mainWindow.controller, _id, '', '')
        self.mainWindow.anonymLayout_2.addWidget(anonym_widget)
