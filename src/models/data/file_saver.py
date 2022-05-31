import json


class FileSaver:

    def save(self, data, path):
        with open(path, 'w') as file:
            json.dump(data, file)
