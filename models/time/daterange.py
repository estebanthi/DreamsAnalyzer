import datetime as dt


class Daterange:

    def __init__(self, start, end=dt.datetime.now()):
        self.start = start
        self.end = end

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        max_index = int((self.end - self.start).days)
        if self.index > max_index:
            raise StopIteration

        date = self.start + dt.timedelta(self.index)
        self.index += 1
        return date
