import datetime as dt

from models.data.datamodel import Datamodel
from models.collections.dreams_collection import DreamsCollection
from models.collections.tags_collection import TagsCollection
from models.collections.categories_collection import CategoriesCollection
from models.dreams.category import Category
from models.dreams.tag import Tag
from models.dreams.dream import Dream


class JSONToDatamodelConverter:

    def convert(self, data: dict) -> Datamodel:
        date = dt.datetime.fromtimestamp(data['timestamp'])
        categories = CategoriesCollection(self.get_categories(data))
        tags = TagsCollection(self.get_tags(data))
        dreams = DreamsCollection(self.get_dreams(data))
        return Datamodel(date, dreams, tags, categories)

    @staticmethod
    def get_categories(data):
        json_categories = data['category']
        categories = [Category.parse(json_category) for json_category in json_categories.values()]
        return categories

    @staticmethod
    def get_tags(data):
        json_tags = data['tags']
        tags = [Tag.parse(json_tag) for json_tag in json_tags.values()]
        return tags

    @staticmethod
    def get_dreams(data):
        json_dreams = data['dreams']
        json_tags = data['tags']
        dreams = [Dream.parse(json_dream, json_tags) for json_dream in json_dreams.values()]
        return dreams
