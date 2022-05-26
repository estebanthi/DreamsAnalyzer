import pickle


class Template:

    def __init__(self, content):
        self.content = content

    def parse(self, dream):
        print(dream)
        self.replace_mark('type', 'RL' if dream.lucid else 'RN')
        self.replace_mark('title', dream.title)
        self.replace_mark('clear', str(dream.clear))
        self.replace_mark('mood', str(dream.mood))
        self.replace_mark('lucidity', dream.lucidity)
        self.replace_mark('tag', " - ".join([tag.label for tag in dream.tags]))
        self.replace_mark('time', str(dream.date.hour)+'H'+str(dream.time.minute))
        return self.content

    @staticmethod
    def load(pathname):
        with open(pathname, 'rb') as file:
            return pickle.load(file)

    def save(self, pathname):
        with open(pathname, 'wb') as file:
            pickle.dump(self, file)

    def replace_mark(self, mark, replacement):
        self.content = self.content.replace('{{'+mark+'}}', replacement)
