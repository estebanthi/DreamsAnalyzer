import datetime as dt


class RoundableDate(dt.datetime):

    def round(self, to=60):
        seconds = (self.replace(tzinfo=None) - self.min).seconds
        rounding = (seconds + to / 2) // to * to
        return self + dt.timedelta(0, rounding - seconds, -self.microsecond)
    