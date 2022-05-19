import datetime as dt


import html2text


from services.config import load_config


class Dream:

    def __init__(self, json_dream):
        self.id = json_dream['id']
        self.date = dt.datetime.fromtimestamp(json_dream['date'])
        self.title = json_dream['title']
        self.content = html2text.html2text(json_dream['content'])
        self.attached = json_dream['attached']
        self.color = self.get_color_mapping(json_dream['meta']['color'])
        self.clear = int(json_dream['meta']['clear'])
        self.note = int(json_dream['meta']['note'])
        self.lucid = json_dream['meta']['lucid']
        self.favorite = json_dream['meta']['favoris']
        self.tags = json_dream['tags']

    def __repr__(self):
        return f"Title : {self.title} | Date : {self.date}"

    @staticmethod
    def get_color_mapping(color):
        config = load_config('config.yml')
        colors_mapper = config['color_mapper']
        return colors_mapper[color]
