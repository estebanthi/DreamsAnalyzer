from enum import Enum


class TypeFilterOptions(Enum):
    ALL = "Tout"
    NORMAL = "Normaux"
    LUCID = "Lucides"


class DataLoadingMethod(Enum):
    REMOTE = 1
    LOCAL = 2
    LAST_DATA = 3


class MetaType(Enum):
    NUMERIC = 1
    STRING = 2
