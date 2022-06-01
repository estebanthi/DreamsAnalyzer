import datetime as dt


import html2text


from models.data.datamodel import Datamodel
from models.collections.dreams_collection import DreamsCollection
from models.collections.tags_collection import TagsCollection
from models.collections.categories_collection import CategoriesCollection
from models.dreams.category import Category
from models.dreams.tag import Tag
from models.dreams.dream import Dream
from models.time.roundable_date import RoundableDate
from models.collections.metas_collection import MetasCollection


class DataDecoder:

    def __init__(self, controller):
        self.controller = controller

    def decode(self, data: dict, metas=MetasCollection()) -> Datamodel:
        try:
            date = dt.datetime.fromtimestamp(data['timestamp'])
            categories = CategoriesCollection(self.get_categories(data['category']))
            tags = TagsCollection(self.get_tags(data['tags']))
            dreams = DreamsCollection(self.get_dreams(data['dreams'], data['tags'], metas))
            return Datamodel(date, dreams, tags, categories)
        except Exception as e:
            self.controller.notify_data_decoding_error()
            return None

    @classmethod
    def get_categories(cls, json_categories):
        categories = [cls.parse_category(json_category) for json_category in json_categories.values()]
        return categories

    @staticmethod
    def parse_category(json_category):
        _id = int(json_category['id'])
        label = json_category['label']
        return Category(_id, label)

    @classmethod
    def get_tags(cls, json_tags):
        tags = [cls.parse_tag(json_tag) for json_tag in json_tags.values()]
        return tags

    @staticmethod
    def parse_tag(json_tag):
        _id = int(json_tag['id'])
        label = json_tag['label']

        category = None
        if 'cat' in json_tag and 'cat_ct' in json_tag:
            if json_tag['cat'] != 'none':
                category = Category(int(json_tag['cat']), json_tag['cat_ct'])

        return Tag(_id, label, category)

    @classmethod
    def get_dreams(cls, json_dreams, json_tags, metas=MetasCollection()):
        dreams = [cls.parse_dream(json_dream, json_tags, metas) for json_dream in json_dreams.values()]
        return dreams

    @classmethod
    def parse_dream(cls, json_dream, json_tags, metas):
        date = dt.datetime.fromtimestamp(json_dream['date'])
        date = RoundableDate(date.year, date.month, date.day, date.hour, date.minute, date.second)

        title = json_dream['title']
        content = html2text.html2text(json_dream['content']).replace('\n', ' ')

        tags = cls.get_tags(json_tags)
        dream_tags = [tag for tag in tags if tag._id in [int(json_tag) for json_tag in json_dream['tags']]]

        lucid = json_dream['meta']['lucid']

        dream_metas = MetasCollection()
        for meta in metas:
            dream_metas.append(meta.get_from_json_dream(json_dream))

        return Dream(date, content, title, lucid, dream_tags, dream_metas)
