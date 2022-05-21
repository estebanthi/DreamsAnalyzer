import datetime as dt


def round_time(date=None, round_to=60):
    """Round a datetime object to any time lapse in seconds
    dt : datetime.datetime object, default now.
    roundTo : Closest number of seconds to round to, default 1 minute.
    Author: Thierry Husson 2012 - Use it as you want but don't blame me.
    """



def get_timeranges(date):
    start_date = round_time(date - dt.timedelta(minutes=15))
    return [start_date + dt.timedelta(minutes=1) * i for i in range(31)]


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + dt.timedelta(n)
