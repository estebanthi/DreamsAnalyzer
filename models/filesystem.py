import json


from services.config import load_config


class Filesystem:

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding
        self.config = load_config('config.yml')

    def load_data(self):
        try:
            with open(f"{self.config['data_pathname']}/{self.config['dream_manager_data_filename']}.json", 'r', encoding=self.encoding) as file:
                data = json.load(file)
                return data
        except Exception as e:
            return None
