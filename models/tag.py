from models.category import Category


class Tag:

    def __init__(self, json_tag):
        self._id = int(json_tag['id'])
        self.label = json_tag['label']
        self.category = None
        if json_tag['cat'] != 'none' and 'cat_ct' in json_tag:
            self.category = Category(self.get_json_category(json_tag))

    @staticmethod
    def get_json_category(json_tag):
        return {'id': json_tag['cat'], 'label': json_tag['cat_ct']}

    def __repr__(self):
        return f"Tag {self._id} : {self.label}"

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return self._id
