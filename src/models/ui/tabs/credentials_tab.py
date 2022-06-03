from models.ui.tabs.tab import Tab
from models.ui.widgets.dream_widget import DreamWidget
from models.ui.qt_utils import clearLayout


class CredentialsTab(Tab):

    def setupUi(self):
        pass

    def connect(self):
        self.mainWindow.passwordDMInput.textChanged.connect(self.mainWindow.controller.save_password)
        self.mainWindow.emailDMInput.textChanged.connect(self.mainWindow.controller.save_email)

    def updateData(self):
        pass