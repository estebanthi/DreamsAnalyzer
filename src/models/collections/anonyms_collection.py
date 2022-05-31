class AnonymsCollection:

    def __init__(self, anonyms=None):
        self.anonyms = anonyms
        if not anonyms:
            self.anonyms = []

    def __getitem__(self, item):
        return self.anonyms[item]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            anonym = self.anonyms[self.index]
            self.index += 1
            return anonym
        except IndexError:
            raise StopIteration
