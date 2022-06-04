from models.ui.tabs.tab import Tab
from models.ui.popups.new_template_popup import NewTemplatePopup
from models.ui.qt_utils import clearLayout
from models.ui.widgets.night_widget import NightWidget


class ForumTab(Tab):

    def setupUi(self):
        pass

    def connect(self):
        self.mainWindow.editTemplateButton.clicked.connect(self.openEditTemplatePopup)
        self.mainWindow.newTemplateButton.clicked.connect(self.openNewTemplatePopup)

    def updateData(self):
        self.addNights()

    def updateTemplates(self):
        self.templates = self.mainWindow.controller.get_templates()

        self.mainWindow.templatesComboBox.clear()
        self.mainWindow.templatesComboBox.addItems([template.name for template in self.templates])

        if self.mainWindow.controller.model.data:
            self.addNights()

    def openEditTemplatePopup(self):
        popup = NewTemplatePopup(self.mainWindow.controller, template=self.templates[self.mainWindow.templatesComboBox.currentIndex()], mode='EDIT')
        popup.show()

    def openNewTemplatePopup(self):
        popup = NewTemplatePopup(self.mainWindow.controller, mode='NEW')
        popup.show()

    def addNights(self):
        clearLayout(self.mainWindow.nightsLayout)
        templates = self.mainWindow.controller.get_templates()
        index = self.mainWindow.templatesComboBox.currentIndex()
        nights = self.mainWindow.controller.model.data.dreams.get_nights()
        for night in sorted(nights, key=lambda night: night.date, reverse=True):
            self.mainWindow.nightsLayout.addWidget(NightWidget(self.mainWindow.controller, night, templates, index))