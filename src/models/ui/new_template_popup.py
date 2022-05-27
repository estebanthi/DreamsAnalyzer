from PyQt5.QtWidgets import QMainWindow, QFileDialog

from models.template import Template


from ui.new_template_popup import Ui_MainWindow


class NewTemplatePopup(QMainWindow, Ui_MainWindow):

    def __init__(self, template=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.saveTemplateButton.clicked.connect(self.saveTemplate)

        self.typeButton.clicked.connect(lambda x: self.insertTemplateText('type'))
        self.titleButton.clicked.connect(lambda x: self.insertTemplateText('title'))
        self.clearButton.clicked.connect(lambda x: self.insertTemplateText('clear'))
        self.moodButton.clicked.connect(lambda x: self.insertTemplateText('mood'))
        self.lucidityButton.clicked.connect(lambda x: self.insertTemplateText('lucidity'))
        self.tagsButton.clicked.connect(lambda x: self.insertTemplateText('tags'))
        self.timeButton.clicked.connect(lambda x: self.insertTemplateText('time'))
        self.contentButton.clicked.connect(lambda x: self.insertTemplateText('content'))
        self.nbButton.clicked.connect(lambda x: self.insertTemplateText('nb'))


    def saveTemplate(self):
        fileDialog = QFileDialog()
        pathname = fileDialog.getSaveFileName(directory='./templates', filter="Templates (*.tp)")[0]

        if pathname:
            template = Template(self.newTemplateTextEdit.toPlainText())
            template.save(pathname)

        self.close()

    def insertTemplateText(self, text):
        self.newTemplateTextEdit.insertPlainText('{{'+text+'}}')