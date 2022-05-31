from models.exceptions.qerror import QError
from models.ui.qinfo_popup import QInfoPopup
from models.enums import TypeFilterOptions


class DataController:

    def __init__(self):
        self.model = None
        self.view = None

    def notify_no_recent_data_error(self):
        pass

    def notify_credentials_error(self):
        QError('Identifiants Dream Manager incorrects')

    def sync_data(self):
        self.model.remote_load_data()
        if self.model.data:
            QInfoPopup('Données chargées avec succès !')

    def load_last_data(self):
        self.model.load_last_data()
        if self.model.data:
            QInfoPopup('Données chargées avec succès !')

    def filter_dreams(self, start=None, end=None, label=None):
        type_ = TypeFilterOptions.ALL
        self.model.load_last_data()

        if label == 'Lucides':
            type_ = TypeFilterOptions.LUCID
        if label == 'Normal':
            type_ = TypeFilterOptions.NORMAL

        self.model.filter_dreams(start, end, type_)

    def reset_filter(self):
        self.model.load_last_data()
        self.view.dreamTypeSelect.setCurrentText('Tout')

    def connect(self):
        self.model.dataUpdatedSignal.connect(self.view.updateData)
