from PyQt5 import QtCore


from models.enums import TypeFilterOptions, DataLoadingMethod
from models.data.data_loader import DataLoader
from models.data.data_decoder import DataDecoder


class DataModel(QtCore.QObject):
    dataUpdatedSignal = QtCore.pyqtSignal()

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        data_loader = DataLoader(self.controller)
        json_data = data_loader.load_data(DataLoadingMethod.LAST_DATA)

        data_decoder = DataDecoder()
        data = data_decoder.decode(json_data)
        self.data = data

    def filter_dreams(self, start=None, end=None, type_=TypeFilterOptions.ALL):
        if start is None:
            start = self.data.dreams[0].date
        if end is None:
            end = self.data.dreams[-1].date

        filtered_dreams = self.data.dreams.filter(lambda dream: dream.date >= start and dream.date <= end)

        if type_ == TypeFilterOptions.NORMAL:
            filtered_dreams = filtered_dreams.filter(lambda dream: not dream.lucid)
        if type_ == TypeFilterOptions.LUCID:
            filtered_dreams = filtered_dreams.filter(lambda dream: dream.lucid)

        self.data.dreams = filtered_dreams
        self.dataUpdatedSignal.emit()
        return filtered_dreams

    def reset_filter(self):
        data_loader = DataLoader()
        data = data_loader.load_data(DataLoadingMethod.LAST_DATA)
        self.data = data
        self.dataUpdatedSignal.emit()
        return data
