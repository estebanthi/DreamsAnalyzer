import yaml


class Anonymisator:

    def get_records(self):
        with open('data/anonyms.yml', 'r') as file:
            return yaml.safe_load(file)

    def save_records(self, records):
        with open('data/anonyms.yml', 'w') as file:
            yaml.dump(records, file)
