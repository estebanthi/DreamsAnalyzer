import sys


from PyQt5.QtWidgets import QApplication


from models.ui.main_window import MainWindow


def run():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()


