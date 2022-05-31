import sys
import unittest


from PyQt5.QtWidgets import QApplication


from models.data.loaders.file_loader import FileLoader
from json.decoder import JSONDecodeError


app = QApplication(sys.argv)


class FileLoaderTest(unittest.TestCase):

    fileloader = FileLoader()

    def test_load_success(self):
        self.assertIs(type(self.fileloader.load('data/test.json')), dict)

    def test_load_failed(self):
        with self.assertRaises(FileNotFoundError):
            self.fileloader.load('data/unknown')

    def test_load_wrong_format(self):
        with self.assertRaises(JSONDecodeError):
            self.fileloader.load('data/credentials.yml')


if __name__ == "__main__":
    unittest.main()
