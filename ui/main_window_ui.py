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
        MainWindow.resize(981, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Accueil = QtWidgets.QWidget()
        self.Accueil.setObjectName("Accueil")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Accueil)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.Accueil)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.last_file_loaded_value = QtWidgets.QLabel(self.groupBox)
        self.last_file_loaded_value.setObjectName("last_file_loaded_value")
        self.horizontalLayout_9.addWidget(self.last_file_loaded_value)
        self.lastLoadedFileDate = QtWidgets.QLineEdit(self.groupBox)
        self.lastLoadedFileDate.setReadOnly(True)
        self.lastLoadedFileDate.setObjectName("lastLoadedFileDate")
        self.horizontalLayout_9.addWidget(self.lastLoadedFileDate)
        self.importJSONFileButton = QtWidgets.QPushButton(self.groupBox)
        self.importJSONFileButton.setObjectName("importJSONFileButton")
        self.horizontalLayout_9.addWidget(self.importJSONFileButton)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_8 = QtWidgets.QGroupBox(self.Accueil)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_8)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.startDate = QtWidgets.QDateEdit(self.groupBox_8)
        self.startDate.setCalendarPopup(True)
        self.startDate.setObjectName("startDate")
        self.horizontalLayout_5.addWidget(self.startDate)
        self.label_17 = QtWidgets.QLabel(self.groupBox_8)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        self.endDate = QtWidgets.QDateEdit(self.groupBox_8)
        self.endDate.setCalendarPopup(True)
        self.endDate.setObjectName("endDate")
        self.horizontalLayout_5.addWidget(self.endDate)
        self.updateButton = QtWidgets.QPushButton(self.groupBox_8)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout_5.addWidget(self.updateButton)
        self.resetButton = QtWidgets.QPushButton(self.groupBox_8)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_5.addWidget(self.resetButton)
        self.verticalLayout_7.addWidget(self.groupBox_8)
        self.groupBox_2 = QtWidgets.QGroupBox(self.Accueil)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.last_file_loaded_value_2 = QtWidgets.QLabel(self.groupBox_2)
        self.last_file_loaded_value_2.setObjectName("last_file_loaded_value_2")
        self.horizontalLayout.addWidget(self.last_file_loaded_value_2)
        self.totalDreamsCounter = QtWidgets.QLineEdit(self.groupBox_2)
        self.totalDreamsCounter.setReadOnly(True)
        self.totalDreamsCounter.setObjectName("totalDreamsCounter")
        self.horizontalLayout.addWidget(self.totalDreamsCounter)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.normalDreamsCounter = QtWidgets.QLineEdit(self.groupBox_2)
        self.normalDreamsCounter.setReadOnly(True)
        self.normalDreamsCounter.setObjectName("normalDreamsCounter")
        self.horizontalLayout.addWidget(self.normalDreamsCounter)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lucidDreamsCounter = QtWidgets.QLineEdit(self.groupBox_2)
        self.lucidDreamsCounter.setReadOnly(True)
        self.lucidDreamsCounter.setObjectName("lucidDreamsCounter")
        self.horizontalLayout.addWidget(self.lucidDreamsCounter)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.hhCounter = QtWidgets.QLineEdit(self.groupBox_2)
        self.hhCounter.setReadOnly(True)
        self.hhCounter.setObjectName("hhCounter")
        self.horizontalLayout.addWidget(self.hhCounter)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.Accueil)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.averageClear = QtWidgets.QLineEdit(self.groupBox_3)
        self.averageClear.setReadOnly(True)
        self.averageClear.setObjectName("averageClear")
        self.horizontalLayout_2.addWidget(self.averageClear)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.averageLucidity = QtWidgets.QLineEdit(self.groupBox_3)
        self.averageLucidity.setReadOnly(True)
        self.averageLucidity.setObjectName("averageLucidity")
        self.horizontalLayout_2.addWidget(self.averageLucidity)
        self.last_file_loaded_value_3 = QtWidgets.QLabel(self.groupBox_3)
        self.last_file_loaded_value_3.setObjectName("last_file_loaded_value_3")
        self.horizontalLayout_2.addWidget(self.last_file_loaded_value_3)
        self.averageMood = QtWidgets.QLineEdit(self.groupBox_3)
        self.averageMood.setReadOnly(True)
        self.averageMood.setObjectName("averageMood")
        self.horizontalLayout_2.addWidget(self.averageMood)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lucidDreamsRate = QtWidgets.QLineEdit(self.groupBox_3)
        self.lucidDreamsRate.setReadOnly(True)
        self.lucidDreamsRate.setObjectName("lucidDreamsRate")
        self.horizontalLayout_10.addWidget(self.lucidDreamsRate)
        self.last_file_loaded_value_4 = QtWidgets.QLabel(self.groupBox_3)
        self.last_file_loaded_value_4.setObjectName("last_file_loaded_value_4")
        self.horizontalLayout_10.addWidget(self.last_file_loaded_value_4)
        self.averageLength = QtWidgets.QLineEdit(self.groupBox_3)
        self.averageLength.setReadOnly(True)
        self.averageLength.setObjectName("averageLength")
        self.horizontalLayout_10.addWidget(self.averageLength)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.averageDreamsPerNight = QtWidgets.QLineEdit(self.groupBox_3)
        self.averageDreamsPerNight.setReadOnly(True)
        self.averageDreamsPerNight.setObjectName("averageDreamsPerNight")
        self.horizontalLayout_10.addWidget(self.averageDreamsPerNight)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.Accueil)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.last_file_loaded_value_5 = QtWidgets.QLabel(self.groupBox_4)
        self.last_file_loaded_value_5.setObjectName("last_file_loaded_value_5")
        self.horizontalLayout_3.addWidget(self.last_file_loaded_value_5)
        self.mostFrequentTag = QtWidgets.QLineEdit(self.groupBox_4)
        self.mostFrequentTag.setReadOnly(True)
        self.mostFrequentTag.setObjectName("mostFrequentTag")
        self.horizontalLayout_3.addWidget(self.mostFrequentTag)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.mostFrequentCategory = QtWidgets.QLineEdit(self.groupBox_4)
        self.mostFrequentCategory.setReadOnly(True)
        self.mostFrequentCategory.setObjectName("mostFrequentCategory")
        self.horizontalLayout_3.addWidget(self.mostFrequentCategory)
        self.last_file_loaded_value_6 = QtWidgets.QLabel(self.groupBox_4)
        self.last_file_loaded_value_6.setObjectName("last_file_loaded_value_6")
        self.horizontalLayout_3.addWidget(self.last_file_loaded_value_6)
        self.mostFrequentHour = QtWidgets.QLineEdit(self.groupBox_4)
        self.mostFrequentHour.setReadOnly(True)
        self.mostFrequentHour.setObjectName("mostFrequentHour")
        self.horizontalLayout_3.addWidget(self.mostFrequentHour)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.Accueil)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.totalWords = QtWidgets.QLineEdit(self.groupBox_5)
        self.totalWords.setReadOnly(True)
        self.totalWords.setObjectName("totalWords")
        self.horizontalLayout_4.addWidget(self.totalWords)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.tabWidget.addTab(self.Accueil, "")
        self.Occurences = QtWidgets.QWidget()
        self.Occurences.setObjectName("Occurences")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Occurences)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.Occurences)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.Occurences)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.tags = QtWidgets.QWidget()
        self.tags.setGeometry(QtCore.QRect(0, 0, 463, 584))
        self.tags.setObjectName("tags")
        self.tagsCounters = QtWidgets.QFormLayout(self.tags)
        self.tagsCounters.setObjectName("tagsCounters")
        self.label_13 = QtWidgets.QLabel(self.tags)
        self.label_13.setObjectName("label_13")
        self.tagsCounters.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_12 = QtWidgets.QLabel(self.tags)
        self.label_12.setObjectName("label_12")
        self.tagsCounters.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_12)
        self.line = QtWidgets.QFrame(self.tags)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tagsCounters.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line)
        self.line_2 = QtWidgets.QFrame(self.tags)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tagsCounters.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_2)
        self.scrollArea.setWidget(self.tags)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.Occurences)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Occurences)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 462, 584))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.categoriesCounters = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_3)
        self.categoriesCounters.setObjectName("categoriesCounters")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_15.setObjectName("label_15")
        self.categoriesCounters.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_14.setObjectName("label_14")
        self.categoriesCounters.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.categoriesCounters.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_4)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.categoriesCounters.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.Occurences, "")
        self.Progression = QtWidgets.QWidget()
        self.Progression.setObjectName("Progression")
        self.gridLayout = QtWidgets.QGridLayout(self.Progression)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_6 = QtWidgets.QGroupBox(self.Progression)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.totalDreamsPlot = MplWidget(self.groupBox_6)
        self.totalDreamsPlot.setObjectName("totalDreamsPlot")
        self.gridLayout_2.addWidget(self.totalDreamsPlot, 0, 0, 1, 1)
        self.lucidDreamsPlot = MplWidget(self.groupBox_6)
        self.lucidDreamsPlot.setObjectName("lucidDreamsPlot")
        self.gridLayout_2.addWidget(self.lucidDreamsPlot, 0, 1, 1, 1)
        self.averageDreamsPerNightPlot = MplWidget(self.groupBox_6)
        self.averageDreamsPerNightPlot.setObjectName("averageDreamsPerNightPlot")
        self.gridLayout_2.addWidget(self.averageDreamsPerNightPlot, 1, 0, 1, 1)
        self.lucidDreamsRatePlot = MplWidget(self.groupBox_6)
        self.lucidDreamsRatePlot.setObjectName("lucidDreamsRatePlot")
        self.gridLayout_2.addWidget(self.lucidDreamsRatePlot, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.Progression)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.averageClearPlot = MplWidget(self.groupBox_7)
        self.averageClearPlot.setObjectName("averageClearPlot")
        self.gridLayout_3.addWidget(self.averageClearPlot, 0, 0, 1, 1)
        self.averageLucidityPlot = MplWidget(self.groupBox_7)
        self.averageLucidityPlot.setObjectName("averageLucidityPlot")
        self.gridLayout_3.addWidget(self.averageLucidityPlot, 0, 1, 1, 1)
        self.averageMoodPlot = MplWidget(self.groupBox_7)
        self.averageMoodPlot.setObjectName("averageMoodPlot")
        self.gridLayout_3.addWidget(self.averageMoodPlot, 1, 0, 1, 1)
        self.averageDreamLengtPlot = MplWidget(self.groupBox_7)
        self.averageDreamLengtPlot.setObjectName("averageDreamLengtPlot")
        self.gridLayout_3.addWidget(self.averageDreamLengtPlot, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_7, 0, 1, 1, 1)
        self.tabWidget.addTab(self.Progression, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Fichier"))
        self.last_file_loaded_value.setText(_translate("MainWindow", "Date du dernier fichier chargé : "))
        self.importJSONFileButton.setText(_translate("MainWindow", "Importer un fichier JSON"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Temps"))
        self.label_16.setText(_translate("MainWindow", "Début"))
        self.label_17.setText(_translate("MainWindow", "Fin"))
        self.updateButton.setText(_translate("MainWindow", "Mettre à jour"))
        self.resetButton.setText(_translate("MainWindow", "Réinitialiser"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Rêves"))
        self.last_file_loaded_value_2.setText(_translate("MainWindow", "Total : "))
        self.label_2.setText(_translate("MainWindow", "Normaux :"))
        self.label_4.setText(_translate("MainWindow", "Lucides :"))
        self.label_6.setText(_translate("MainWindow", "HH :"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Moyennes"))
        self.label_7.setText(_translate("MainWindow", "Clareté :"))
        self.label_5.setText(_translate("MainWindow", "Lucidité :"))
        self.last_file_loaded_value_3.setText(_translate("MainWindow", "Mood :"))
        self.label_8.setText(_translate("MainWindow", "Taux de RL :"))
        self.last_file_loaded_value_4.setText(_translate("MainWindow", "Longueur de rêve (en mots) :"))
        self.label_9.setText(_translate("MainWindow", "Rêves par nuit :"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Fréquences"))
        self.last_file_loaded_value_5.setText(_translate("MainWindow", "Tag le plus fréquent :"))
        self.label_10.setText(_translate("MainWindow", "Catégorie la plus fréquente :"))
        self.last_file_loaded_value_6.setText(_translate("MainWindow", "Heure la plus fréquente :"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Total"))
        self.label_11.setText(_translate("MainWindow", "Total de mots écrits :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Accueil), _translate("MainWindow", "Accueil"))
        self.label.setText(_translate("MainWindow", "Tags"))
        self.label_13.setText(_translate("MainWindow", "Label"))
        self.label_12.setText(_translate("MainWindow", "Nombre d\'occurences"))
        self.label_3.setText(_translate("MainWindow", "Catégories"))
        self.label_15.setText(_translate("MainWindow", "Label"))
        self.label_14.setText(_translate("MainWindow", "Nombre d\'occurences"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Occurences), _translate("MainWindow", "Tags"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Rêves"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Meta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Progression), _translate("MainWindow", "Progression"))
from mplwidget import MplWidget
