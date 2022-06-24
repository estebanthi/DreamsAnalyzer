import yaml
from PyQt5.QtWidgets import QFileDialog


from models.ui.tabs.tab import Tab
from models.ui.widgets.dream_widget import DreamWidget
from models.ui.qt_utils import clearLayout


class GlobalConfigTab(Tab):

    def setupUi(self):
        conf = {'data_pathname': 'data'}
        with open('conf.yml', 'r') as file:
            conf = yaml.safe_load(file)

        self.mainWindow.dataPathnameEdit.setText(conf['data_pathname'])

    def connect(self):
        self.mainWindow.passwordDMInput.textChanged.connect(self.mainWindow.controller.save_password)
        self.mainWindow.emailDMInput.textChanged.connect(self.mainWindow.controller.save_email)
        self.mainWindow.autosyncCheckBox.stateChanged.connect(self.mainWindow.controller.handle_autosync_changed)
        self.mainWindow.modifyDataPathname.clicked.connect(self.changeDataPathname)
        self.mainWindow.controller.dataPathnameUpdatedSignal.connect(self.updateDataPathname)

    def updateData(self):
        pass

    def changeDataPathname(self):
        pathname = QFileDialog.getExistingDirectory()
        try:
            self.mainWindow.controller.chande_data_pathname(pathname)
        except Exception as e:
            print(e)

    def updateDataPathname(self, pathname):
        self.mainWindow.dataPathnameEdit.setText(pathname)
