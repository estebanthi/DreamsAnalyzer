import pickle
import yaml
import os


from models.string.mutable_string import MutableString


class Template:

    def __init__(self, filename, name='Template par défaut', content='', lucid_dreams_color='blue',
                 normal_dreams_color='green', special_texts=None):
        self.name = name
        self.content = content
        self.filename = filename

        self.lucid_dreams_color = lucid_dreams_color
        self.normal_dreams_color = normal_dreams_color

        if not special_texts:
            special_texts = []
        self.special_texts = special_texts

    def parse(self, dream, nb=''):
        conf = {'data_pathname': 'data'}
        with open(f"{os.environ['ProgramFiles']}\\Dreams Analyzer\\conf.yml", 'r') as file:
            conf = yaml.safe_load(file)
        data_pathname = conf['data_pathname']

        self.copied = self.content
        self.replace_mark('type', 'RL' if dream.lucid else 'RN')
        self.replace_mark('title', dream.title)
        self.replace_mark('tags', " - ".join([tag.label for tag in dream.tags]))
        self.replace_mark('time', str(dream.date.hour)+'H'+str(dream.date.minute))

        for meta in dream.metas:
            if hasattr(meta, 'value'):
                if meta.value is not None:
                    self.replace_mark(meta.json_name, str(meta.value))

        content = dream.content
        color = self.lucid_dreams_color if dream.lucid else self.normal_dreams_color
        content = f'[color={color}]{content.strip()}[/color]'
        self.replace_mark('content', content)

        self.replace_mark('nb', str(nb))

        anonyms = []
        with open(f'{data_pathname}/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for anonym in anonyms:
            real = anonym['real']
            fake = anonym['anonym']
            if real and fake:
                self.copied = self.copied.replace(real, fake)

        for special_text in self.special_texts:
            self.copied = self.copied.replace(special_text['text'], special_text['bbcode'])

        return self.copied.replace('  ', '\n\n')

    def save(self):
        conf = {'data_pathname': 'data'}
        with open(f"{os.environ['ProgramFiles']}\\Dreams Analyzer\\conf.yml", 'r') as file:
            conf = yaml.safe_load(file)
        data_pathname = conf['data_pathname']

        with open(f"{data_pathname}/templates/{self.filename}", 'wb') as file:
            pickle.dump(self, file)

    def replace_mark(self, mark, replacement):
        self.copied = self.copied.replace('{{'+mark+'}}', replacement)

    def __repr__(self):
        return self.name
