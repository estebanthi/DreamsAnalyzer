import sys
import unittest


from PyQt5.QtWidgets import QApplication


from models.data.file_loader import FileLoader
from models.exceptions.qerror import QError


app = QApplication(sys.argv)


class QErrorPopupTest(unittest.TestCase):

    fileloader = FileLoader()

    def test_load_success(self):
        self.assertIs(type(self.fileloader.load('data/test.json')), dict)

    def test_load_failed(self):
        with self.assertRaises(QError):
            self.fileloader.load('data/unknown')

    def test_load_wrong_format(self):
        with self.assertRaises(QError):
            self.fileloader.load('data/credentials.yml')


if __name__ == "__main__":
    unittest.main()
