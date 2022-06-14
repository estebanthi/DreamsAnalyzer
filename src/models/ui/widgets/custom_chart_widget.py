from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit, QLabel


from models.ui.popups.custom_chart_popup import CustomChartPopup


class CustomChartWidget(QWidget):

    def __init__(self, controller, chart, parent=None):
        QWidget.__init__(self, parent)
        self.hbl = QHBoxLayout()
        self.setLayout(self.hbl)

        self.chart = chart
        self.controller = controller

        label = QLabel(chart['title'])
        self.hbl.addWidget(label)

        self.edit_button = QPushButton('Editer')
        self.delete_button = QPushButton('Supprimer')

        self.hbl.addWidget(self.edit_button)
        self.hbl.addWidget(self.delete_button)

        self.delete_button.clicked.connect(lambda x: controller.delete_chart(chart['id_']))
        self.edit_button.clicked.connect(self.openEditPopup)

    def openEditPopup(self):
        self.popup = CustomChartPopup(self.controller, self.chart)
        self.popup.show()
