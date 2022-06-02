from models.collections.base_collection import BaseCollection


class MetasCollection(BaseCollection):

    def __init__(self, metas=None):
        super().__init__(metas)
