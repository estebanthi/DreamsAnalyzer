from models.dream import Dream


def get_dreams(data):
    json_dreams = data['dreams']
    return [Dream(json_dream) for json_dream in json_dreams.values()]


def get_normal_dreams(dreams):
    return [dream for dream in dreams if not dream.lucid]


def get_lucid_dreams(dreams):
    return [dream for dream in dreams if dream.lucid]
