import datetime as dt


import html2text


from models.json.json_serializable import JSONSerializable
from models.config import Config
from models.dreams.tag import Tag
from models.time.roundable_date import RoundableDate
from models.collections.tags_collection import TagsCollection


class Dream(JSONSerializable):

    def __init__(self, _id, date, content, lucidity, lucid, title=None, clear=None, mood=None, tags=[],
                 is_hh=False):
        self._id = _id
        self.date = date
        self.content = content
        self.lucidity = lucidity
        self.lucid = lucid
        self.title = title
        self.clear = clear
        self.mood = mood
        self.tags = tags
        self.is_hh = is_hh

    @classmethod
    def parse(cls, json_model, json_tags):
        _id = json_model['id']

        date = dt.datetime.fromtimestamp(json_model['date'])
        date = RoundableDate(date.year, date.month, date.day, date.hour, date.minute, date.second)
        title = json_model['title']
        content = html2text.html2text(json_model['content']).replace('\n', ' ')
        lucidity = cls.get_lucidity_from_color(json_model['meta']['color'])
        lucid = json_model['meta']['lucid']
        clear = int(json_model['meta']['clear'])
        mood = int(json_model['meta']['note'])
        tags = TagsCollection([Tag.parse(json_tags[_id]) for _id in json_model['tags']])
        is_hh = True if lucidity == -1 else False
        return Dream(_id, date, content, lucidity, lucid, title, clear, mood, tags, is_hh)

    @staticmethod
    def get_lucidity_from_color(color):
        config = Config()
        colors_mapper = config['colors_mapper']
        return colors_mapper[color]

    def __repr__(self):
        return f"Title : {self.title} | Date : {self.date}"
