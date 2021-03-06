from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget


from models.ui.popups.dream_popup import DreamPopup


class DreamWidget(QWidget):

    def __init__(self, dream, parent=None):
        QWidget.__init__(self, parent)
        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        self.dream = dream

        self.label = QLabel(dream.title) if dream.title else QLabel(str(dream.date))
        self.button = QPushButton('Voir')

        self.hbl.addWidget(self.label)
        self.hbl.addWidget(self.button)

        dream_popup = DreamPopup(dream)
        self.button.clicked.connect(lambda x: dream_popup.show())
