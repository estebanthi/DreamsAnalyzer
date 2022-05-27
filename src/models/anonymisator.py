import yaml


from models.config import Config


class Anonymisator:

    def get_records(self):
        config = Config()
        anonyms_pathname = config['anonyms_pathname']
        with open(anonyms_pathname, 'r') as file:
            return yaml.safe_load(file)

    def save_records(self, records):
        config = Config()
        anonyms_pathname = config['anonyms_pathname']
        with open(anonyms_pathname, 'w') as file:
            yaml.dump(records, file)
