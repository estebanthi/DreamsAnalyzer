import requests
import json
from base64 import b64decode


from models.data.loader import Loader
from models.exceptions.qerror import QError


class RemoteLoader(Loader):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def load(self):
        api_url = "https://astucesweb.fr/dream-manager/api/"

        body = {'mail': self.email, 'motdepasse': self.password, 'operation': 'login'}
        headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'X-Requested-With': 'XMLHttpRequest',
                   'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

        response = requests.post(api_url, data=body, headers=headers)

        if response.status_code == 404:
            raise QError('Identifiants Dream Manager incorrects')

        json_res = response.json()

        if 'data' not in json_res:
            raise QError('Erreur lors de la réception des données')

        data = json_res['data']

        if not data:
            raise QError("Votre journal de rêves est vide")

        try:
            decoded_data = self._decode_json(data)
        except Exception:
            raise QError('Erreur lors du décodage de vos données')

        return decoded_data

    def _decode_json(self, data):
        bytes_ = b64decode(data)
        return json.loads(bytes_)
