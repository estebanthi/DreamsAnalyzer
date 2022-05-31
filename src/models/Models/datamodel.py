from PyQt5 import QtCore


from models.enums import TypeFilterOptions, DataLoadingMethod
from models.data.data_loader import DataLoader
from models.data.data_decoder import DataDecoder
from models.config import Config
from models.data.file_saver import FileSaver


class DataModel(QtCore.QObject):
    dataUpdatedSignal = QtCore.pyqtSignal()

    def __init__(self, controller):
        super().__init__()
        self.config = Config()
        self.controller = controller

        data_loader = DataLoader(self.controller)
        json_data = data_loader.load_data(DataLoadingMethod.LAST_DATA)

        data_decoder = DataDecoder()
        data = None
        if json_data:
            data = data_decoder.decode(json_data, self.config.metas)

        self.dataUpdatedSignal.emit()
        self.data = data

    def filter_dreams(self, start=None, end=None, type_=TypeFilterOptions.ALL):
        if start is None:
            start = self.data.dreams[0].date
        if end is None:
            end = self.data.dreams[-1].date

        filtered_dreams = self.data.dreams.filter(lambda dream: dream.date >= start and dream.date <= end)
        filtered_hhs = self.data.hhs.filter(lambda dream: dream.date >= start and dream.date <= end)

        if type_ == TypeFilterOptions.NORMAL:
            filtered_dreams = filtered_dreams.filter(lambda dream: not dream.lucid)
        if type_ == TypeFilterOptions.LUCID:
            filtered_dreams = filtered_dreams.filter(lambda dream: dream.lucid)

        self.data.dreams = filtered_dreams
        self.data.hhs = filtered_hhs
        self.dataUpdatedSignal.emit()
        return filtered_dreams

    def reset_filter(self):
        data_loader = DataLoader()
        data = data_loader.load_data(DataLoadingMethod.LAST_DATA)
        self.data = data
        self.dataUpdatedSignal.emit()
        return data

    def remote_load_data(self):
        data_loader = DataLoader(self.controller)
        data = data_loader.load_data(DataLoadingMethod.REMOTE)

        if not data:
            return None

        file_saver = FileSaver()
        file_saver.save(data, 'data/data.json')

        data_decoder = DataDecoder()
        decoded_data = data_decoder.decode(data, self.config.metas)
        self.data = decoded_data
        self.dataUpdatedSignal.emit()
        return decoded_data

    def load_last_data(self):
        data_loader = DataLoader(self.controller)
        data = data_loader.load_data(DataLoadingMethod.LAST_DATA)

        if not data:
            return None

        data_decoder = DataDecoder()
        decoded_data = data_decoder.decode(data, self.config.metas)
        self.data = decoded_data
        self.dataUpdatedSignal.emit()
        return decoded_data
