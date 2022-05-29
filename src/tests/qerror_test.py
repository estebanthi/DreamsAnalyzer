import unittest
import sys


from PyQt5.QtWidgets import QApplication


from models.exceptions.qerror import QError


app = QApplication(sys.argv)


class QErrorTest(unittest.TestCase):

    def test_error(self):
        error = QError('test')


if __name__ == '__main__':
    unittest.main()
