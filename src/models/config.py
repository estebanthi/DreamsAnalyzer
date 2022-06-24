import json
import pickle
import os


import yaml


from models.data.data_decoder import DataDecoder
from models.template import Template
from models.collections.anonyms_collection import AnonymsCollection
from models.collections.metas_collection import MetasCollection
from models.dataclasses.meta import Meta
from models.enums import MetaType
from models.data.data_formatter import DataFormatter


class Config:

    def __init__(self, controller):
        self.controller = controller
        self.data = self.get_data()
        self.anonyms = self.get_anonyms()
        self.metas = self.get_metas()
        self.credentials = self.get_credentials()

    def get_data(self):
        conf = {'data_pathname': 'data'}
        with open('conf.yml', 'r') as file:
            conf = yaml.safe_load(file)
        data_pathname = conf['data_pathname']

        datamodel = None
        metas = self.get_metas()
        try:
            with open(f'{data_pathname}/data.json', 'r', encoding='utf-8') as file:
                json_data = json.load(file)

                data_formatter = DataFormatter(self.controller)
                formatted_data = None
                if json_data:
                    formatted_data = data_formatter.format(json_data)

                if formatted_data:
                    decoder = DataDecoder(self.controller)
                    datamodel = decoder.decode(formatted_data, metas)
                    return datamodel
                return None
        except Exception as e:
            return None

        return datamodel

    def get_anonyms(self):
        conf = {'data_pathname': 'data'}
        with open('conf.yml', 'r') as file:
            conf = yaml.safe_load(file)
        data_pathname = conf['data_pathname']
        anonyms_collection = None
        try:
            with open(f'{data_pathname}/anonyms.yml', 'r') as file:
                anonyms = yaml.safe_load(file)
                anonyms_collection = AnonymsCollection(anonyms)
        except Exception as e:
            print(e)

        return anonyms_collection

    def get_metas(self):
        conf = {'data_pathname': 'data'}
        with open('conf.yml', 'r') as file:
            conf = yaml.safe_load(file)
        data_pathname = conf['data_pathname']
        metas_collection = MetasCollection()
        try:
            with open(f'{data_pathname}/metas.dat', 'rb') as file:
                metas_collection = pickle.load(file)
        except Exception as e:
            print(e)

        return metas_collection

    def get_credentials(self):
        conf = {'data_pathname': 'data'}
        with open('conf.yml', 'r') as file:
            conf = yaml.safe_load(file)
        data_pathname = conf['data_pathname']

        credentials = {'password': '', 'email': ''}
        try:
            with open(f'{data_pathname}/credentials.yml', 'r') as file:
                credentials = yaml.safe_load(file)
        except Exception as e:
            print(e)

        return credentials

    @classmethod
    def initial_config(cls):

        default_pathname = 'O:\\data'

        if not os.path.isfile('data_pathname.yml'):
            with open('conf.yml', 'w') as file:
                yaml.dump({'data_pathname': default_pathname}, file)

        if not os.path.isdir(default_pathname):
            os.makedirs(default_pathname)

        if not os.path.isfile(f'{default_pathname}/metas.dat'):
            metas = MetasCollection()
            clear = Meta('Clarté', 'clear', MetaType.NUMERIC, id_=0)
            mood = Meta('Mood', 'note', MetaType.NUMERIC, id_=1)
            lucidity = Meta('Lucidité', 'lucidity', MetaType.NUMERIC, id_=2)

            metas.append(clear)
            metas.append(mood)
            metas.append(lucidity)

            with open(f'{default_pathname}/metas.dat', 'wb') as file:
                pickle.dump(metas, file)

        if not os.path.isfile(f'{default_pathname}/anonyms.yml'):
            with open(f'{default_pathname}/anonyms.yml', 'w') as file:
                yaml.safe_dump([], file)

        if not os.path.isdir(f'{default_pathname}/templates'):
            os.makedirs(f'{default_pathname}/templates')
            template = Template('0.tp', 'Template par défaut', '{{content}}')
            with open(f'{default_pathname}/templates/0.tp', 'wb') as file:
                pickle.dump(template, file)

        if not os.path.isfile(f'{default_pathname}/credentials.yml'):
            with open(f'{default_pathname}/credentials.yml', 'w') as file:
                yaml.dump({'email': '', 'password': ''}, file)

        if not os.path.isfile(f'{default_pathname}/config.yml'):
            with open(f'{default_pathname}/config.yml', 'w') as file:
                yaml.dump({'autosync': False}, file)

        if not os.path.isfile(f'{default_pathname}/charts.yml'):
            with open(f'{default_pathname}/charts.yml', 'w') as file:

                charts = [
            {'id_': 0, 'title': "Méthodes d'inductions", 'tags': [['WILD', 'IN', '#008080', {}], ['DILD', 'IN', '#a52a2a', {}]]},
            {'id_': 1, 'title': "Proportion de RL WBTB", 'tags': [['WBTB', 'IN', '#458b74', {'lucid': True}], ['WBTB', 'NOT IN', '#3cb371', {'lucid':True}]]},
            {'id_': 2, 'title': "Proportion de rêves VIVID", 'tags': [['VIVID', 'IN', '#ff5800', {}], ['VIVID', 'NOT IN', '#a52a2a', {}]],},
        ]
                yaml.dump(charts, file)
