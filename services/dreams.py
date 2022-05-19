from statistics import mean


from models.dream import Dream
from services.config import load_config


def get_dreams(data):
    json_dreams = data['dreams']
    return [Dream(json_dream) for json_dream in json_dreams.values()]


def get_normal_dreams(dreams):
    return [dream for dream in dreams if not dream.lucid]


def get_lucid_dreams(dreams):
    return [dream for dream in dreams if dream.lucid]


def get_hypnagogic_dreams(dreams):
    config = load_config()
    return [dream for dream in dreams if dream.color == config['hh_color']]


def get_average_meta(meta, dreams):
    average = mean([getattr(dream, meta) for dream in dreams if getattr(dream, meta) > -1])
    return round(average, 2)
