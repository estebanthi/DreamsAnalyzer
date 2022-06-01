from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit


from models.anonymisator import Anonymisator


class AnonymWidget(QWidget):

    def __init__(self, real=None, anonym=None, parent=None):
        QWidget.__init__(self, parent)
        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        self.real = QLineEdit()
        self.real.setText(real)

        self.anonym = QLineEdit()
        self.anonym.setText(anonym)

        self.button = QPushButton('Supprimer')

        self.hbl.addWidget(self.real)
        self.hbl.addWidget(self.anonym)
        self.hbl.addWidget(self.button)

        self.button.clicked.connect(self.delete)

    def delete(self):
        anonymisator = Anonymisator()
        records = anonymisator.get_records()
        record_index = self.find_record(records)
        if record_index > -1:
            del(records[(self.find_record(records))])
        anonymisator.save_records(records)
        self.deleteLater()

    def get_record(self):
        return {self.real.text(): self.anonym.text()}

    def find_record(self, records):
        for i, record in enumerate(records):
            for real, fake in record.items():
                if real == self.real.text() and fake == self.anonym.text():
                    return i
        return -1