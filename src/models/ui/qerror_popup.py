from PyQt5.QtWidgets import QMessageBox


class QErrorPopup:

    def __init__(self, text=''):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle("Erreur")
        msg.exec_()
