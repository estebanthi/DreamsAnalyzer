from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget, QSpinBox, QSpacerItem

from copy import deepcopy


from models.ui.dream_popup import DreamPopup


class NightWidget(QWidget):

    def __init__(self, night, template, parent=None):
        QWidget.__init__(self, parent)
        print(parent)

        self.night = night
        self.template = template

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
        self.button2.clicked.connect(self.parse)

    def parse(self):
        print(self.template)
