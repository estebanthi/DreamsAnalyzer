from statistics import mean
from collections import Counter
import datetime as dt
from statistics import mode


from models.collections.dreams_collection import DreamsCollection


class DreamsAnalyzer:

    def __init__(self, dreams):
        self.dreams = dreams

    def get_lucid_dreams_rate(self):
        return len([dream for dream in self.dreams if dream.lucid])/len(self.dreams)*100

    def get_average_dreams_length(self):
        lengths = [len(dream.content.split()) for dream in self.dreams]
        return round(mean(lengths), 2)

    def get_average_dreams_per_nights(self):
        dates = [dream.date.round(84000) for dream in self.dreams]
        if not dates:
            return 0
        counter = Counter(dates)
        dreams_per_night = list(counter.values())
        return round(mean(dreams_per_night), 2)

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

    def get_total_words(self):
        return sum([len(dream.content.split()) for dream in self.dreams])

    def get_hours_counter(self):
        times = [dt.time(dream.date.hour, dream.date.minute) for dream in self.dreams]
        counter = list(Counter(times).items())
        counter = sorted(counter, key=lambda x: x[1], reverse=True)
        return counter

    def get_most_frequent_hour(self):
        counter = self.get_hours_counter()
        return counter[0][0]

    def get_average_meta(self, meta):
        metas = []
        for dream in self.dreams:
            for dream_meta in dream.metas:
                if dream_meta == meta:
                    metas.append(dream_meta.value)
        return mean(metas)

    def get_all_average_metas(self):
        metas = {}
        for meta in self.dreams[0].metas:
            metas[meta.name] = []

        for dream in self.dreams:
            for meta in dream.metas:
                metas[meta.name].append(meta.value)

        for name, values in metas.items():
            if values:
                if type(values[0]) is str:
                    metas[name] = mode(values)
                else:
                    metas[name] = float(mean(values))

        return metas

    def get_values_over_time(self, time_intervals, method):
        values = []
        dreams_collection = DreamsCollection()
        for interval in time_intervals:
            for dream in self.dreams:
                if dream.date in interval:
                    dreams_collection.append(dream)
            new_analyzer = DreamsAnalyzer(dreams_collection)
            values.append(getattr(new_analyzer, method)())
        return values

    def count_dreams(self):
        return len(self.dreams)

    def count_lucid_dreams(self):
        return len(self.dreams.filter(lambda dream: dream.lucid))

    def get_meta_over_time(self, time_intervals, meta):
        values = []
        dreams_collection = DreamsCollection()
        for interval in time_intervals:
            for dream in self.dreams:
                if dream.date in interval:
                    dreams_collection.append(dream)
            new_analyzer = DreamsAnalyzer(dreams_collection)
            values.append(new_analyzer.get_average_meta(meta))
        return values