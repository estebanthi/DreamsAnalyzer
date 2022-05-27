from models.json.json_serializable import JSONSerializable


class Category(JSONSerializable):

    def __init__(self, _id, label):
        self._id = _id
        self.label = label

    @staticmethod
    def parse(json_model):
        _id = int(json_model['id'])
        label = json_model['label']
        return Category(_id, label)

    def __repr__(self):
        return f"Category {self._id} : {self.label}"

    def __hash__(self):
        return self._id

    def __eq__(self, other):
        return self._id == other._id
