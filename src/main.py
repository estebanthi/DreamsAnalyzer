from src.models.time.daterange import Daterange


import datetime as dt


daterange = Daterange(dt.datetime(2022, 1, 1))

for date in daterange:
    print(date)
