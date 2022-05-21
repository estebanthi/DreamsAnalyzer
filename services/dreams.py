from statistics import mean
from collections import Counter


from models.dreams.dream import Dream
from services.config import load_config
from utils.dates import round_time


def get_dreams(data):
    config = load_config()
    json_dreams = data['dreams']
    dreams = [Dream(json_dream) for json_dream in json_dreams.values()]
    return [dream for dream in dreams if dream.color != config['hh_color']]


def get_normal_dreams(dreams):
    return [dream for dream in dreams if not dream.lucid]


def get_lucid_dreams(dreams):
    return [dream for dream in dreams if dream.lucid]


def get_hh(data):
    config = load_config()
    json_dreams = data['dreams']
    dreams = [Dream(json_dream) for json_dream in json_dreams.values()]
    return [dream for dream in dreams if dream.color == config['hh_color']]


def get_average_meta(meta, dreams):
    average = mean([getattr(dream, meta) for dream in dreams if getattr(dream, meta) > -1])
    return round(average, 2)


def get_average_dreams_per_nights(dreams):
    dates = [round_time(dream.date, 84000) for dream in dreams]
    counter = Counter(dates)
    dreams_per_night = list(counter.values())
    return round(mean(dreams_per_night), 2)


def get_tags_counter(dreams, sort=True):
    tags = [tag for dream in dreams for tag in dream.tags]
    counter = list(Counter(tags).items())
    if sort:
        counter = sorted(counter, key=lambda x: x[1], reverse=True)
    return counter


def get_most_frequent_tag(dreams):
    counter = get_tags_counter(dreams)
    return counter[0][0]


def get_categories_counter(dreams):
    tags = [tag for dream in dreams for tag in dream.tags]
    categories = [tag.category for tag in tags]
    return categories


def get_average_dreams_length(dreams):
    lengths = [len(dream.content.split()) for dream in dreams]
    return round(mean(lengths), 2)