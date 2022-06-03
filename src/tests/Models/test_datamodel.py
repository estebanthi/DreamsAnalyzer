import unittest
from unittest.mock import MagicMock, patch, create_autospec, PropertyMock


from models.Models.datamodel import DataModel
from models.Controllers.datacontroller import DataController


class TestDataModel(unittest.TestCase):

    DataController = MagicMock()
    controller = DataController()

    with patch('models.Models.datamodel.Config'):
        model = DataModel(controller)

    mock_data = MagicMock()
    model.data = mock_data

    @patch('models.data.data_representation.DataRepresentation.dreams', new_callable=PropertyMock)
    @patch.object(model, 'dataUpdatedSignal')
    def test_filter_(self, mock_signal, data_mock):
        self.model.filter_dreams()
        mock_signal.emit.assert_called()


if __name__ == '__main__':
    unittest.main()
