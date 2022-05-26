from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QMainWindow, QFileDialog, QApplication
from PyQt5.QtCore import QMimeData, QUrl
from ui.post_popup import Ui_MainWindow

from models.template import Template


class PostPopup(QMainWindow, Ui_MainWindow):

    def __init__(self, night, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.night = night
        self.dateLabel.setText(str(night.date))

        self.generateButton.clicked.connect(self.generate)
        self.resetButton.clicked.connect(lambda x: self.postEdit.setText(""))
        self.copyButton.clicked.connect(self.copy_to_clip)

        self.generate()


    def generate(self):
        template = Template.load('./templates/temp.tp')

        nbs = []
        rn_nb = 0
        rl_nb = 0
        for dream in self.night.dreams:
            if dream.lucid:
                rl_nb += 1
                nbs.append(rl_nb)
            else:
                rn_nb += 1
                nbs.append(rn_nb)

        content = [template.parse(dream, nb) for nb, dream in enumerate(self.night.dreams)]
        self.postEdit.setText("\n\n\n".join(content))

    def copy_to_clip(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.postEdit.toPlainText())
