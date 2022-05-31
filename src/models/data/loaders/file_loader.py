import json


from models.data.loaders.loader import Loader


class FileLoader(Loader):

    def load(self, path):
        data = None
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
