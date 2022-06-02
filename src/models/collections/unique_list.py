from models.collections.base_collection import BaseCollection


class UniqueList(BaseCollection):

    def __init__(self, _list):
        _list = list(set(_list))
        super().__init__(_list)
