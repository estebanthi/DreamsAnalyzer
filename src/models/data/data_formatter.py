class DataFormatter:
    color_to_lucidity_mapper = {
        'blue': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'grey': 4,
        'pink': 5,
        'purple': 6,
        'indigo': 7,
        'teal': 8,
        'lime': 9,
        'orange': 10,
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