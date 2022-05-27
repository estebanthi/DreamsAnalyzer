import datetime as dt


class ConvertibleTime(dt.time):

    def __new__(cls, time):
        self = super().__new__(cls, hour=time.hour, minute=time.minute, second=time.second)
        return self

    def to_seconds(self):
        return int(dt.timedelta(hours=self.hour, minutes=self.minute, seconds=self.second).total_seconds())

    @staticmethod
    def from_timedelta(timedelta):
        return ConvertibleTime((dt.datetime.min + timedelta).time())
