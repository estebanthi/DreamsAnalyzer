from models.enums import MetaType


class Meta:

    def __init__(self, name, json_name, type_, value=None, id_=None):
        self.name = name
        self.json_name = json_name
        self.type_ = type_
        self.value = value
        self.id_ = id_

    def get_from_json_dream(self, json_dream):
        try:
            value = json_dream['meta'][self.json_name]
        except Exception as e:
            return Meta(self.name, self.json_name, self.type_, None)
        return Meta(self.name, self.json_name, self.type_, int(value) if self.type_ == MetaType.NUMERIC else str(value))

    def __eq__(self, other):
        if type(other) is Meta:
            return self.name == other.name
        if type(other) is str:
            return self.name == other

    def __str__(self):
        return f"{self.name} : {self.value}"
