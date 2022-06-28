from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit
import PyQt5.QtCore


class SpecialTextWidget(QWidget):

    deleted = PyQt5.QtCore.pyqtSignal(int)

    def __init__(self, popup, id_, text='', bbcode='', parent=None):
        QWidget.__init__(self, parent)

        self.id_ = id_
        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        self.textEdit = QLineEdit()
        self.textEdit.setText(text)

        self.bbcodeEdit = QLineEdit()
        self.bbcodeEdit.setText(bbcode)

        self.popup = popup
        self.button = QPushButton('Supprimer')
        self.button.clicked.connect(lambda x: self.popup.deleteSpecialText(self.id_))

        self.hbl.addWidget(self.textEdit)
        self.hbl.addWidget(self.bbcodeEdit)
        self.hbl.addWidget(self.button)
