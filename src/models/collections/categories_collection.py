from models.collections.base_collection import BaseCollection


class CategoriesCollection(BaseCollection):

    def __init__(self, categories=None):
        super().__init__(categories)
