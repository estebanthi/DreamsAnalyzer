from PyQt5.QtWidgets import QWidget, QLabel, QDoubleSpinBox, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout


class MetaWidget(QWidget):

    def __init__(self, name, value, changeFont=False, parent=None):
        QWidget.__init__(self, parent)

        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        if type(value) is float:
            self.input = QDoubleSpinBox()
            self.input.setMinimum(-999999)
            self.input.setMaximum(999999)
            self.input.setValue(value)

        if type(value) is int:
            self.input = QDoubleSpinBox()
            self.input.setMinimum(-999999)
            self.input.setMaximum(999999)
            self.input.setValue(value)

        if type(value) is str:
            self.input = QLineEdit()
            self.input.setText(value)

        self.input.setReadOnly(True)
        self.label = QLabel(f"{name} :")
        if changeFont:
            font = self.input.font()
            font.setPointSize(12)
            self.input.setFont(font)
            self.label.setFont(font)

        self.hbl.addWidget(self.label)
        self.hbl.addWidget(self.input)
