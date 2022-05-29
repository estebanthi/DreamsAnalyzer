import unittest
import sys


from PyQt5.QtWidgets import QApplication
from yaml import safe_load


from models.exceptions.qerror import QError
from models.data.json_to_datamodel_converter import JSONToDatamodelConverter
from models.data.remote_loader import RemoteLoader
from models.data.datamodel import Datamodel


app = QApplication(sys.argv)


class QErrorTest(unittest.TestCase):

    with open('data/credentials.yml', 'r') as file:
        credentials = safe_load(file)

    email = credentials['email']
    password = credentials['password']

    remoteloader = RemoteLoader(email, password)
    data = remoteloader.load()
    converter = JSONToDatamodelConverter()

    def test_get_categories(self):
        self.assertIs(type(self.converter.convert(self.data)), Datamodel)

if __name__ == '__main__':
    unittest.main()
