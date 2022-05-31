from models.collections.metas_collection import MetasCollection


class Dream:

    def __init__(self, date, content, title, lucid, tags=[], metas=MetasCollection()):
        self.date = date
        self.content = content
        self.lucid = lucid
        self.title = title
        self.tags = tags
        self.metas = MetasCollection()

    def __repr__(self):
        return f"Title : {self.title} | Date : {self.date}"
