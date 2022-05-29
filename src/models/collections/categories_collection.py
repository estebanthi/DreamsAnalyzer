class CategoriesCollection:

    def __init__(self, categories=None):
        self.categories = categories
        if not categories:
            self.categories = []

    def __getitem__(self, item):
        return self.categories[item._id]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            category = self.categories[self.index]
            self.index += 1
            return category
        except IndexError:
            raise StopIteration
