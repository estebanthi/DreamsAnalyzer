from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.post_popup import Ui_MainWindow

from models.template import Template
from models.config import Config


class PostPopup(QMainWindow, Ui_MainWindow):

    def __init__(self, template, night, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.template = template
        self.night = night
        self.dateLabel.setText(str(night.date))

        self.generateButton.clicked.connect(self.generate)
        self.resetButton.clicked.connect(lambda x: self.postEdit.setText(""))
        self.copyButton.clicked.connect(self.copy_to_clip)

        self.generate()


    def generate(self):
        template = self.template

        nbs = []
        rn_nb = 0
        rl_nb = 0
        for dream in self.night:
            if dream.lucid:
                rl_nb += 1
                nbs.append(rl_nb)
            else:
                rn_nb += 1
                nbs.append(rn_nb)

        content = []
        for dream, nb in zip(self.night, nbs):
            content.append(template.parse(dream, nb))
        self.postEdit.setText("\n\n\n".join(content))

    def copy_to_clip(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.postEdit.toPlainText())
