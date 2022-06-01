class MetasCollection:

    def __init__(self, metas=None):
        if not metas:
            metas = []
        self.metas = metas

    def __getitem__(self, item):
        return self.metas[item]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            meta = self.metas[self.index]
            self.index += 1
            return meta
        except IndexError:
            raise StopIteration

    def __repr__(self):
        return str([str(meta) for meta in self.metas])

    def append(self, item):
        self.metas.append(item)
