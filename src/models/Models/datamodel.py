import copy

from PyQt5 import QtCore
import yaml


from models.enums import TypeFilterOptions, DataLoadingMethod
from models.data.data_loader import DataLoader
from models.data.data_decoder import DataDecoder
from models.config import Config
from models.data.file_saver import FileSaver
from models.data.data_formatter import DataFormatter
import os


class DataModel(QtCore.QObject):
    dataUpdatedSignal = QtCore.pyqtSignal()

    def __init__(self, controller):
        super().__init__()

        conf = {'data_pathname': 'data'}
        with open(f"{os.environ['ProgramFiles']}\\Dreams Analyzer\\conf.yml", 'r') as file:
            conf = yaml.safe_load(file)
        self.data_pathname = conf['data_pathname']

        self.controller = controller
        self.config = Config(self.controller)

        self.load_last_data(initial=True)

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

    def remote_load_data(self):
        data_loader = DataLoader(self.controller)
        json_data = data_loader.load_data(DataLoadingMethod.REMOTE)

        if not json_data:
            return None

        file_saver = FileSaver()
        file_saver.save(json_data, f'{self.data_pathname}/data.json')

        data_formatter = DataFormatter(self.controller)
        formatted_data = None
        if json_data:
            formatted_data = data_formatter.format(json_data)

        data_decoder = DataDecoder(self.controller)
        data = None
        if formatted_data:
            data = data_decoder.decode(formatted_data, self.config.metas)

        self.data = data
        self.dataUpdatedSignal.emit()
        return data

    def load_last_data(self, initial=False):
        data_loader = DataLoader(self.controller)

        autosync = False

        if initial:
            with open(f'{self.data_pathname}/config.yml', 'r') as file:
                data = yaml.safe_load(file)
                autosync = data['autosync']

        loading_method = DataLoadingMethod.REMOTE if autosync else DataLoadingMethod.LAST_DATA
        json_data = data_loader.load_data(loading_method)

        if autosync and json_data:
            self.controller.notify_synced_successfully()

        data_formatter = DataFormatter(self.controller)
        formatted_data = None
        if json_data:
            formatted_data = data_formatter.format(json_data)

        data_decoder = DataDecoder(self.controller)
        data = None
        if formatted_data:
            data = data_decoder.decode(formatted_data, self.config.metas)

        self.data = data
        self.check_data()

        self.dataUpdatedSignal.emit()
        return True

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    def check_data(self):
        if self.data:
            if self.data.dreams:
                initial_metas = copy.copy(self.data.dreams[0].metas)
                for dream in self.data.dreams:
                    dream.clean()
                final_metas = self.data.dreams[0].metas

                if len(initial_metas) != len(final_metas):
                    self.controller.notify_metas_error(initial_metas, final_metas)