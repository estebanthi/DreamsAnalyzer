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
        datamodel = None
        metas = self.get_metas()
        try:
            with open('data/data.json', 'r', encoding='utf-8') as file:
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
        anonyms_collection = None
        try:
            with open('data/anonyms.yml', 'r') as file:
                anonyms = yaml.safe_load(file)
                anonyms_collection = AnonymsCollection(anonyms)
        except Exception as e:
            print(e)

        return anonyms_collection

    def get_metas(self):
        metas_collection = MetasCollection()
        try:
            with open('data/metas.dat', 'rb') as file:
                metas_collection = pickle.load(file)
        except Exception as e:
            print(e)

        return metas_collection

    def get_credentials(self):
        credentials = {'password': '', 'email': ''}
        try:
            with open('data/credentials.yml', 'r') as file:
                credentials = yaml.safe_load(file)
        except Exception as e:
            print(e)

        return credentials

    @classmethod
    def initial_config(cls):

        if not os.path.isdir('data'):
            os.mkdir('data')

        if not os.path.isfile('data/metas.dat'):
            metas = MetasCollection()
            clear = Meta('Clarté', 'clear', MetaType.NUMERIC)
            mood = Meta('Mood', 'note', MetaType.NUMERIC)
            lucidity = Meta('Lucidité', 'lucidity', MetaType.NUMERIC)

            metas.append(clear)
            metas.append(mood)
            metas.append(lucidity)

            with open('data/metas.dat', 'wb') as file:
                pickle.dump(metas, file)

        if not os.path.isfile('data/anonyms.yml'):
            with open('data/anonyms.yml', 'w') as file:
                yaml.safe_dump([], file)

        if not os.path.isdir('data/templates'):
            os.mkdir('data/templates')
            template = Template('0.tp', 'Template par défaut', '{{content}}')
            with open('data/templates/0.tp', 'wb') as file:
                pickle.dump(template, file)

        if not os.path.isfile('data/credentials.yml'):
            with open('data/credentials.yml', 'w') as file:
                yaml.dump({'email': '', 'password': ''}, file)
