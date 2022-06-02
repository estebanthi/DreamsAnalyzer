from models.collections.base_collection import BaseCollection


class AnonymsCollection(BaseCollection):

    def __init__(self, anonyms=None):
        super().__init__(anonyms)
