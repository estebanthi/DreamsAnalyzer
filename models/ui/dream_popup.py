from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QMainWindow
from PyQt5.QtCore import Qt


from ui.dream_popup import Ui_MainWindow


class DreamPopup(QMainWindow, Ui_MainWindow):

    def __init__(self, dream, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.dream = dream
        self.titleInput.setText(dream.title)
        self.rlCheckbox.setChecked(dream.lucid)
        self.lucidityInput.setValue(dream.lucidity)
        self.clearInput.setValue(dream.clear)
        self.moodInput.setValue(dream.mood)
        self.hourEdit.setText(f'{str(dream.date.hour)}H{str(dream.date.minute)}')

        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        self.tagsHorizontalLayout.addWidget(line)

        tags_labels = [tag.label for tag in dream.tags]
        for label in tags_labels:
            labelWidget = QLabel(label)
            labelWidget.setAlignment(Qt.AlignCenter)
            self.tagsHorizontalLayout.addWidget(labelWidget)

            line = QFrame()
            line.setFrameShape(QFrame.VLine)
            line.setFrameShadow(QFrame.Sunken)
            self.tagsHorizontalLayout.addWidget(line)

        self.textEdit.setText(dream.content)
