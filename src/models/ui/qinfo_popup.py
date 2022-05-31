from PyQt5.QtWidgets import QMessageBox


class QInfoPopup:

    def __init__(self, text=''):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Information")
        msg.exec_()
