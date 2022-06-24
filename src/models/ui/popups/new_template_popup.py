from PyQt5.QtWidgets import QMainWindow, QFileDialog
import os
import pickle
import yaml

from models.template import Template


from ui.new_template_popup import Ui_MainWindow


class NewTemplatePopup(QMainWindow, Ui_MainWindow):

    def __init__(self, controller, template=None, mode='NEW', parent=None):
        super().__init__(parent)
        self.setupUi(self)

        conf = {'data_pathname': 'data'}
        with open(f"{os.environ['ProgramFiles']}\\Dreams Analyzer\\conf.yml", 'r') as file:
            conf = yaml.safe_load(file)
        self.data_pathname = conf['data_pathname']

        self.template = template
        self.controller = controller

        self.saveTemplateButton.clicked.connect(self.saveTemplate)
        self.deleteTemplateButton.clicked.connect(self.deleteTemplate)

        self.typeButton.clicked.connect(lambda x: self.insertTemplateText('type'))
        self.titleButton.clicked.connect(lambda x: self.insertTemplateText('title'))
        self.tagsButton.clicked.connect(lambda x: self.insertTemplateText('tags'))
        self.timeButton.clicked.connect(lambda x: self.insertTemplateText('time'))
        self.contentButton.clicked.connect(lambda x: self.insertTemplateText('content'))
        self.nbButton.clicked.connect(lambda x: self.insertTemplateText('nb'))
        self.metaButton.clicked.connect(lambda x: self.insertTemplateText('json_name'))

        if mode == 'EDIT':
            if self.template:
                self.templateNameEdit.setText(template.name)
                self.newTemplateTextEdit.setText(template.content)

        if mode == 'NEW':
            filenames = os.listdir(f'{self.data_pathname}/templates')
            for i in range(len(filenames)+1):
                if f"{i}.tp" not in filenames:
                    self.template = Template(f"{i}.tp")
                print(i)

    def deleteTemplate(self):
        self.controller.delete_template(self.template)
        self.destroy()

    def saveTemplate(self):
        self.template = Template(self.template.filename, self.templateNameEdit.text(), self.newTemplateTextEdit.toPlainText())
        self.controller.save_template(self.template)
        self.destroy()

    def insertTemplateText(self, text):
        self.newTemplateTextEdit.insertPlainText('{{'+text+'}}')
