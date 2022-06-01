import sys
import unittest


from PyQt5.QtWidgets import QApplication


from models.ui.popups.qerror_popup import QErrorPopup


app = QApplication(sys.argv)


class QErrorPopupTest(unittest.TestCase):

    def test_show(self):
        self.popup = QErrorPopup('Erreur lors du chargement des données')

    def test_empty_popup(self):
        self.empty = QErrorPopup()


if __name__ == "__main__":
    unittest.main()
