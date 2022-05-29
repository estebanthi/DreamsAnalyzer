import sys
import unittest


from PyQt5.QtWidgets import QApplication
from yaml import safe_load


from models.data.remote_loader import RemoteLoader
from models.exceptions.qerror import QError


app = QApplication(sys.argv)


class RemoteLoaderTest(unittest.TestCase):

    with open('data/credentials.yml', 'r') as file:
        credentials = safe_load(file)

    email = credentials['email']
    password = credentials['password']

    remoteloader = RemoteLoader(email, password)
    wrong_remoteloader = RemoteLoader(email, email)

    def test_load_success(self):
        self.assertIs(type(self.remoteloader.load()), dict)

    def test_load_failed(self):
        with self.assertRaises(QError):
            self.wrong_remoteloader.load()


if __name__ == "__main__":
    unittest.main()
