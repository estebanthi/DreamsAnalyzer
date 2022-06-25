from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox
from PyQt5.QtCore import Qt

from ui.custom_chart_popup import Ui_MainWindow
from models.ui.widgets.custom_chart_tag_widget import CustomChartTagWidget
from mplwidget import MplWidget
from models.ui.qt_utils import clearLayout
from models.dreams_analyzer import DreamsAnalyzer

import random


class CustomChartPopup(QMainWindow, Ui_MainWindow):

    def __init__(self, controller, chart=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.typeCombo.addItems(['Camembert', 'Barres'])

        if chart:
            if chart['type'] == 'bar':
                self.barZone.addWidget(QLabel('Abscisse'))

                self.comboBox = QComboBox()
                self.comboBox.addItems(['Jours', 'Heures'])
                self.barZone.addWidget(self.comboBox)
                self.typeCombo.setCurrentIndex(1)
                self.comboBox.setCurrentIndex(0 if chart['x'] == 'days' else 1)
                self.comboBox.currentIndexChanged.connect(self.preview)

        self.controller = controller
        self.chart = chart

        if self.chart:
            self.setup()

        dreams_analyzer = DreamsAnalyzer(self.controller.model.data.dreams)
        categories = [category[0].label for category in dreams_analyzer.get_categories_counter() if category[0]]
        self.categoriesComboBox.addItems(categories)
        self.categoriesComboBox.setCurrentIndex(-1)

        self.saveButton.clicked.connect(self.save)
        self.addTagButton.clicked.connect(
            lambda x: self.tagsLayout.addWidget(CustomChartTagWidget(self, self.controller)))
        self.titleEdit.textChanged.connect(self.preview)
        self.categoriesComboBox.currentTextChanged.connect(self.addCategory)
        self.deleteAll.clicked.connect(self.deleteAll_)
        self.typeCombo.currentIndexChanged.connect(self.changeType)


    def changeType(self, index):
        if index == 0:
            clearLayout(self.barZone)
        if index == 1:
            self.barZone.addWidget(QLabel('Abscisse'))

            self.comboBox = QComboBox()
            self.comboBox.addItems(['Jours', 'Heures'])
            self.barZone.addWidget(self.comboBox)
            self.comboBox.currentIndexChanged.connect(self.preview)

        self.preview()

    def setup(self):
        self.titleEdit.setText(self.chart['title'])

        tags = self.chart['tags']
        for tag in tags:
            self.tagsLayout.addWidget(CustomChartTagWidget(self, self.controller, tag))

        self.preview()

    def get_graph(self):
        tags = [self.tagsLayout.itemAt(i).widget().get_tag() for i in range(self.tagsLayout.count())]
        title = self.titleEdit.text()
        type_ = 'pie' if self.typeCombo.currentIndex() == 0 else 'bar'
        x = None
        if self.typeCombo.currentIndex() == 1:
            x = 'days' if self.comboBox.currentIndex() == 0 else 'hours'
            
        if self.chart:
            id_ = self.chart['id_']
        else:
            id_ = self.controller.get_next_chart_id()

        return {'id_': id_, 'title': title, 'tags': tags, 'type': type_, 'x': x}

    def save(self):
        self.controller.save_chart(self.get_graph())
        self.destroy()

    def preview(self):
        if self.typeCombo.currentIndex() == 0:
            self.previewPie()
        else:
            self.previewBar()

    def previewPie(self):
        clearLayout(self.previewLayout)
        self.previewLayout.setAlignment(Qt.AlignCenter)

        chart = self.get_graph()

        dreams = self.controller.model.data.dreams

        tags = chart['tags']

        labels = [("Pas " + tag[0] if tag[1] == 'NOT IN' else tag[0]) for tag in tags]
        colors = [tag[2] for tag in tags]

        collections = []
        for tag in tags:
            filter = tag[3]
            collection = dreams

            if filter:
                if filter['lucid'] is True:
                    collection = dreams.filter(lambda dream: dream.lucid)
                if filter['lucid'] is False:
                    collection = dreams.filter(lambda dream: not dream.lucid)

            collections.append(collection)

        values = []
        for tag, collection in zip(tags, collections):
            value = 0
            if tag[0] == 'RL':
                value = len(collection.filter(lambda dream: dream.lucid))
            elif tag[0] == 'RN':
                value = len(collection.filter(lambda dream: not dream.lucid))
            elif tag[1] == 'NOT IN':
                value = len(collection.filter(lambda dream: tag[0] not in dream.tags))
            elif tag[1] == 'IN':
                value = len(collection.filter(lambda dream: tag[0] in dream.tags))
            values.append(value)

        widget = MplWidget()

        widget.pie(values, colors=colors, legend_labels=labels, bbox_to_anchor=(1.05, 1))
        widget.setTitle(chart['title'])

        self.previewLayout.addWidget(widget)

    def previewBar(self):
        clearLayout(self.previewLayout)

        bar = self.get_graph()
        barType = bar['x']

        if not self.controller.model.data:
            return

        dreams = self.controller.model.data.dreams

        tags = bar['tags']

        labels = [("Pas " + tag[0] if tag[1] == 'NOT IN' else tag[0]) for tag in tags]
        colors = [tag[2] for tag in tags]

        collections = []

        for tag in tags:
            filter = tag[3]
            collection = dreams

            if filter:
                if filter['lucid'] is True:
                    collection = dreams.filter(lambda dream: dream.lucid)
                if filter['lucid'] is False:
                    collection = dreams.filter(lambda dream: not dream.lucid)

            collections.append(collection)

        for index, collection in enumerate(collections):
            if barType == 'days':
                collections[index] = collection.group_by_day()
            if barType == 'hours':
                collections[index] = collection.group_by_hour()

        values = []
        for tag, collection in zip(tags, collections):

            if tag[0] == 'RL':
                if barType == 'days':
                    values_per_x = {day: len(collection[day].filter(lambda dream: dream.lucid)) for day in range(7)}
                else:
                    values_per_x = {hour: len(collection[hour].filter(lambda dream: dream.lucid)) for hour in range(24)}

            elif tag[0] == 'RN':
                if barType == 'days':
                    values_per_x = {day: len(collection[day].filter(lambda dream: not dream.lucid)) for day in range(7)}
                else:
                    values_per_x = {hour: len(collection[hour].filter(lambda dream: not dream.lucid)) for hour in
                                    range(24)}

            elif tag[1] == 'NOT IN':
                if barType == 'days':
                    values_per_x = {day: len(collection[day].filter(lambda dream: tag[0] not in dream.tags)) for day in
                                    range(7)}
                else:
                    values_per_x = {hour: len(collection[hour].filter(lambda dream: tag[0] not in dream.tags)) for hour
                                    in range(24)}

            elif tag[1] == 'IN':
                if barType == 'days':
                    values_per_x = {day: len(collection[day].filter(lambda dream: tag[0] in dream.tags)) for day in
                                    range(7)}
                else:
                    values_per_x = {hour: len(collection[hour].filter(lambda dream: tag[0] in dream.tags)) for hour in
                                    range(24)}

            values.append(values_per_x)

        x = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'] if barType == 'days' else [f"{h}H"
                                                                                                                 for h
                                                                                                                 in
                                                                                                                 range(
                                                                                                                     24)]

        width = -0.013 * len(values) + 0.23  # "responsive" width equation found with linear regression

        widget = MplWidget()
        widget.setFixedHeight(400)

        for y, color, label, index in zip(values, colors, labels, range(len(values))):
            widget.bar(x, y.values(), color=color, label=label, width=width, space=width * index, legend=True,
                       ylabel='Quantité')
        widget.setTitle(bar['title'])

        self.previewLayout.addWidget(widget)

    def addCategory(self, category):
        dreams_analyzer = DreamsAnalyzer(self.controller.model.data.dreams)
        tags = [tag[0] for tag in dreams_analyzer.get_tags_counter()]

        filtered_tags = []
        for tag in tags:
            if tag.category:
                if tag.category.label == category:
                    filtered_tags.append(tag.label)

        for tag in filtered_tags:
            self.tagsLayout.addWidget(CustomChartTagWidget(self, self.controller, [tag, 'IN', "#" + ''.join(
                [random.choice('ABCDEF0123456789') for i in range(6)]), {}]))

    def deleteAll_(self):
        clearLayout(self.tagsLayout)
        self.preview()
