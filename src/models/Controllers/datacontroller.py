import datetime as dt
import yaml
import os
import pickle


from PyQt5 import QtCore


from models.ui.popups.qerror import QError
from models.ui.popups.qinfo_popup import QInfoPopup
from models.enums import TypeFilterOptions
from models.time.daterange import Daterange
from models.time.timerange import TimeResolution
from models.dreams_analyzer import DreamsAnalyzer
from models.template import Template
from models.dataclasses.meta import Meta
from models.enums import MetaType
from models.ui.popups.custom_chart_popup import CustomChartPopup


class DataController(QtCore.QObject):

    resolutionChangedSignal = QtCore.pyqtSignal()
    anonymsUpdatedSignal = QtCore.pyqtSignal()
    templatesUpdatedSignal = QtCore.pyqtSignal()
    chartsUpdatedSignal = QtCore.pyqtSignal()
    updateMetasSignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.model = None
        self.view = None

        conf = {'data_pathname': 'data'}
        with open('conf.yml', 'r') as file:
            conf = yaml.safe_load(file)
        self.data_pathname = conf['data_pathname']

    def control_data(self):
        if not self.model.data:
            QError("Veuillez d'abord charger vos données")
            return False
        return True

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

    def notify_synced_successfully(self):
        QInfoPopup('Synchronisation avec Dream Manager réalisée avec succès')

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
        if self.control_data():
            self.model.load_last_data()
            self.view.dreamTypeSelect.setCurrentText('Tout')

    def handle_resolution_changed(self):
        if self.model.data:
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

    def get_other_plots(self):

        charts = []
        with open(f'{self.data_pathname}/charts.yml', 'r') as file:
            charts = yaml.safe_load(file)
        return charts

    def save_password(self, password):
        data = None
        with open(f'{self.data_pathname}/credentials.yml', 'r') as file:
            data = yaml.safe_load(file)
        if data:
            with open(f'{self.data_pathname}/credentials.yml', 'w') as file:
                data['password'] = password
                yaml.safe_dump(data, file)

    def save_email(self, email):
        data = None
        with open(f'{self.data_pathname}/credentials.yml', 'r') as file:
            data = yaml.safe_load(file)
        if data:
            with open(f'{self.data_pathname}/credentials.yml', 'w') as file:
                data['email'] = email
                yaml.safe_dump(data, file)

    def get_anonyms(self):
        with open(f'{self.data_pathname}/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)
            return anonyms

    def get_next_anonym_id(self):
        anonyms = []
        with open(f'{self.data_pathname}/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for i in range(len(anonyms)):
            if i not in [anonym['id_'] for anonym in anonyms]:
                return i
        return 0

    def delete_anonym(self, id_):
        anonyms = []
        with open(f'{self.data_pathname}/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for index, anonym in enumerate(anonyms):
            if anonym['id_'] == id_:
                del(anonyms[index])

        with open(f'{self.data_pathname}/anonyms.yml', 'w') as file:
            yaml.safe_dump(anonyms, file)

        self.anonymsUpdatedSignal.emit()

    def update_real(self, id_, real):
        anonyms = []
        with open(f'{self.data_pathname}/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for index, anonym in enumerate(anonyms):
            if anonym['id_'] == id_:
                anonyms[index]['real'] = real

        with open(f'{self.data_pathname}/anonyms.yml', 'w') as file:
            yaml.safe_dump(anonyms, file)

    def update_anonym(self, id_, anonym):
        anonyms = []
        with open(f'{self.data_pathname}/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for index, record in enumerate(anonyms):
            if record['id_'] == id_:
                anonyms[index]['anonym'] = anonym

        with open(f'{self.data_pathname}/anonyms.yml', 'w') as file:
            yaml.safe_dump(anonyms, file)

    def add_anonym(self):
        id_ = self.get_next_anonym_id()

        anonyms = []
        with open(f'{self.data_pathname}/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        anonyms.append({'id_': id_, 'real': '', 'anonym': ''})

        with open(f'{self.data_pathname}/anonyms.yml', 'w') as file:
            yaml.safe_dump(anonyms, file)

        return id_

    def get_templates(self):
        filenames = os.listdir(f'{self.data_pathname}/templates')

        templates = []
        for filename in filenames:
            with open(f'{self.data_pathname}/templates/{filename}', 'rb') as file:
                templates.append(pickle.load(file))
        return templates

    def save_template(self, template):
        if template.name == '':
            QError("Veuillez donner un nom à votre template")
            return
        try:
            template.save()
        except Exception:
            QError("Erreur lors de l'enregistrement du template")
            return
        QInfoPopup("Template sauvegardé avec succès")
        self.templatesUpdatedSignal.emit()

    def delete_template(self, template):
        if template:
            try:
                os.remove(f"data/templates/{template.filename}")
            except Exception:
                QError("Erreur lors de la suppression de votre template")
                return
        QInfoPopup("Template supprimé avec succès")
        self.templatesUpdatedSignal.emit()

    def control_post_popup(self, index):
        if index <= -1:
            QError("Veuillez créer un template avant de générer un post")
            return
        return True

    def handle_autosync_changed(self, state):
        state = True if state == 2 else False
        with open(f'{self.data_pathname}/config.yml', 'r') as file:
            data = yaml.safe_load(file)

            with open(f'{self.data_pathname}/config.yml', 'w') as wfile:
                data['autosync'] = state
                yaml.safe_dump(data, wfile)

    def delete_chart(self, id_):
        charts = []
        with open(f'{self.data_pathname}/charts.yml', 'r') as file:
            charts = yaml.safe_load(file)

        for index, chart in enumerate(charts):
            if chart['id_'] == id_:
                del(charts[index])

        with open(f'{self.data_pathname}/charts.yml', 'w') as file:
            yaml.safe_dump(charts, file)

        self.chartsUpdatedSignal.emit()

    def get_next_chart_id(self):
        charts = []
        with open(f'{self.data_pathname}/charts.yml', 'r') as file:
            charts = yaml.safe_load(file)

        for i in range(len(charts)):
            if i not in [chart['id_'] for chart in charts]:
                return i
        return len(charts)

    def delete_chart(self, id_):
        charts = []
        with open(f'{self.data_pathname}/charts.yml', 'r') as file:
            charts = yaml.safe_load(file)

        for index, chart in enumerate(charts):
            if chart['id_'] == id_:
                del(charts[index])

        with open(f'{self.data_pathname}/charts.yml', 'w') as file:
            yaml.safe_dump(charts, file)

        self.chartsUpdatedSignal.emit()

    def save_chart(self, chart):
        charts = []
        with open(f'{self.data_pathname}/charts.yml', 'r') as file:
            charts = yaml.safe_load(file)

        id_ = chart['id_']

        if id_ < len(charts):
            charts[id_] = chart

        else:
            charts.append(chart)

        with open(f'{self.data_pathname}/charts.yml', 'w') as file:
            yaml.safe_dump(charts, file)

        self.chartsUpdatedSignal.emit()

    def get_metas(self):
        metas = []
        with open(f'{self.data_pathname}/metas.dat', 'rb') as file:
            metas = pickle.load(file)
        return metas

    def update_meta(self, field, id_, value):
        metas = []
        with open(f'{self.data_pathname}/metas.dat', 'rb') as file:
            metas = pickle.load(file)


        for index, meta in enumerate(metas):
            if meta.id_ == id_:
                setattr(meta, field, value)

        with open(f'{self.data_pathname}/metas.dat', 'wb') as file:
            pickle.dump(metas, file)

    def notify_metas_error(self, initial_metas, final_metas):
        metas = [meta.name for meta in initial_metas if meta not in final_metas]
        QError(f"Les métadonnées suivantes ne sont pas valides : {' - '.join(metas)}")

    def delete_meta(self, id_):
        metas = []
        with open(f'{self.data_pathname}/metas.dat', 'rb') as file:
            metas = pickle.load(file)

        for index, meta in enumerate(metas):
            if meta.id_ == id_:
                del(metas.items[index])

        with open(f'{self.data_pathname}/metas.dat', 'wb') as file:
            pickle.dump(metas, file)

        self.updateMetasSignal.emit()

    def get_next_meta_id(self):
        metas = []
        with open(f'{self.data_pathname}/metas.dat', 'rb') as file:
            metas = pickle.load(file)

        for i in range(len(metas)):
            if i not in [meta.id_ for meta in metas]:
                return i
        return len(metas)

    def add_meta(self):
        with open(f'{self.data_pathname}/metas.dat', 'rb') as file:
            metas = pickle.load(file)
        id_ = self.get_next_meta_id()

        meta = Meta('', '', MetaType.NUMERIC, id_=id_)

        if id_ < len(metas):
            metas[id_] = meta

        else:
            metas.append(meta)

        with open(f'{self.data_pathname}/metas.dat', 'wb') as file:
            pickle.dump(metas, file)

        self.updateMetasSignal.emit()

    def open_edit_chart_popup(self, chart):
        if self.model.data:
            popup = CustomChartPopup(self, chart)
            popup.show()
        else:
            QError("Veuillez charger des données avant d'effectuer cette action")

    def connect(self):
        self.model.dataUpdatedSignal.connect(self.view.updateData)
        self.resolutionChangedSignal.connect(self.view.updateData)
        self.anonymsUpdatedSignal.connect(self.view.updateAnonyms)
        self.templatesUpdatedSignal.connect(self.view.updateTemplates)
        self.chartsUpdatedSignal.connect(self.view.updateCharts)
        self.updateMetasSignal.connect(self.view.updateMetas)
