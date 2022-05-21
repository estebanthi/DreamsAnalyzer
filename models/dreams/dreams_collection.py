from statistics import mean
from collections import Counter


class DreamsCollection:

    def __init__(self, dreams):
        self.dreams = dreams

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.dreams):
            raise StopIteration
        dream = self.dreams[self.index]
        self.index += 1
        return dream

    def __len__(self):
        return len(self.dreams)

    def __getitem__(self, item):
        return self.dreams[item]

    def get_average_meta(self, meta):
        average = mean([getattr(dream, meta) for dream in self.dreams if getattr(dream, meta) > -1])
        return round(average, 2)

    def get_average_dreams_per_nights(self):
        dates = [dream.date.round(84000) for dream in self.dreams]
        counter = Counter(dates)
        dreams_per_night = list(counter.values())
        return round(mean(dreams_per_night), 2)

    def get_average_dreams_length(self):
        lengths = [len(dream.content.split()) for dream in self.dreams]
        return round(mean(lengths), 2)

    def get_tags_counter(self):
        tags = [tag for dream in self.dreams for tag in dream.tags]
        counter = list(Counter(tags).items())
        counter = sorted(counter, key=lambda x: x[1], reverse=True)
        return counter

    def get_most_frequent_tag(self):
        counter = self.get_tags_counter()
        return counter[0][0]

    def get_categories_counter(self):
        tags = [tag for dream in self.dreams for tag in dream.tags]
        categories = [tag.category for tag in tags]
        counter = list(Counter(categories).items())
        counter = sorted(counter, key=lambda x: x[1], reverse=True)
        return counter

    def get_most_frequent_category(self):
        counter = self.get_categories_counter()
        if counter[0][0] is None:
            return counter[1][0]
        return counter[0][0]

