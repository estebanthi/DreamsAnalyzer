import requests
import json
from base64 import b64decode


from models.data.loaders.loader import Loader
from models.exceptions import DreamManagerWrongCredentials, DreamManagerDataError, EmptyDreamJournal


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

        json_res = response.json()
        if json_res['status'] == '404':
            raise DreamManagerWrongCredentials()

        if 'data' not in json_res:
            raise DreamManagerDataError()

        data = json_res['data']

        if not data:
            raise EmptyDreamJournal()

        decoded_data = self._decode_json(data)
        return decoded_data

    def _decode_json(self, data):
        bytes_ = b64decode(data)
        return json.loads(bytes_)
