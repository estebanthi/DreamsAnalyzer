from models.collections.base_collection import BaseCollection
from models.collections.metas_collection import MetasCollection
from models.collections.unique_list import UniqueList
from models.collections.night import Night


class DreamsCollection(BaseCollection):

    weekdays = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

    def __init__(self, dreams=None):
        super().__init__(dreams)
        self.metas = MetasCollection()
        if dreams:
            self.metas = dreams[0].metas

    def group_by_day(self):
        return {
            day: [dream for dream in self.items if dream.date.weekday() == day] for day in range(7)
        }

    def group_by_hour(self):
        return {
            hour: [dream for dream in self.items if dream.date.hour == hour] for hour in range(24)
        }

    def get_nights(self):
        dates = UniqueList([dream.date.round(86400) for dream in self.items])
        nights = []
        for date in dates:
            dreams = self.filter(lambda dream: dream.date.round(86400) == date)
            nights.append(Night(date, dreams))
        return nights

