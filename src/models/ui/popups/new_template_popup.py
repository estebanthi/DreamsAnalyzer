from PyQt5.QtWidgets import QMainWindow, QFileDialog, QHBoxLayout, QLineEdit, QPushButton
import os
import pickle
import yaml
import random

from models.template import Template
from models.ui.widgets.special_text_widget import SpecialTextWidget
from models.ui.qt_utils import clearLayout


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
        self.specialTexts = []

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
        self.addSpecialTextButton.clicked.connect(self.addSpecialText)

        if mode == 'EDIT':
            if self.template:
                self.templateNameEdit.setText(template.name)
                self.newTemplateTextEdit.setText(template.content)
                self.RLColorEdit.setText(template.lucid_dreams_color)
                self.RNColorEdit.setText(template.normal_dreams_color)
                self.specialTexts = self.template.special_texts

        if mode == 'NEW':
            filenames = os.listdir(f'{self.data_pathname}/templates')
            for i in range(len(filenames)+1):
                if f"{i}.tp" not in filenames:
                    self.template = Template(f"{i}.tp")
            self.RLColorEdit.setText('blue')
            self.RNColorEdit.setText('green')

        self.update_()

    def update_(self):
        clearLayout(self.specialTextsLayout)
        for special_text in self.specialTexts:
            widget = SpecialTextWidget(special_text['id_'], special_text['text'], special_text['bbcode'])
            widget.button.clicked.connect(lambda x: self.deleteSpecialText(widget.id_))
            self.specialTextsLayout.addWidget(widget)

    def deleteTemplate(self):
        self.controller.delete_template(self.template)
        self.destroy()

    def saveTemplate(self):
        specialTexts = []

        for index in range(self.specialTextsLayout.count()):
            widget = self.specialTextsLayout.itemAt(index).widget()
            specialTexts.append({'text': widget.textEdit.text(), 'bbcode': widget.bbcodeEdit.text(), 'id_': widget.id_})

        self.template = Template(self.template.filename, self.templateNameEdit.text(),
                                 self.newTemplateTextEdit.toPlainText(), self.RLColorEdit.text(), self.RNColorEdit.text(),
                                 specialTexts)

        self.controller.save_template(self.template)
        self.destroy()

    def insertTemplateText(self, text):
        self.newTemplateTextEdit.insertPlainText('{{'+text+'}}')

    def addSpecialText(self):
        widget = SpecialTextWidget(random.randint(0, 999999999999))
        widget.button.clicked.connect(lambda x: self.deleteSpecialText(widget.id_))
        self.specialTextsLayout.addWidget(widget)
        self.specialTexts.append({'text': '', 'bbcode': '', 'id_': widget.id_})

    def deleteSpecialText(self, id_):
        for index, specialText in enumerate(self.specialTexts):
            if specialText['id_'] == id_:
                del(self.specialTexts[index])
        self.update_()
