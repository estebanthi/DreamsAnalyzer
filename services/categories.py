from models.dreams.category import Category


def get_categories(json_data):
    json_categories = json_data['category']
    return [Category(json_category) for json_category in json_categories.values()]