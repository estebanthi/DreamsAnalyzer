import pickle


from models.anonymisator import Anonymisator


class Template:

    def __init__(self, content):
        self.content = content

    def parse(self, dream, nb=''):
        self.copied = self.content
        self.replace_mark('type', 'RL' if dream.lucid else 'RN')
        self.replace_mark('title', dream.title)
        self.replace_mark('clear', str(dream.clear))
        self.replace_mark('mood', str(dream.mood))
        self.replace_mark('lucidity', str(dream.lucidity))
        self.replace_mark('tags', " - ".join([tag.label for tag in dream.tags]))
        self.replace_mark('time', str(dream.date.hour)+'H'+str(dream.date.minute))

        content = dream.content
        color = 'blue' if dream.lucid else 'green'
        content = f'[color={color}]{content}[/color]'
        self.replace_mark('content', content)
        self.replace_mark('nb', str(nb))

        anonymisator = Anonymisator()
        records = anonymisator.get_records()
        for record in records:
            for real, fake in record.items():
                if real and fake:
                    self.copied = self.copied.replace(real, fake)

        return self.copied

    @staticmethod
    def load(pathname):
        with open(pathname, 'rb') as file:
            return pickle.load(file)

    def save(self, pathname):
        with open(pathname, 'wb') as file:
            pickle.dump(self, file)

    def replace_mark(self, mark, replacement):
        self.copied = self.copied.replace('{{'+mark+'}}', replacement)
