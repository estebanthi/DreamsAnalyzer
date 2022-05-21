from models.json.json_serializable import JSONSerializable
from models.dreams.category import Category


class Tag(JSONSerializable):

    def __init__(self, _id, label, category=None):
        self._id = _id
        self.label = label
        self.category = category

    @staticmethod
    def parse(json_model):
        _id = int(json_model['id'])
        label = json_model['label']

        category = None
        if 'cat' in json_model and 'cat_ct' in json_model:
            if json_model['cat'] != 'none':
                category = Category(int(json_model['cat']), json_model['cat_ct'])

        return Tag(_id, label, category)

    def __repr__(self):
        return f"Tag {self._id} : {self.label}"

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return self._id
