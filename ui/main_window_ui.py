# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 731, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.last_file_loaded_value = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.last_file_loaded_value.setObjectName("last_file_loaded_value")
        self.horizontalLayout.addWidget(self.last_file_loaded_value)
        self.last_file_loaded_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.last_file_loaded_label.setObjectName("last_file_loaded_label")
        self.horizontalLayout.addWidget(self.last_file_loaded_label)
        self.import_json_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.import_json_button.setObjectName("import_json_button")
        self.horizontalLayout.addWidget(self.import_json_button)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 731, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.last_file_loaded_value_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.last_file_loaded_value_2.setObjectName("last_file_loaded_value_2")
        self.horizontalLayout_2.addWidget(self.last_file_loaded_value_2)
        self.dreams_total_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dreams_total_value.setObjectName("dreams_total_value")
        self.horizontalLayout_2.addWidget(self.dreams_total_value)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dreams_normal_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dreams_normal_value.setObjectName("dreams_normal_value")
        self.horizontalLayout_2.addWidget(self.dreams_normal_value)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.dreams_lucid_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dreams_lucid_value.setObjectName("dreams_lucid_value")
        self.horizontalLayout_2.addWidget(self.dreams_lucid_value)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.dreams_hh_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dreams_hh_value.setObjectName("dreams_hh_value")
        self.horizontalLayout_2.addWidget(self.dreams_hh_value)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 150, 731, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.last_file_loaded_value_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.last_file_loaded_value_3.setObjectName("last_file_loaded_value_3")
        self.horizontalLayout_3.addWidget(self.last_file_loaded_value_3)
        self.mood_mean = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.mood_mean.setObjectName("mood_mean")
        self.horizontalLayout_3.addWidget(self.mood_mean)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lucidity_mean = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lucidity_mean.setObjectName("lucidity_mean")
        self.horizontalLayout_3.addWidget(self.lucidity_mean)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.clear_mean = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.clear_mean.setObjectName("clear_mean")
        self.horizontalLayout_3.addWidget(self.clear_mean)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.rl_percent_value = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.rl_percent_value.setObjectName("rl_percent_value")
        self.horizontalLayout_3.addWidget(self.rl_percent_value)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.last_file_loaded_value_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.last_file_loaded_value_4.setObjectName("last_file_loaded_value_4")
        self.horizontalLayout_4.addWidget(self.last_file_loaded_value_4)
        self.length_mean = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.length_mean.setObjectName("length_mean")
        self.horizontalLayout_4.addWidget(self.length_mean)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.dreams_per_night_mean = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.dreams_per_night_mean.setObjectName("dreams_per_night_mean")
        self.horizontalLayout_4.addWidget(self.dreams_per_night_mean)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.last_file_loaded_value_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.last_file_loaded_value_5.setObjectName("last_file_loaded_value_5")
        self.horizontalLayout_5.addWidget(self.last_file_loaded_value_5)
        self.most_frequent_tag = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.most_frequent_tag.setObjectName("most_frequent_tag")
        self.horizontalLayout_5.addWidget(self.most_frequent_tag)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.most_frequent_category = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.most_frequent_category.setObjectName("most_frequent_category")
        self.horizontalLayout_5.addWidget(self.most_frequent_category)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menubar.setObjectName("menubar")
        self.menuVue_d_ensemble = QtWidgets.QMenu(self.menubar)
        self.menuVue_d_ensemble.setObjectName("menuVue_d_ensemble")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuVue_d_ensemble.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.last_file_loaded_value.setText(_translate("MainWindow", "Date du dernier fichier chargé : "))
        self.last_file_loaded_label.setText(_translate("MainWindow", "Aucun fichier chargé"))
        self.import_json_button.setText(_translate("MainWindow", "Importer un fichier JSON"))
        self.label.setText(_translate("MainWindow", "Rêves"))
        self.last_file_loaded_value_2.setText(_translate("MainWindow", "Total : "))
        self.dreams_total_value.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Normaux :"))
        self.dreams_normal_value.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Lucides :"))
        self.dreams_lucid_value.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "HH :"))
        self.dreams_hh_value.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Moyennes"))
        self.last_file_loaded_value_3.setText(_translate("MainWindow", "Mood :"))
        self.mood_mean.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Lucidité :"))
        self.lucidity_mean.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Clareté :"))
        self.clear_mean.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Taux de RL :"))
        self.rl_percent_value.setText(_translate("MainWindow", "0"))
        self.last_file_loaded_value_4.setText(_translate("MainWindow", "Longueur de rêve (en mots) :"))
        self.length_mean.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Rêves par nuit :"))
        self.dreams_per_night_mean.setText(_translate("MainWindow", "0"))
        self.last_file_loaded_value_5.setText(_translate("MainWindow", "Tag le plus fréquent :"))
        self.most_frequent_tag.setText(_translate("MainWindow", "Indéfini"))
        self.label_10.setText(_translate("MainWindow", "Catégorie la plus fréquente :"))
        self.most_frequent_category.setText(_translate("MainWindow", "Indéfini"))
        self.menuVue_d_ensemble.setTitle(_translate("MainWindow", "Vue d\'ensemble"))
