class Category:

    def __init__(self, json_category):
        self._id = int(json_category['id'])
        self.label = json_category['label']

    def __repr__(self):
        return f"Category {self._id} : {self.label}"
