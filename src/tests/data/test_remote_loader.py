import unittest
from unittest.mock import MagicMock, patch
from base64 import b64encode


from models.exceptions.exceptions import DreamManagerWrongCredentials, DreamManagerDataError, EmptyDreamJournal


from models.data.loaders.remote_loader import RemoteLoader, requests


class TestRemoteLoader(unittest.TestCase):

    wrong_credentials_mock = MagicMock()
    wrong_credentials_mock.json.return_value = {'status': '404'}

    empty_dream_journal_mock = MagicMock()
    empty_dream_journal_mock.json.return_value = {'data': {}, 'status': '200'}

    remote_loader = RemoteLoader('', '')

    test_data = b64encode(b'{"a": "1"}')

    @patch.object(requests, 'post', return_value=wrong_credentials_mock)
    def test_wrong_credentials(self, mock_requests):
        with self.assertRaises(DreamManagerWrongCredentials):
            self.remote_loader.load()

    @patch.object(requests, 'post')
    def test_wrong_data_format(self, mock_requests):
        with self.assertRaises(DreamManagerDataError):
            self.remote_loader.load()

    @patch.object(requests, 'post', return_value=empty_dream_journal_mock)
    def test_empty_dream_journal(self, mock_requests):
        with self.assertRaises(EmptyDreamJournal):
            self.remote_loader.load()

    def test_decode_json(self):
        decoded_data = self.remote_loader._decode_json(self.test_data)
        self.assertIsInstance(decoded_data, dict)


if __name__ == '__main__':
    unittest.main()
