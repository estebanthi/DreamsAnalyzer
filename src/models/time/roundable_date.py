import datetime as dt


class RoundableDate(dt.datetime):

    def round(self, to=60):
        seconds = (self.replace(tzinfo=None) - self.min).seconds
        rounding = (seconds + to / 2) // to * to
        return self + dt.timedelta(0, rounding - seconds, -self.microsecond)

    def is_same_week(self, other):
        return self.isocalendar()[0] == other.isocalendar()[0] and self.isocalendar()[1] == other.isocalendar()[1]

    def is_same_day(self, other):
        return self.isocalendar()[0] == other.isocalendar()[0] and self.isocalendar()[1] == other.isocalendar()[1] \
               and self.isocalendar()[2] == other.isocalendar()[2]

    def __hash__(self):
        return int((self - dt.datetime.fromtimestamp(0)).total_seconds())
