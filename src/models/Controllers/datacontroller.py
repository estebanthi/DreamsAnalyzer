from models.ui.popups.qerror import QError
from models.ui.popups.qinfo_popup import QInfoPopup
from models.enums import TypeFilterOptions


class DataController:

    def __init__(self):
        self.model = None
        self.view = None

    def notify_no_recent_data_error(self):
        pass

    def notify_credentials_error(self):
        QError('Identifiants Dream Manager incorrects')

    def notify_data_decoding_error(self):
        QError('Erreur lors du décodage de vos données')

    def notify_data_formatting_error(self):
        QError('Erreur lors du formattage de vos données')

    def notify_file_not_found_error(self):
        QError('Impossible de trouver le fichier de vos données')

    def notify_io_error(self):
        QError('Impossible de charger vos données')

    def sync_data(self):
        success = self.model.remote_load_data()
        if success:
            QInfoPopup('Données chargées avec succès !')

    def load_last_data(self):
        self.model.load_last_data()
        if self.model.data:
            print(self.model.data)
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
