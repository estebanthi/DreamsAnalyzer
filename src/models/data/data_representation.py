import datetime as dt


from models.collections.dreams_collection import DreamsCollection
from models.collections.tags_collection import TagsCollection
from models.collections.categories_collection import CategoriesCollection


class DataRepresentation:

    def __init__(self, date:dt.datetime, dreams: DreamsCollection, tags: TagsCollection,
                 categories: CategoriesCollection):
        self.date = date
        self.dreams = dreams.filter(lambda dream: not dream.is_hh)
        self.hhs = dreams.filter(lambda dream: dream.is_hh)
        self.tags = tags
        self.categories = categories

    @property
    def dreams(self):
        return self._dreams

    @dreams.setter
    def dreams(self, dreams):
        self._dreams = dreams
