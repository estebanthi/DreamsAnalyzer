from models.enums import DataLoadingMethod
from models.config import Config
from models.data.loaders.remote_loader import RemoteLoader
from models.data.loaders.file_loader import FileLoader
from models.exceptions.exceptions import DreamManagerWrongCredentials


class DataLoader:

    def __init__(self, controller):
        self.controller = controller

    def load_data(self, method, path=''):
        data = None

        if method == DataLoadingMethod.REMOTE:
            data = self.load_data_remote()
        if method == DataLoadingMethod.LOCAL:
            data = self.load_data_local(path)
        if method == DataLoadingMethod.LAST_DATA:
            data = self.load_last_data()

        return data

    def load_data_remote(self):
        data = None
        config = Config(self.controller)

        try:
            dream_manager_email = config.credentials['email']
            dream_manager_password = config.credentials['password']
        except KeyError:
            self.controller.notify_credentials_error()
            return None

        loader = RemoteLoader(dream_manager_email, dream_manager_password)
        try:
            data = loader.load()
        except DreamManagerWrongCredentials:
            self.controller.notify_credentials_error()
            return None

        return data

    def load_data_local(self, path):
        data = None

        loader = FileLoader()
        try:
            data = loader.load(path)
        except FileNotFoundError:
            self.controller.notify_file_not_found_error()
        except IOError:
            self.controller.notify_io_error()

        return data

    def load_last_data(self):
        data = None

        loader = FileLoader()
        try:
            data = loader.load('data/data.json')
        except FileNotFoundError:
            self.controller.notify_no_recent_data_error()
        except IOError:
            self.controller.notify_io_error()

        return data
