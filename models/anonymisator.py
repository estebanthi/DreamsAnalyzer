import yaml


class Anonymisator:

    def get_records(self):
        with open('anonyms.yml', 'r') as file:
            return yaml.safe_load(file)

    def save_records(self, records):
        with open('anonyms.yml', 'w') as file:
            yaml.dump(records, file)
