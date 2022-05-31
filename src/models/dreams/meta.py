from models.enums import MetaType


class Meta:

    def __init__(self, name, json_name, type_, value=None):
        self.name = name
        self.json_name = json_name
        self.type_ = type_
        self.value = value

    def get_from_json_dream(self, json_dream):
        value = json_dream[self.json_name]
        return int(value) if self.type_ == MetaType.INT else str(value)

    def __eq__(self, other):
        return self.name == other.name
