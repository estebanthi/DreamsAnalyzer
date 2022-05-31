from models.ui.tabs.tab import Tab


class HomeTab(Tab):

    def __init__(self, data, metas):
        super().__init__()
        self.data = data
        self.metas = metas

    def connect(self):
        pass