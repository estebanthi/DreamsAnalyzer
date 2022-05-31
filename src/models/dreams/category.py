from models.json.json_serializable import JSONSerializable


class Category:

    def __init__(self, _id, label):
        self._id = _id
        self.label = label

    def __repr__(self):
        return f"Category {self._id} : {self.label}"

    def __hash__(self):
        return self._id

    def __eq__(self, other):
        return self._id == other._id
