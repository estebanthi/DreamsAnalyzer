from collections.abc import Sequence


class UniqueList(Sequence):

    def __init__(self, _list):
        self._list = list(set(_list))

    def __getitem__(self, item):
        return self._list[item]

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self):
            item = self._list[self.index]
            self.index += 1
            return item
        raise StopIteration

    def __repr__(self):
        return str(self._list)
