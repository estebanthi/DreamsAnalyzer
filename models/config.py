from yaml import safe_load


class Config:

    def __init__(self, pathname='config.yml'):
        with open(pathname, 'r') as file:
            self.config = safe_load(file)

    def __getitem__(self, item):
        return self.config[item]
