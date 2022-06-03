import datetime as dt


from PyQt5 import QtCore


from models.ui.popups.qerror import QError
from models.ui.popups.qinfo_popup import QInfoPopup
from models.enums import TypeFilterOptions
from models.time.daterange import Daterange
from models.time.timerange import TimeResolution
from models.dreams_analyzer import DreamsAnalyzer

class DataController(QtCore.QObject):

    resolutionChangedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
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

    def handle_resolution_changed(self):
        self.resolutionChangedSignal.emit()

    def parse_resolution(self, resolution):
        if resolution == 'Jour':
            return TimeResolution.DAYS
        if resolution == 'Semaine':
            return TimeResolution.WEEKS
        if resolution == 'Mois':
            return TimeResolution.MONTHS

    def get_plot_params(self, resolution):
        resolution = resolution.value
        dates = [dream.date.round(TimeResolution.DAYS.value) for dream in self.model.data.dreams]
        sorted_dates = sorted(dates)

        start = sorted_dates[0]

        daterange = Daterange(start, dt.datetime.now(), resolution)
        x = [date for date in daterange]
        time_intervals = daterange.split(resolution)

        return x, time_intervals

    def get_values_over_time(self, resolution, method):
        analyzer = DreamsAnalyzer(self.model.data.dreams)

        time_intervals = self.get_plot_params(resolution)[1]
        return analyzer.get_values_over_time(time_intervals, method)

    def get_metas_over_time(self, resolution):
        analyzer = DreamsAnalyzer(self.model.data.dreams)

        time_intervals = self.get_plot_params(resolution)[1]

        metas = {}
        for index, meta in enumerate(list(self.model.data.dreams.metas)):
            metas[meta.name] = analyzer.get_meta_over_time(time_intervals, meta)
        return metas




    def connect(self):
        self.model.dataUpdatedSignal.connect(self.view.updateData)
        self.resolutionChangedSignal.connect(self.view.updateData)
