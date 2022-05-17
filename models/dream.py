import datetime as dt


class Dream:

    def __init__(self, json_dream):
        self.id = json_dream['id']
        self.date = dt.datetime.fromtimestamp(json_dream['date'])
        self.title = json_dream['title']
        self.content = json_dream['content']
        self.attached = json_dream['attached']
        self.color = json_dream['meta']['color']
        self.clear = json_dream['meta']['clear']
        self.note = json_dream['meta']['note']
        self.lucid = json_dream['meta']['lucid']
        self.favorite = json_dream['meta']['favoris']
        self.tags = json_dream['tags']

    def __repr__(self):
        return f"Title : {self.title} | Date : {self.date}"
