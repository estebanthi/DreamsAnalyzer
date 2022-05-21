from yaml import safe_load


class Config:

    def __init__(self, pathname='config.yml'):
        with open(pathname, 'r') as file:
            return safe_load(file)
