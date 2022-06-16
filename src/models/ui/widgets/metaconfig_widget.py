from PyQt5.QtWidgets import QWidget, QLabel, QDoubleSpinBox, QLineEdit, QPushButton, QComboBox
from PyQt5.QtWidgets import QHBoxLayout


from models.enums import MetaType


class MetaconfigWidget(QWidget):

    def __init__(self, controller, meta=None, parent=None):
        QWidget.__init__(self, parent)

        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        self.name = QLineEdit()
        self.json_name = QLineEdit()
        self.delete_button = QPushButton('Supprimer')

        self.combo = QComboBox()
        self.combo.addItems(['NUMERIC', 'STR'])

        self.hbl.addWidget(self.name)
        self.hbl.addWidget(self.json_name)
        self.hbl.addWidget(self.combo)
        self.hbl.addWidget(self.delete_button)

        self.controller = controller
        self.meta = meta
        if self.meta:
            self.setup()

        self.name.textChanged.connect(self.updateMetaName)
        self.json_name.textChanged.connect(self.updateMetaJSONName)
        self.combo.currentTextChanged.connect(self.updateMetaType)
        self.delete_button.clicked.connect(self.delete)

    def setup(self):
        self.name.setText(self.meta.name)
        self.json_name.setText(self.meta.json_name)
        self.combo.setCurrentText('NUMERIC' if self.meta.type_ == MetaType.NUMERIC else "STR")

    def updateMetaName(self, new_name):
        self.controller.update_meta('name', self.meta.id_, new_name)

    def updateMetaJSONName(self, new_name):
        self.controller.update_meta('json_name', self.meta.id_, new_name)

    def updateMetaType(self, type_):
        if type_ == 'NUMERIC':
            new_type = MetaType.NUMERIC
        else:
            new_type = MetaType.STRING

        self.controller.update_meta('type_', self.meta.id_, new_type)

    def delete(self):
        self.controller.delete_meta(self.meta.id_)
