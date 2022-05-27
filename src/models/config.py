import os
from yaml import safe_load
from yaml import dump


class Config:

    def __init__(self, pathname='config.yml'):
        with open(pathname, 'r') as file:
            self.config = safe_load(file)

    def __getitem__(self, item):
        return self.config[item]

    @staticmethod
    def initial_setup():
        try:
            with open('config.yml', 'r') as file:
                pass
        except FileNotFoundError:
            with open('config.yml', 'w') as file:
                dump({'dream_manager_data_pathname': 'data/dream_manager_data.json', 'anonyms_pathname': 'anonyms.yml', 'templates_directory': 'templates', 'temp_template_pathname': 'templates/temp.tp', 'dream_manager_data_filename': 'src/dream_manager_data', 'templates_pathname': 'src/templates', 'hh_color': -1, 'colors_mapper': {'red': 0, 'pink': 1, 'orange': 2, 'yellow': 3, 'lime': 4, 'green': 5, 'teal': 6, 'blue': 7, 'indigo': 8, 'grey': 9, 'purple': -1}}, file)

        with open('config.yml', 'r') as file:

            if not os.path.isdir('data'):
                os.mkdir('data')

            if not os.path.isdir('templates'):
                os.mkdir('templates')

            if not os.path.isfile('anonyms.yml'):
                with open('anonyms.yml', 'w') as file:
                    dump([], file)
