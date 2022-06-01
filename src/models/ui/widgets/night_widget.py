from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget, QSpinBox, QSpacerItem

from models.ui.popups.dream_popup import DreamPopup
from models.ui.popups.post_popup import PostPopup


class NightWidget(QWidget):

    def __init__(self, night, parent=None):
        QWidget.__init__(self, parent)

        self.night = night

        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        self.label = QLabel(night.date.strftime("%d/%m/%y"))
        self.spacer = QSpacerItem(50, 0)
        self.button = QPushButton('Voir')
        self.button2 = QPushButton('Générer post')

        self.rn_label = QLabel('RN :')
        self.rn_count = QSpinBox()
        self.rn_count.setValue(len(night.dreams.filter(lambda dream: not dream.lucid)))

        self.rl_label = QLabel('RL :')
        self.rl_count = QSpinBox()
        self.rl_count.setValue(len(night.dreams.filter(lambda dream: dream.lucid)))

        self.hbl.addWidget(self.label)
        self.hbl.addItem(self.spacer)
        self.hbl.addWidget(self.rn_label)
        self.hbl.addWidget(self.rn_count)
        self.hbl.addWidget(self.rl_label)
        self.hbl.addWidget(self.rl_count)
        self.hbl.addWidget(self.button)
        self.hbl.addWidget(self.button2)

        dream_popups = [DreamPopup(dream) for dream in night.dreams]
        self.button.clicked.connect(lambda x: [dream_popup.show() for dream_popup in dream_popups])
        self.button2.clicked.connect(self.openPopup)

    def openPopup(self):
        self.postPopup = PostPopup(self.night)
        self.postPopup.show()
