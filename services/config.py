from yaml import safe_load


def load_config(filename='config.yml'):
    with open(filename, 'r') as file:
        return safe_load(file)
