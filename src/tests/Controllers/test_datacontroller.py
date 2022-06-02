import unittest
from unittest.mock import patch, create_autospec
from models.Views.main_window import MainWindow
from models.Models.datamodel import DataModel
from models.Controllers.datacontroller import DataController, TypeFilterOptions


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
        popup_mock.assert_called()

    @patch('models.Controllers.datacontroller.QInfoPopup')
    @patch.object(controller, 'model')
    def test_sync_data_failed(self, model_mock, popup_mock):
        model_mock.remote_load_data.return_value = False
        self.controller.sync_data()
        popup_mock.assert_not_called()

    @patch('models.Controllers.datacontroller.QInfoPopup')
    @patch.object(controller, 'model')
    def test_load_last_data_success(self, model_mock, popup_mock):
        model_mock.load_last_data.return_value = True
        self.controller.load_last_data()
        popup_mock.assert_called()

    @patch('models.Controllers.datacontroller.QInfoPopup')
    @patch.object(controller, 'model')
    def test_load_last_data_failed(self, model_mock, popup_mock):
        model_mock.data = None
        self.controller.load_last_data()
        popup_mock.assert_not_called()

    def test_notify_no_recent_data_error(self):
        callb = self.controller.notify_no_recent_data_error()
        self.assertIs(callb, None)

    @patch('models.Controllers.datacontroller.QError')
    def test_notify_credentials_error(self, popup_mock):
        self.controller.notify_credentials_error()
        popup_mock.assert_called()

    @patch('models.Controllers.datacontroller.QError')
    def test_notify_data_decoding_error(self, popup_mock):
        self.controller.notify_data_decoding_error()
        popup_mock.assert_called()

    @patch('models.Controllers.datacontroller.QError')
    def test_notify_data_formatting_error(self, popup_mock):
        self.controller.notify_data_formatting_error()
        popup_mock.assert_called()

    @patch('models.Controllers.datacontroller.QError')
    def test_notify_file_not_found_error(self, popup_mock):
        self.controller.notify_file_not_found_error()
        popup_mock.assert_called()

    @patch('models.Controllers.datacontroller.QError')
    def test_notify_io_error(self, popup_mock):
        self.controller.notify_io_error()
        popup_mock.assert_called()

    @patch.object(controller, 'model')
    def test_filter_dreams(self, model_mock):
        self.controller.filter_dreams(label='Lucides')
        model_mock.filter_dreams.assert_called_with(None, None, TypeFilterOptions.LUCID)
        result = self.controller.filter_dreams(label='Normal')
        model_mock.filter_dreams.assert_called_with(None, None, TypeFilterOptions.NORMAL)
        self.controller.filter_dreams()
        model_mock.filter_dreams.assert_called_with(None, None, TypeFilterOptions.ALL)

    @patch.object(controller, 'view')
    def test_reset_filter(self, view_mock):
        self.controller.reset_filter()
        view_mock.dreamTypeSelect.setCurrentText.assert_called_with('Tout')

    @patch.object(controller, 'view')
    @patch.object(controller, 'model')
    def test_connect(self, model_mock, view_mock):
        self.controller.connect()
        model_mock.dataUpdatedSignal.connect.assert_called_with(view_mock.updateData)



if __name__ == '__main__':
    unittest.main()
