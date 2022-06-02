import unittest
from unittest.mock import patch, MagicMock, create_autospec, mock_open


from models.data.data_loader import DataLoadingMethod, DataLoader, Config, RemoteLoader, DreamManagerWrongCredentials
from models.Controllers.datacontroller import DataController


class TestDataLoader(unittest.TestCase):

    DataController = create_autospec(DataController)
    mock_controller = DataController()

    data_loader = DataLoader(mock_controller)

    @patch('models.data.data_loader.Config.get_credentials', return_value={'password': ''})
    def test_load_data_remote_credentials_error(self, mock_config):
        with patch("builtins.open", mock_open()):
            data = self.data_loader.load_data_remote()
        self.mock_controller.notify_credentials_error.assert_called()
        self.assertIs(data, None)

    @patch('models.data.data_loader.RemoteLoader.load')
    @patch('models.data.data_loader.Config')
    def test_load_data_remote_credentials_error(self, config_mock, load_mock):
        load_mock.side_effect = DreamManagerWrongCredentials
        with patch("builtins.open", mock_open()):
            data = self.data_loader.load_data_remote()
        self.mock_controller.notify_credentials_error.assert_called()

    @patch('models.data.data_loader.RemoteLoader.load', return_value='ok')
    @patch('models.data.data_loader.Config')
    def test_load_data_remote_ok(self, config_mock, load_mock):
        data = self.data_loader.load_data_remote()
        self.assertEqual(data, 'ok')

    @patch('models.data.data_loader.FileLoader.load')
    def test_load_data_local_file_not_found(self, load_mock):
        load_mock.side_effect = FileNotFoundError
        data = self.data_loader.load_data_local('')
        self.mock_controller.notify_file_not_found_error.assert_called()

    @patch('models.data.data_loader.FileLoader.load')
    def test_load_data_local_io_error(self, load_mock):
        load_mock.side_effect = IOError
        data = self.data_loader.load_data_local('')
        self.mock_controller.notify_io_error.assert_called()

    @patch('models.data.data_loader.FileLoader.load')
    def test_load_data_local_ok(self, load_mock):
        load_mock.return_value = 'ok'
        data = self.data_loader.load_data_local('')
        self.assertEqual(data, 'ok')

    @patch('models.data.data_loader.FileLoader.load')
    def test_load_last_data_not_found(self, load_mock):
        load_mock.side_effect = FileNotFoundError
        data = self.data_loader.load_last_data()
        self.mock_controller.notify_no_recent_data_error.assert_called()

    @patch('models.data.data_loader.FileLoader.load')
    def test_load_last_data_io_error(self, load_mock):
        load_mock.side_effect = IOError
        data = self.data_loader.load_last_data()
        self.mock_controller.notify_io_error.assert_called()

    @patch('models.data.data_loader.FileLoader.load')
    def test_load_last_data_ok(self, load_mock):
        load_mock.return_value = 'ok'
        data = self.data_loader.load_last_data()
        self.assertEqual(data, 'ok')


if __name__ == '__main__':
    unittest.main()
