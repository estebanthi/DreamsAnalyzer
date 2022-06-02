from models.collections.base_collection import BaseCollection


class TagsCollection(BaseCollection):

    def __init__(self, tags=None):
        super().__init__(tags)

    def __contains__(self, item):
        return item in [tag.label for tag in self.items]
