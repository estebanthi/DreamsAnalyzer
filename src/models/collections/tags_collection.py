class TagsCollection:

    def __init__(self, tags=None):
        self.tags = tags
        if not tags:
            self.tags = []

    def __getitem__(self, item):
        return self.tags[item]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            tag = self.tags[self.index]
            self.index += 1
            return tag
        except IndexError:
            raise StopIteration

    def __contains__(self, item):
        return item in [tag.label for tag in self.tags]