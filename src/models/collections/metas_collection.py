from models.collections.base_collection import BaseCollection


class MetasCollection(BaseCollection):

    def __init__(self, metas=None):
        super().__init__(metas)

    def __contains__(self, item):
        for item_ in self.items:
            if item_.name == item.name:
                return True
        return False