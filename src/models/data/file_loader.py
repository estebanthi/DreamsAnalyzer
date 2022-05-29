import json


from models.data.loader import Loader
from models.data.datamodel import Datamodel
from models.exceptions.qerror import QError


class FileLoader(Loader):

    def load(self, path):
        data = None
        try:
            with open(path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            raise QError('Fichier introuvable')
        except IOError:
            raise QError("Erreur lors de l'ouverture du fichier")
        except json.decoder.JSONDecodeError:
            raise QError("Le format de votre fichier est invalide")

        return data
