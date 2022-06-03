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
        clearLayout(self.mainWindow.otherPlotsLayout_2)
        self.plotDreamsByDay()
        self.plotDreamsByHour()
        self.plotOthers(self.mainWindow.otherPlotsLayout_2)

    def plotDreamsByDay(self):
        dreams_by_day = self.mainWindow.controller.model.data.dreams.group_by_day()
        lucid_dreams_by_day = {day: len(list(filter(lambda dream: dream.lucid, dreams_by_day[day]))) for day in
                               dreams_by_day.keys()}
        normal_dreams_by_days = {day: len(list(filter(lambda dream: not dream.lucid, dreams_by_day[day]))) for day in
                                 dreams_by_day.keys()}
        hh_by_days = self.mainWindow.controller.model.data.hhs.group_by_day()
        hh = {day: len(hh_by_days[day]) for day in hh_by_days.keys()}
        vivid_per_day = self.mainWindow.controller.model.data.dreams.filter(lambda dream: 'VIVID' in dream.tags).group_by_day()

        days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        width = 0.2

        self.mainWindow.dreamsByDayPlot.clear()
        self.mainWindow.dreamsByDayPlot.bar(days, list(normal_dreams_by_days.values()), width=width, color='green',
                                            label='RN')
        self.mainWindow.dreamsByDayPlot.bar(days, list(lucid_dreams_by_day.values()), width=width, space=width,
                                            color='blue',
                                            label='RL')
        self.mainWindow.dreamsByDayPlot.bar(days, [len(dreams) for dreams in vivid_per_day.values()], width=width,
                                            space=width * 2, color='orange', label='VIVID')
        self.mainWindow.dreamsByDayPlot.bar(days, list(hh.values()), width=width, space=width * 3, color='purple',
                                            label='HH',
                                            legend=True, ylabel='Quantité')

    def plotDreamsByHour(self):
        normal_dreams_per_hour = self.mainWindow.controller.model.data.dreams.filter(lambda dream: not dream.lucid).group_by_hour()
        lucid_dreams_per_hour = self.mainWindow.controller.model.data.dreams.filter(lambda dream: dream.lucid).group_by_hour()
        hh_per_hour = self.mainWindow.controller.model.data.hhs.group_by_hour()
        vivid_per_hour = self.mainWindow.controller.model.data.dreams.filter(lambda dream: 'VIVID' in dream.tags).group_by_hour()

        width = 0.2
        hours = [f"{h}H" for h in range(24)]
        self.mainWindow.dreamsPerHourPlot.clear()
        self.mainWindow.dreamsPerHourPlot.bar(hours, [len(dreams) for dreams in normal_dreams_per_hour.values()], width=width,
                                   color='green', label='RN')
        self.mainWindow.dreamsPerHourPlot.bar(hours, [len(dreams) for dreams in lucid_dreams_per_hour.values()], width=width,
                                   space=width, color='blue', label='RL')
        self.mainWindow.dreamsPerHourPlot.bar(hours, [len(dreams) for dreams in vivid_per_hour.values()], width=width,
                                   space=width * 2, color='orange', label='VIVID')
        self.mainWindow.dreamsPerHourPlot.bar(hours, [len(dreams) for dreams in hh_per_hour.values()], width=width,
                                   space=width * 3, color='purple', label='HH',
                                   legend=True, ylabel='Quantité')

    def plotOthers(self, layout):
        others = self.mainWindow.controller.get_other_plots()
        for other in others:
            self.plotOther(other, layout)

    def plotOther(self, other, layout):

        dreams = self.mainWindow.controller.model.data.dreams

        filter = other['filter']
        if filter:
            if filter['lucid']:
                dreams = dreams.filter(lambda dream: dream.lucid)
            else:
                dreams = dreams.filter(lambda dream: not dream.lucid)


        values = [len(dreams.filter(lambda dream: tag not in dream.tags)) if "Pas " in tag
                  else len(dreams.filter(lambda dream: tag in dream.tags))
                  for tag in other['tags']]

        widget = MplWidget()
        widget.setFixedSize(250, 250)

        widget.pie(values, colors=other['colors'], legend_labels=other['tags'])
        widget.setTitle(other['title'])

        layout.addWidget(widget)
