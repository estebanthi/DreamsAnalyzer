import datetime as dt


from models.collections.dreams_collection import DreamsCollection
from models.collections.tags_collection import TagsCollection
from models.collections.categories_collection import CategoriesCollection


class Datamodel:

    def __init__(self, date:dt.datetime, dreams: DreamsCollection, tags: TagsCollection,
                 categories: CategoriesCollection):
        self.date = date
        self.dreams = dreams
        self.tags = tags
        self.categories = categories

