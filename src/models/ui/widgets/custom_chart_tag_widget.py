from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit, QLabel, QComboBox, QColorDialog, QCompleter
from PyQt5.QtGui import QColor
import PyQt5.QtCore
import webcolors
from sklearn.metrics import mean_squared_error
import numpy as np
import random


from models.dreams_analyzer import DreamsAnalyzer


class CustomChartTagWidget(QWidget):

    def __init__(self, popup, controller, tag=None, parent=None):
        QWidget.__init__(self, parent)
        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        self.popup = popup

        self.colorDialog = QColorDialog()

        self.tag = tag

        self.label = QLineEdit()
        self.label.textChanged.connect(self.popup.preview)

        dreams_analyzer = DreamsAnalyzer(controller.model.data.dreams)
        tags_counter = dreams_analyzer.get_tags_counter()
        completer = QCompleter([tag[0].label for tag in tags_counter])
        completer.setCaseSensitivity(PyQt5.QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.label.setCompleter(completer)


        self.comboBox = QComboBox()
        self.comboBox.addItems(['IN', 'NOT IN'])
        self.comboBox.currentTextChanged.connect(self.popup.preview)

        self.filterBox = QComboBox()
        self.filterBox.addItems(['Tout', 'Lucides', 'Normaux'])
        self.filterBox.currentTextChanged.connect(self.popup.preview)

        self.color_text = QLineEdit()
        self.color_text.setReadOnly(True)
        self.color_text.setText("#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]))

        self.edit_color_button = QPushButton('Modifier la couleur')
        self.delete_button = QPushButton('Supprimer')

        self.hbl.addWidget(self.label)
        self.hbl.addWidget(self.comboBox)
        self.hbl.addWidget(self.filterBox)
        self.hbl.addWidget(self.color_text)
        self.hbl.addWidget(self.edit_color_button)
        self.hbl.addWidget(self.delete_button)

        if tag:
            self.setup()

        self.edit_color_button.clicked.connect(self.openColorDialog)
        self.delete_button.clicked.connect(self.delete)

    def setup(self):
        tag = self.tag

        self.label.setText(tag[0])
        self.comboBox.setCurrentIndex(0 if tag[1] == 'IN' else 1)

        color = tag[2]
        self.color_text.setText(color)

        if tag[3]:
            self.filterBox.setCurrentIndex(1 if tag[3]['lucid'] else 2)

    def openColorDialog(self):
        color = self.colorDialog.getColor()
        color_name = color.name()
        self.color_text.setText(color_name)
        self.popup.preview()

    def mse(self, actual, predicted):
        actual = np.array(actual)
        predicted = np.array(predicted)
        differences = np.subtract(actual, predicted)
        squared_differences = np.square(differences)
        return squared_differences.mean()

    def get_tag(self):
        return [self.label.text(), self.comboBox.currentText(), self.color_text.text(), self.get_filter()]

    def get_filter(self):
        filter = {}
        if self.filterBox.currentText() == 'Lucides':
            filter = {'lucid': True}
        if self.filterBox.currentText() == 'Normaux':
            filter = {'lucid': False}
        return filter

    def delete(self):
        self.setParent(None)
        self.popup.preview()