from models.ui.tabs.tab import Tab
from models.ui.popups.new_template_popup import NewTemplatePopup
from models.ui.qt_utils import clearLayout


class ForumTab(Tab):

    def setupUi(self):
        pass

    def connect(self):
        self.mainWindow.editTemplateButton.clicked.connect(self.openEditTemplatePopup)
        self.mainWindow.newTemplateButton.clicked.connect(self.openNewTemplatePopup)

    def updateTemplates(self):
        self.templates = self.mainWindow.controller.get_templates()

        self.mainWindow.templatesComboBox.clear()
        self.mainWindow.templatesComboBox.addItems([template.name for template in self.templates])

    def openEditTemplatePopup(self):
        popup = NewTemplatePopup(self.mainWindow.controller, template=self.templates[self.mainWindow.templatesComboBox.currentIndex()], mode='EDIT')
        popup.show()

    def openNewTemplatePopup(self):
        popup = NewTemplatePopup(self.mainWindow.controller, mode='NEW')
        popup.show()