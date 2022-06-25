from PyQt5.QtWidgets import QLabel, QLineEdit, QSpinBox


from models.ui.qt_utils import clearLayout
from models.ui.tabs.tab import Tab
from models.dreams_analyzer import DreamsAnalyzer


class TagsTab(Tab):

    def setupUi(self):
        pass

    def connect(self):
        pass

    def updateData(self):
        clearLayout(self.mainWindow.tagsCounters)
        clearLayout(self.mainWindow.categoriesCounters)

        self.addTags()
        self.addCategories()

    def addTags(self):
        dreams_analyzer = DreamsAnalyzer(self.mainWindow.controller.model.data.dreams)
        tags_counter = dreams_analyzer.get_tags_counter()
        for tag, count in tags_counter:
            qlabel = QLabel(tag.label)
            qline = QSpinBox()
            qline.setMaximum(999999)
            qline.setValue(count)
            qline.setReadOnly(True)
            self.mainWindow.tagsCounters.addRow(qlabel, qline)

    def addCategories(self):
        dreams_analyzer = DreamsAnalyzer(self.mainWindow.controller.model.data.dreams)
        categories_counter = dreams_analyzer.get_categories_counter()
        for category, count in categories_counter:
            qlabel = QLabel(category.label) if category else QLabel("Sans catégorie")
            qline = QSpinBox()
            qline.setMaximum(9999999)
            qline.setValue(count)
            qline.setReadOnly(True)
            self.mainWindow.categoriesCounters.addRow(qlabel, qline)
