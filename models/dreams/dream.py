import datetime as dt


import html2text


from models.json.json_serializable import JSONSerializable
from models.config import Config


class Dream(JSONSerializable):

    def __init__(self, _id, date, content, lucidity, lucid, title=None, attached=None, clear=None, mood=None, tags=[],
                 is_hh=False):
        self._id = _id
        self.date = date
        self.content = content,
        self.lucidity = lucidity
        self.lucid = lucid
        self.title = title
        self.attached = attached
        self.clear = clear
        self.mood = mood
        self.tags = tags
        self.is_hh = is_hh

    @classmethod
    def parse(cls, json_model):
        _id = json_model['id']
        date = dt.datetime.fromtimestamp(json_model['date'])
        title = json_model['title']
        content = html2text.html2text(json_model['content'])
        lucidity = cls.get_lucidity_from_color(json_model['meta']['color'])

    @staticmethod
    def get_lucidity_from_color(color):
        config = Config()
        colors_mapper = config['colors_mapper']
        return colors_mapper[color]

    def __repr__(self):
        return f"Title : {self.title} | Date : {self.date}"
