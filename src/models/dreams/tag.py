class Tag:

    def __init__(self, _id, label, category=None):
        self._id = _id
        self.label = label
        self.category = category

    def __repr__(self):
        return f"Tag {self._id} : {self.label}"

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return self._id
