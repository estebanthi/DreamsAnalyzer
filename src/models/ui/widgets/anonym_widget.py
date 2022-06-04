from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit


class AnonymWidget(QWidget):

    def __init__(self, controller, id_, real='', anonym='', parent=None):
        QWidget.__init__(self, parent)
        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        self.real = QLineEdit()
        self.real.setText(real)

        self.anonym = QLineEdit()
        self.anonym.setText(anonym)

        self.id_ = id_

        self.button = QPushButton('Supprimer')

        self.hbl.addWidget(self.real)
        self.hbl.addWidget(self.anonym)
        self.hbl.addWidget(self.button)

        self.button.clicked.connect(lambda x: controller.delete_anonym(self.id_))
        self.real.textChanged.connect(lambda x: controller.update_real(self.id_, self.real.text()))
        self.anonym.textChanged.connect(lambda x: controller.update_anonym(self.id_, self.anonym.text()))
