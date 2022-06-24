from models.ui.qt_utils import clearLayout
from models.ui.tabs.tab import Tab
from models.dreams_analyzer import DreamsAnalyzer
from mplwidget import MplWidget


class StatisticsTab(Tab):

    def setupUi(self):
        self.mainWindow.otherPlotsLayout.setFixedHeight(400)

    def connect(self):
        pass

    def updateData(self):
        clearLayout(self.mainWindow.pieChartsLayout)
        clearLayout(self.mainWindow.barChartsLayout)
        self.plotBarCharts(self.mainWindow.barChartsLayout)
        self.plotPieCharts(self.mainWindow.pieChartsLayout)

    def updateCharts(self):
        clearLayout(self.mainWindow.pieChartsLayout)
        clearLayout(self.mainWindow.barChartsLayout)
        self.plotBarCharts(self.mainWindow.barChartsLayout)
        self.plotPieCharts(self.mainWindow.pieChartsLayout)

    def plotBarCharts(self, layout):
        bars = [chart for chart in self.mainWindow.controller.get_charts() if chart['type'] == 'bar']
        for bar in bars:
            self.plotBarChart(bar, layout)

    def plotBarChart(self, bar, layout):

        barType = bar['x']

        if not self.mainWindow.controller.model.data:
            return

        dreams = self.mainWindow.controller.model.data.dreams

        tags = bar['tags']

        labels = [("Pas "+tag[0] if tag[1] == 'NOT IN' else tag[0]) for tag in tags]
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
                    values_per_x = {hour: len(collection[hour].filter(lambda dream: not dream.lucid)) for hour in range(24)}

            elif tag[1] == 'NOT IN':
                if barType == 'days':
                    values_per_x = {day: len(collection[day].filter(lambda dream: tag[0] not in dream.tags)) for day in range(7)}
                else:
                    values_per_x = {hour: len(collection[hour].filter(lambda dream: tag[0] not in dream.tags)) for hour in range(24)}

            elif tag[1] == 'IN':
                if barType == 'days':
                    values_per_x = {day: len(collection[day].filter(lambda dream: tag[0] in dream.tags)) for day in range(7)}
                else:
                    values_per_x = {hour: len(collection[hour].filter(lambda dream: tag[0] in dream.tags)) for hour in range(24)}

            values.append(values_per_x)

        x = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'] if barType == 'days' else [f"{h}H" for h in range(24)]
        width = 0.2 - (0.2 / len(values))

        widget = MplWidget()
        widget.setFixedHeight(400)

        for y, color, label, index in zip(values, colors, labels, range(len(values))):
            widget.bar(x, y.values(), color=color, label=label, width=width, space=width*index, legend=True, ylabel='Quantité')
        widget.setTitle(bar['title'])

        layout.addWidget(widget)

    def plotPieCharts(self, layout):
        pies = [chart for chart in self.mainWindow.controller.get_charts() if chart['type'] == 'pie']
        for pie in pies:
            self.plotPieChart(pie, layout)

    def plotPieChart(self, pie, layout):
        if not self.mainWindow.controller.model.data:
            return

        dreams = self.mainWindow.controller.model.data.dreams

        tags = pie['tags']

        labels = [("Pas "+tag[0] if tag[1] == 'NOT IN' else tag[0]) for tag in tags]
        colors = [tag[2] for tag in tags]

        collections = []
        for tag in tags:
            filter = tag[3]
            collection = dreams

            if filter:
                if filter['lucid'] is True:
                    collection = dreams.filter(lambda  dream: dream.lucid)
                if filter['lucid'] is False:
                    collection = dreams.filter(lambda dream: not dream.lucid)

            collections.append(collection)

        values = []
        for tag, collection in zip(tags, collections):
            value = 0
            if tag[1] == 'NOT IN':
                value = len(collection.filter(lambda dream: tag[0] not in dream.tags))
            if tag[1] == 'IN':
                value = len(collection.filter(lambda dream: tag[0] in dream.tags))
            values.append(value)

        widget = MplWidget()
        widget.setFixedSize(500, 400)

        widget.pie(values, colors=colors, legend_labels=labels, bbox_to_anchor=(0.8, 1))
        widget.setTitle(pie['title'])

        layout.addWidget(widget)
