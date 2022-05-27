import json


class Filesystem:

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def load_data(self, pathname):
        try:
            with open(pathname, 'r', encoding=self.encoding) as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return None
