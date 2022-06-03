from enum import Enum


class TimeResolution(Enum):
    SECONDS = 1
    MINUTES = 1*60
    HOURS = 1*60*60
    DAYS = 1*60*60*24
    WEEKS = 1*60*60*24*7
    MONTHS = 1 * 60 * 60 * 24 * 30
