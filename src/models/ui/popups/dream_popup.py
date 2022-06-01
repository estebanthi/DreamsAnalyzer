from PyQt5.QtWidgets import QLabel, QFrame, QMainWindow
from PyQt5.QtCore import Qt


from ui.dream_popup import Ui_MainWindow
from models.ui.widgets.meta_widget import MetaWidget


class DreamPopup(QMainWindow, Ui_MainWindow):

    def __init__(self, dream, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.dream = dream
        self.titleInput.setText(dream.title)
        self.titleInput.setReadOnly(True)
        self.rlCheckbox.setChecked(dream.lucid)
        self.rlCheckbox.setCheckable(False)
        self.hourEdit.setText(f'{str(dream.date.hour)}H{str(dream.date.minute)}')
        self.hourEdit.setReadOnly(True)

        self.addMetas()

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
        self.textEdit.setReadOnly(True)

    def addMetas(self):
        for meta in self.dream.metas:
            self.mainLayout.addWidget(MetaWidget(meta.name, meta.value, True))

