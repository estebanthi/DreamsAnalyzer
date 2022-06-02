import unittest
from unittest.mock import patch, MagicMock, create_autospec


from models.data.data_formatter import DataFormatter
from models.Controllers.datacontroller import DataController
from tests.samples.test_data import json_data


class TestDataFormatter(unittest.TestCase):

    DataController = create_autospec(DataController)
    mock_controller = DataController()
    formatter = DataFormatter(mock_controller)

    def test_format_ok(self):
        formatted_data = self.formatter.format(json_data)
        self.assertEqual(formatted_data['dreams']['0']['meta']['lucidity'], 0)

    def test_format_nok(self):
        json_data_copy = json_data.copy()
        del(json_data_copy['dreams'])
        formatted_data = self.formatter.format(json_data_copy)
        self.mock_controller.notify_data_formatting_error.assert_called()
        self.assertIs(formatted_data, None)


if __name__ == '__main__':
    unittest.main()
