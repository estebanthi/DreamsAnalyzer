from statistics import mean
from collections import Counter
import datetime as dt


from models.time.daterange import Daterange


class DreamsCollection:

    weekdays = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

    def __init__(self, dreams=None):
        if dreams:
            self.dreams = [dream for dream in dreams]
        if not dreams:
            self.dreams = []

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

    def append(self, dream):
        self.dreams.append(dream)

    def get_average_meta(self, meta):
        average = mean([getattr(dream, meta) for dream in self.dreams if getattr(dream, meta) > -1])
        return round(average, 2)

    def get_average_dreams_per_nights(self):
        dates = [dream.date.round(84000) for dream in self.dreams]
        if not dates:
            return 0
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

    def count_dreams(self):
        return len(self.dreams)

    def get_lucid_dreams_rate(self):
        return len([dream for dream in self.dreams if dream.lucid])/len(self)*100

    def get_average_clear(self):
        return self.get_average_meta('clear')

    def get_average_mood(self):
        return self.get_average_meta('mood')

    def get_average_lucidity(self):
        return self.get_average_meta('lucidity')

    def get_vivid_dreams(self):
        return [dream for dream in self.dreams if dream.clear == 4]

    def get_dilds(self):
        return [dream for dream in self.dreams if 'DILD' in [tag.label for tag in dream.tags]]

    def get_wilds(self):
        return [dream for dream in self.dreams if 'WILD' in [tag.label for tag in dream.tags]]

    def get_dreams_by_day(self):
        return {
            day: [dream for dream in self.dreams if dream.date.weekday() == day] for day in range(7)
        }

    def get_lucid_dreams_day(self):

        dreams_by_day = self.get_dreams_by_day()

        lucid_dreams_by_day = {day: len(list(filter(lambda dream: dream.lucid, dreams_by_day[day]))) for day in
                               dreams_by_day.keys()}

        return self.weekdays[max(lucid_dreams_by_day, key=lambda day: lucid_dreams_by_day[day])]

    def get_normal_dreams_day(self):
        dreams_by_day = self.get_dreams_by_day()

        normal_dreams_by_day = {day: len(list(filter(lambda dream: not dream.lucid, dreams_by_day[day]))) for day in
                                dreams_by_day.keys()}

        return self.weekdays[max(normal_dreams_by_day, key=lambda day: normal_dreams_by_day[day])]

    def get_vivid_dreams_day(self):
        dreams_by_day = self.get_dreams_by_day()

        vivid_dreams_by_day = {day: len(list(filter(lambda dream: dream.clear == 4, dreams_by_day[day]))) for day in
                               dreams_by_day.keys()}

        return self.weekdays[max(vivid_dreams_by_day, key=lambda day: vivid_dreams_by_day[day])]

    def get_hh_day(self):
        dreams_by_day = self.get_dreams_by_day()

        hh = {day: len(dreams_by_day[day]) for day in dreams_by_day.keys()}

        return self.weekdays[max(hh, key=lambda day: hh[day])]

