import sys
import time

from PyQt5.QtWidgets import QApplication

from models.config import Config


from models.ui.main_window import MainWindow


def run():
    Config.initial_setup()
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()


