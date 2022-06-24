import pickle
import yaml
import os


class Template:

    def __init__(self, filename, name='Template par défaut', content=''):
        self.name = name
        self.content = content
        self.filename = filename

        conf = {'data_pathname': 'data'}
        with open(f"{os.environ['ProgramFiles']}\\Dreams Analyzer\\conf.yml", 'r') as file:
            conf = yaml.safe_load(file)
        self.data_pathname = conf['data_pathname']

    def parse(self, dream, nb=''):
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
        color = 'blue' if dream.lucid else 'green'
        content = f'[color={color}]{content.strip()}[/color]'
        self.replace_mark('content', content)

        self.copied = self.copied.replace('(', '[color=black][i](')
        self.copied = self.copied.replace(')', ')[/i][/color]')

        self.copied = self.copied.replace('[color=black][i](...)[/i][/color]', '(...)')

        self.replace_mark('nb', str(nb))

        anonyms = []
        with open(f'{self.data_pathname}/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for anonym in anonyms:
            real = anonym['real']
            fake = anonym['anonym']
            if real and fake:
                self.copied = self.copied.replace(real, fake)

        return self.copied.replace('  ', '\n\n')

    def save(self):
        with open(f"data/templates/{self.filename}", 'wb') as file:
            pickle.dump(self, file)

    def replace_mark(self, mark, replacement):
        self.copied = self.copied.replace('{{'+mark+'}}', replacement)

    def __repr__(self):
        return self.name
