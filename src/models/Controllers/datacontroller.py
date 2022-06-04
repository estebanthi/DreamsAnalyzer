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

class DataController(QtCore.QObject):

    resolutionChangedSignal = QtCore.pyqtSignal()
    anonymsUpdatedSignal = QtCore.pyqtSignal()
    templatesUpdatedSignal = QtCore.pyqtSignal()

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

    def get_other_plots(self):
        return [
            {'title': "Méthodes d'inductions", 'tags': ['WILD', 'DILD'], 'colors': ['teal', 'brown'], 'filter': {}},
            {'title': "Proportion de RL WBTB", 'tags': ['WBTB', 'Pas WBTB'], 'colors': ['aquamarine', 'mediumseagreen'], 'filter': {'lucid': True}},
            {'title': "Proportion de rêves VIVID", 'tags': ['VIVID', 'Pas VIVID'], 'colors': ['orange', 'brown'],
             'filter': {}},
        ]

    def save_password(self, password):
        data = None
        with open('data/credentials.yml', 'r') as file:
            data = yaml.safe_load(file)
        if data:
            with open('data/credentials.yml', 'w') as file:
                data['password'] = password
                yaml.safe_dump(data, file)

    def save_email(self, email):
        data = None
        with open('data/credentials.yml', 'r') as file:
            data = yaml.safe_load(file)
        if data:
            with open('data/credentials.yml', 'w') as file:
                data['email'] = email
                yaml.safe_dump(data, file)

    def get_anonyms(self):
        with open('data/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)
            return anonyms

    def get_next_anonym_id(self):
        anonyms = []
        with open('data/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for i in range(len(anonyms)):
            if i not in [anonym['id_'] for anonym in anonyms]:
                return i
        return 0

    def delete_anonym(self, id_):
        anonyms = []
        with open('data/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for index, anonym in enumerate(anonyms):
            if anonym['id_'] == id_:
                del(anonyms[index])

        with open('data/anonyms.yml', 'w') as file:
            yaml.safe_dump(anonyms, file)

        self.anonymsUpdatedSignal.emit()

    def update_real(self, id_, real):
        anonyms = []
        with open('data/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for index, anonym in enumerate(anonyms):
            if anonym['id_'] == id_:
                anonyms[index]['real'] = real

        with open('data/anonyms.yml', 'w') as file:
            yaml.safe_dump(anonyms, file)

    def update_anonym(self, id_, anonym):
        anonyms = []
        with open('data/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        for index, record in enumerate(anonyms):
            if record['id_'] == id_:
                anonyms[index]['anonym'] = anonym

        with open('data/anonyms.yml', 'w') as file:
            yaml.safe_dump(anonyms, file)

    def add_anonym(self):
        id_ = self.get_next_anonym_id()

        anonyms = []
        with open('data/anonyms.yml', 'r') as file:
            anonyms = yaml.safe_load(file)

        anonyms.append({'id_': id_, 'real': '', 'anonym': ''})

        with open('data/anonyms.yml', 'w') as file:
            yaml.safe_dump(anonyms, file)

        return id_

    def get_templates(self):
        filenames = os.listdir('data/templates')

        templates = []
        for filename in filenames:
            with open(f'data/templates/{filename}', 'rb') as file:
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

    def connect(self):
        self.model.dataUpdatedSignal.connect(self.view.updateData)
        self.resolutionChangedSignal.connect(self.view.updateData)
        self.anonymsUpdatedSignal.connect(self.view.updateAnonyms)
        self.templatesUpdatedSignal.connect(self.view.updateTemplates)
