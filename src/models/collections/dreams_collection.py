from models.collections.base_collection import BaseCollection


class DreamsCollection(BaseCollection):

    weekdays = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

    def __init__(self, dreams=None):
        super().__init__(dreams)

    """def get_average_meta(self, meta):
        metas = []
        for dream in self.dreams:
            for dream_meta in dream.metas:
                if dream_meta == meta:
                    metas.append(dream_meta.value)

        return mean(metas)

    def count_dreams(self):
        return len(self.dreams)

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

    def group_by_day(self):
        return {
            day: [dream for dream in self.dreams if dream.date.weekday() == day] for day in range(7)
        }

    def get_lucid_dreams_day(self):

        dreams_by_day = self.group_by_day()

        lucid_dreams_by_day = {day: len(list(filter(lambda dream: dream.lucid, dreams_by_day[day]))) for day in
                               dreams_by_day.keys()}

        return self.weekdays[max(lucid_dreams_by_day, key=lambda day: lucid_dreams_by_day[day])]

    def get_normal_dreams_day(self):
        dreams_by_day = self.group_by_day()

        normal_dreams_by_day = {day: len(list(filter(lambda dream: not dream.lucid, dreams_by_day[day]))) for day in
                                dreams_by_day.keys()}

        return self.weekdays[max(normal_dreams_by_day, key=lambda day: normal_dreams_by_day[day])]

    def get_vivid_dreams_day(self):
        dreams_by_day = self.group_by_day()

        vivid_dreams_by_day = {day: len(list(filter(lambda dream: dream.clear == 4, dreams_by_day[day]))) for day in
                               dreams_by_day.keys()}

        return self.weekdays[max(vivid_dreams_by_day, key=lambda day: vivid_dreams_by_day[day])]

    def get_hh_day(self):
        dreams_by_day = self.group_by_day()

        hh = {day: len(dreams_by_day[day]) for day in dreams_by_day.keys()}

        return self.weekdays[max(hh, key=lambda day: hh[day])]

    def get_dreams_containing_tag(self, tag_label):
        return [dream for dream in self.dreams if tag_label in [tag.label for tag in dream.tags]]

    def get_dreams_not_containing_tag(self, tag_label):
        return [dream for dream in self.dreams if tag_label not in [tag.label for tag in dream.tags]]

    def filter(self, method):
        return DreamsCollection(list(filter(method, self)))

    def group_by_hour(self):
        return {
            hour: [dream for dream in self.dreams if dream.date.hour == hour] for hour in range(24)
        }

    def get_mean_time(self):
        times = [ConvertibleTime(dream.date.time()) for dream in self.dreams]
        seconds = [time.to_seconds() for time in times]

        mean_seconds = mean(seconds)
        timedelta = dt.datetime.fromtimestamp(mean_seconds) - dt.datetime.fromtimestamp(0)

        mean_time = ConvertibleTime.from_timedelta(timedelta)
        return mean_time

    def get_nights(self):
        dates = UniqueList([dream.date.round(86400) for dream in self.dreams])
        nights = []
        for date in dates:
            dreams = self.filter(lambda dream: dream.date.round(86400) == date)
            nights.append(Night(date, dreams))
        return nights

"""