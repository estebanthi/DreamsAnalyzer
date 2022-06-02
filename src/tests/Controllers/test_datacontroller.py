import unittest
from unittest.mock import patch, create_autospec
from models.Views.main_window import MainWindow
from models.Models.datamodel import DataModel
from models.Controllers.datacontroller import DataController


class TestDataController(unittest.TestCase):

    controller = DataController()

    MainWindow = create_autospec(MainWindow)
    main_window_mock = MainWindow(controller)

    DataModel = create_autospec(DataModel)
    model_mock = DataModel(controller)

    controller.view = main_window_mock
    controller.model = model_mock

    @patch('models.Controllers.datacontroller.QInfoPopup')
    @patch.object(controller, 'model')
    def test_sync_data_success(self, model_mock, popup_mock):
        model_mock.remote_load_data.return_value = True
        self.controller.sync_data()
        assert popup_mock.called

    @patch('models.Controllers.datacontroller.QInfoPopup')
    @patch.object(controller, 'model')
    def test_sync_data_failed(self, model_mock, popup_mock):
        model_mock.remote_load_data.return_value = False
        self.controller.sync_data()
        assert popup_mock.not_called

    @patch('models.Controllers.datacontroller.QInfoPopup')
    @patch.object(controller, 'model')
    def test_load_last_data_success(self, model_mock, popup_mock):
        model_mock.load_last_data.return_value = True
        self.controller.load_last_data()
        assert popup_mock.called

    @patch('models.Controllers.datacontroller.QInfoPopup')
    @patch.object(controller, 'model')
    def test_load_last_data_failed(self, model_mock, popup_mock):
        model_mock.load_last_data.return_value = False
        self.controller.load_last_data()
        assert popup_mock.not_called


if __name__ == '__main__':
    unittest.main()
