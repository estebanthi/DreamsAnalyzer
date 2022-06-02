import unittest
import sys


from PyQt5.QtWidgets import QApplication
from yaml import safe_load


from models.data.data_decoder import DataDecoder
from models.data.loaders.remote_loader import RemoteLoader
from models.data.data_representation import DataRepresentation


app = QApplication(sys.argv)


class DataDecoderTest(unittest.TestCase):

    with open('data/credentials.yml', 'r') as file:
        credentials = safe_load(file)

    email = credentials['email']
    password = credentials['password']

    remoteloader = RemoteLoader(email, password)
    data = remoteloader.load()
    decoder = DataDecoder()

    def test_decode(self):
        self.assertIs(type(self.decoder.decode(self.data)), DataRepresentation)


if __name__ == '__main__':
    unittest.main()
