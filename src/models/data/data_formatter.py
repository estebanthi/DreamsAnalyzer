class DataFormatter:
    color_to_lucidity_mapper = {
        'red': 0,
        'pink': 1,
        'orange': 2,
        'yellow': 3,
        'lime': 4,
        'green': 5,
        'teal': 6,
        'blue': 7,
        'indigo': 8,
        'purple': 9,
        'grey': 10,
    }

    def __init__(self, controller):
        self.controller = controller

    def format(self, data):
        new_data = data
        try:
            for _id, dream in data['dreams'].items():

                if dream['meta']['color']:
                    color = dream['meta']['color']
                    del (new_data['dreams'][_id]['meta']['color'])
                    lucidity = self.color_to_lucidity_mapper[color]
                    new_data['dreams'][_id]['meta']['lucidity'] = lucidity

            return new_data
        except Exception:
            self.controller.notify_data_formatting_error()
            return None