class Night:

    def __init__(self, date, dreams):
        self.date = date
        self.dreams = dreams

        for dream in dreams:
            if dream.date.round(86400) != date:
                raise ValueError(f"Dream {dream.title} is not in night {date}")

    def get_bbcode(self, intro='', conclusion='', comments=None):
        if not comments:
            comments = ['' for dream in self.dreams]

        dreams_bbcodes = [dream.get_bbcode(comments[i]) for dream, i in zip(self.dreams, range(len(comments)))]

        return '\n\n'.join([intro, *dreams_bbcodes, conclusion])

    def __getitem__(self, item):
        return self.dreams[item]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.dreams):
            raise StopIteration
        dream = self.dreams[self.index]
        self.index += 1
        return dream