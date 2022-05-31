# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DreamsAnalyzer(object):
    def setupUi(self, DreamsAnalyzer):
        DreamsAnalyzer.setObjectName("DreamsAnalyzer")
        DreamsAnalyzer.resize(820, 542)
        self.centralwidget = QtWidgets.QWidget(DreamsAnalyzer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.Accueil = QtWidgets.QWidget()
        self.Accueil.setObjectName("Accueil")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Accueil)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.Accueil)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.last_file_loaded_value = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_file_loaded_value.setFont(font)
        self.last_file_loaded_value.setObjectName("last_file_loaded_value")
        self.horizontalLayout_9.addWidget(self.last_file_loaded_value)
        self.lastLoadedDataDateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.lastLoadedDataDateTimeEdit.setReadOnly(True)
        self.lastLoadedDataDateTimeEdit.setObjectName("lastLoadedDataDateTimeEdit")
        self.horizontalLayout_9.addWidget(self.lastLoadedDataDateTimeEdit)
        self.syncButton = QtWidgets.QPushButton(self.groupBox)
        self.syncButton.setObjectName("syncButton")
        self.horizontalLayout_9.addWidget(self.syncButton)
        self.importJSONFileButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importJSONFileButton.setFont(font)
        self.importJSONFileButton.setObjectName("importJSONFileButton")
        self.horizontalLayout_9.addWidget(self.importJSONFileButton)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_8 = QtWidgets.QGroupBox(self.Accueil)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.startDate = QtWidgets.QDateEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startDate.setFont(font)
        self.startDate.setCalendarPopup(True)
        self.startDate.setObjectName("startDate")
        self.horizontalLayout_5.addWidget(self.startDate)
        self.label_17 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        self.endDate = QtWidgets.QDateEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.endDate.setFont(font)
        self.endDate.setCalendarPopup(True)
        self.endDate.setObjectName("endDate")
        self.horizontalLayout_5.addWidget(self.endDate)
        self.label_19 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.dreamTypeSelect = QtWidgets.QComboBox(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dreamTypeSelect.setFont(font)
        self.dreamTypeSelect.setObjectName("dreamTypeSelect")
        self.horizontalLayout_5.addWidget(self.dreamTypeSelect)
        self.updateButton = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout_5.addWidget(self.updateButton)
        self.resetButton = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_5.addWidget(self.resetButton)
        self.verticalLayout_7.addWidget(self.groupBox_8)
        self.groupBox_2 = QtWidgets.QGroupBox(self.Accueil)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.last_file_loaded_value_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_file_loaded_value_2.setFont(font)
        self.last_file_loaded_value_2.setObjectName("last_file_loaded_value_2")
        self.horizontalLayout.addWidget(self.last_file_loaded_value_2)
        self.totalDreamsCounter = QtWidgets.QSpinBox(self.groupBox_2)
        self.totalDreamsCounter.setReadOnly(True)
        self.totalDreamsCounter.setObjectName("totalDreamsCounter")
        self.horizontalLayout.addWidget(self.totalDreamsCounter)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.normalDreamsCounter = QtWidgets.QSpinBox(self.groupBox_2)
        self.normalDreamsCounter.setObjectName("normalDreamsCounter")
        self.horizontalLayout.addWidget(self.normalDreamsCounter)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lucidDreamsCounter = QtWidgets.QSpinBox(self.groupBox_2)
        self.lucidDreamsCounter.setObjectName("lucidDreamsCounter")
        self.horizontalLayout.addWidget(self.lucidDreamsCounter)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.hhCounter = QtWidgets.QSpinBox(self.groupBox_2)
        self.hhCounter.setObjectName("hhCounter")
        self.horizontalLayout.addWidget(self.hhCounter)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.Accueil)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.meanMetaLayout = QtWidgets.QHBoxLayout()
        self.meanMetaLayout.setObjectName("meanMetaLayout")
        self.verticalLayout.addLayout(self.meanMetaLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lucidDreamsRate = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lucidDreamsRate.setFont(font)
        self.lucidDreamsRate.setReadOnly(True)
        self.lucidDreamsRate.setObjectName("lucidDreamsRate")
        self.horizontalLayout_10.addWidget(self.lucidDreamsRate)
        self.last_file_loaded_value_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_file_loaded_value_4.setFont(font)
        self.last_file_loaded_value_4.setObjectName("last_file_loaded_value_4")
        self.horizontalLayout_10.addWidget(self.last_file_loaded_value_4)
        self.averageLength = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.averageLength.setFont(font)
        self.averageLength.setReadOnly(True)
        self.averageLength.setObjectName("averageLength")
        self.horizontalLayout_10.addWidget(self.averageLength)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.averageDreamsPerNight = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.averageDreamsPerNight.setFont(font)
        self.averageDreamsPerNight.setReadOnly(True)
        self.averageDreamsPerNight.setObjectName("averageDreamsPerNight")
        self.horizontalLayout_10.addWidget(self.averageDreamsPerNight)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.Accueil)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.last_file_loaded_value_5 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_file_loaded_value_5.setFont(font)
        self.last_file_loaded_value_5.setObjectName("last_file_loaded_value_5")
        self.horizontalLayout_3.addWidget(self.last_file_loaded_value_5)
        self.mostFrequentTag = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mostFrequentTag.setFont(font)
        self.mostFrequentTag.setReadOnly(True)
        self.mostFrequentTag.setObjectName("mostFrequentTag")
        self.horizontalLayout_3.addWidget(self.mostFrequentTag)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.mostFrequentCategory = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mostFrequentCategory.setFont(font)
        self.mostFrequentCategory.setReadOnly(True)
        self.mostFrequentCategory.setObjectName("mostFrequentCategory")
        self.horizontalLayout_3.addWidget(self.mostFrequentCategory)
        self.last_file_loaded_value_6 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_file_loaded_value_6.setFont(font)
        self.last_file_loaded_value_6.setObjectName("last_file_loaded_value_6")
        self.horizontalLayout_3.addWidget(self.last_file_loaded_value_6)
        self.mostFrequentHour = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mostFrequentHour.setFont(font)
        self.mostFrequentHour.setReadOnly(True)
        self.mostFrequentHour.setObjectName("mostFrequentHour")
        self.horizontalLayout_3.addWidget(self.mostFrequentHour)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.Accueil)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.totalWords = QtWidgets.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalWords.setFont(font)
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
        self.tags.setGeometry(QtCore.QRect(0, 0, 382, 423))
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
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 382, 423))
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Progression)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.Progression)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.resolutionSelect = QtWidgets.QComboBox(self.Progression)
        self.resolutionSelect.setObjectName("resolutionSelect")
        self.horizontalLayout_6.addWidget(self.resolutionSelect)
        self.updateButton2 = QtWidgets.QPushButton(self.Progression)
        self.updateButton2.setObjectName("updateButton2")
        self.horizontalLayout_6.addWidget(self.updateButton2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_6 = QtWidgets.QGroupBox(self.Progression)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lucidDreamsRatePlot = MplWidget(self.groupBox_6)
        self.lucidDreamsRatePlot.setObjectName("lucidDreamsRatePlot")
        self.gridLayout_2.addWidget(self.lucidDreamsRatePlot, 1, 2, 1, 1)
        self.totalDreamsPlot = MplWidget(self.groupBox_6)
        self.totalDreamsPlot.setObjectName("totalDreamsPlot")
        self.gridLayout_2.addWidget(self.totalDreamsPlot, 0, 1, 1, 1)
        self.lucidDreamsPlot = MplWidget(self.groupBox_6)
        self.lucidDreamsPlot.setObjectName("lucidDreamsPlot")
        self.gridLayout_2.addWidget(self.lucidDreamsPlot, 0, 2, 1, 1)
        self.averageDreamsPerNightPlot = MplWidget(self.groupBox_6)
        self.averageDreamsPerNightPlot.setObjectName("averageDreamsPerNightPlot")
        self.gridLayout_2.addWidget(self.averageDreamsPerNightPlot, 1, 1, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.Progression)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.averageMoodPlot = MplWidget(self.groupBox_7)
        self.averageMoodPlot.setObjectName("averageMoodPlot")
        self.gridLayout_3.addWidget(self.averageMoodPlot, 1, 0, 1, 1)
        self.averageLucidityPlot = MplWidget(self.groupBox_7)
        self.averageLucidityPlot.setObjectName("averageLucidityPlot")
        self.gridLayout_3.addWidget(self.averageLucidityPlot, 0, 1, 1, 1)
        self.averageDreamLengtPlot = MplWidget(self.groupBox_7)
        self.averageDreamLengtPlot.setObjectName("averageDreamLengtPlot")
        self.gridLayout_3.addWidget(self.averageDreamLengtPlot, 1, 1, 1, 1)
        self.averageClearPlot = MplWidget(self.groupBox_7)
        self.averageClearPlot.setObjectName("averageClearPlot")
        self.gridLayout_3.addWidget(self.averageClearPlot, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.Progression, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.dreamsByDayPlot = MplWidget(self.groupBox_9)
        self.dreamsByDayPlot.setObjectName("dreamsByDayPlot")
        self.horizontalLayout_12.addWidget(self.dreamsByDayPlot)
        self.verticalLayout_5.addWidget(self.groupBox_9)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.dreamsPerHourPlot = MplWidget(self.groupBox_11)
        self.dreamsPerHourPlot.setObjectName("dreamsPerHourPlot")
        self.verticalLayout_8.addWidget(self.dreamsPerHourPlot)
        self.verticalLayout_5.addWidget(self.groupBox_11)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.inductionsPlot = MplWidget(self.groupBox_10)
        self.inductionsPlot.setObjectName("inductionsPlot")
        self.horizontalLayout_13.addWidget(self.inductionsPlot)
        self.wbtbPlot = MplWidget(self.groupBox_10)
        self.wbtbPlot.setObjectName("wbtbPlot")
        self.horizontalLayout_13.addWidget(self.wbtbPlot)
        self.vividDreamsPlot = MplWidget(self.groupBox_10)
        self.vividDreamsPlot.setObjectName("vividDreamsPlot")
        self.horizontalLayout_13.addWidget(self.vividDreamsPlot)
        self.verticalLayout_5.addWidget(self.groupBox_10)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.dreamsScrollArea = QtWidgets.QScrollArea(self.tab)
        self.dreamsScrollArea.setWidgetResizable(True)
        self.dreamsScrollArea.setObjectName("dreamsScrollArea")
        self.dreamsForm = QtWidgets.QWidget()
        self.dreamsForm.setGeometry(QtCore.QRect(0, 0, 776, 451))
        self.dreamsForm.setObjectName("dreamsForm")
        self.dreamsLayoutVertical = QtWidgets.QVBoxLayout(self.dreamsForm)
        self.dreamsLayoutVertical.setObjectName("dreamsLayoutVertical")
        self.dreamsScrollArea.setWidget(self.dreamsForm)
        self.horizontalLayout_11.addWidget(self.dreamsScrollArea)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_20 = QtWidgets.QLabel(self.groupBox_12)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_14.addWidget(self.label_20)
        self.selectedTemplateEdit = QtWidgets.QLineEdit(self.groupBox_12)
        self.selectedTemplateEdit.setObjectName("selectedTemplateEdit")
        self.horizontalLayout_14.addWidget(self.selectedTemplateEdit)
        self.loadTemplateButton = QtWidgets.QPushButton(self.groupBox_12)
        self.loadTemplateButton.setObjectName("loadTemplateButton")
        self.horizontalLayout_14.addWidget(self.loadTemplateButton)
        self.newTemplateButton = QtWidgets.QPushButton(self.groupBox_12)
        self.newTemplateButton.setObjectName("newTemplateButton")
        self.horizontalLayout_14.addWidget(self.newTemplateButton)
        self.verticalLayout_9.addWidget(self.groupBox_12)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 378))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.nightsLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.nightsLayout.setObjectName("nightsLayout")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.addAnonymButton = QtWidgets.QPushButton(self.tab_4)
        self.addAnonymButton.setObjectName("addAnonymButton")
        self.horizontalLayout_15.addWidget(self.addAnonymButton)
        self.saveAnonymsButton = QtWidgets.QPushButton(self.tab_4)
        self.saveAnonymsButton.setObjectName("saveAnonymsButton")
        self.horizontalLayout_15.addWidget(self.saveAnonymsButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.anonymLayout = QtWidgets.QWidget()
        self.anonymLayout.setGeometry(QtCore.QRect(0, 0, 776, 415))
        self.anonymLayout.setObjectName("anonymLayout")
        self.anonymLayout_3 = QtWidgets.QVBoxLayout(self.anonymLayout)
        self.anonymLayout_3.setObjectName("anonymLayout_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_21 = QtWidgets.QLabel(self.anonymLayout)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_16.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.anonymLayout)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_16.addWidget(self.label_22)
        self.anonymLayout_3.addLayout(self.horizontalLayout_16)
        self.anonymLayout_2 = QtWidgets.QVBoxLayout()
        self.anonymLayout_2.setObjectName("anonymLayout_2")
        self.anonymLayout_3.addLayout(self.anonymLayout_2)
        self.scrollArea_4.setWidget(self.anonymLayout)
        self.verticalLayout_10.addWidget(self.scrollArea_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        DreamsAnalyzer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DreamsAnalyzer)
        self.statusbar.setObjectName("statusbar")
        DreamsAnalyzer.setStatusBar(self.statusbar)

        self.retranslateUi(DreamsAnalyzer)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DreamsAnalyzer)

    def retranslateUi(self, DreamsAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        DreamsAnalyzer.setWindowTitle(_translate("DreamsAnalyzer", "Dreams Analyzer"))
        self.groupBox.setTitle(_translate("DreamsAnalyzer", "Fichier"))
        self.last_file_loaded_value.setText(_translate("DreamsAnalyzer", "Dernières données chargées :"))
        self.syncButton.setText(_translate("DreamsAnalyzer", "Synchroniser les rêves"))
        self.importJSONFileButton.setText(_translate("DreamsAnalyzer", "Importer un fichier JSON"))
        self.groupBox_8.setTitle(_translate("DreamsAnalyzer", "Filtres"))
        self.label_16.setText(_translate("DreamsAnalyzer", "Début"))
        self.label_17.setText(_translate("DreamsAnalyzer", "Fin"))
        self.label_19.setText(_translate("DreamsAnalyzer", "Type de rêves :"))
        self.updateButton.setText(_translate("DreamsAnalyzer", "Valider"))
        self.resetButton.setText(_translate("DreamsAnalyzer", "Réinitialiser"))
        self.groupBox_2.setTitle(_translate("DreamsAnalyzer", "Rêves"))
        self.last_file_loaded_value_2.setText(_translate("DreamsAnalyzer", "Total : "))
        self.label_2.setText(_translate("DreamsAnalyzer", "Normaux :"))
        self.label_4.setText(_translate("DreamsAnalyzer", "Lucides :"))
        self.label_6.setText(_translate("DreamsAnalyzer", "HH :"))
        self.groupBox_3.setTitle(_translate("DreamsAnalyzer", "Moyennes"))
        self.label_8.setText(_translate("DreamsAnalyzer", "Taux de RL :"))
        self.last_file_loaded_value_4.setText(_translate("DreamsAnalyzer", "Longueur de rêve (en mots) :"))
        self.label_9.setText(_translate("DreamsAnalyzer", "Rêves par nuit :"))
        self.groupBox_4.setTitle(_translate("DreamsAnalyzer", "Fréquences"))
        self.last_file_loaded_value_5.setText(_translate("DreamsAnalyzer", "Tag le plus fréquent :"))
        self.label_10.setText(_translate("DreamsAnalyzer", "Catégorie la plus fréquente :"))
        self.last_file_loaded_value_6.setText(_translate("DreamsAnalyzer", "Heure la plus fréquente :"))
        self.groupBox_5.setTitle(_translate("DreamsAnalyzer", "Total"))
        self.label_11.setText(_translate("DreamsAnalyzer", "Total de mots écrits :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Accueil), _translate("DreamsAnalyzer", "Accueil"))
        self.label.setText(_translate("DreamsAnalyzer", "Tags"))
        self.label_13.setText(_translate("DreamsAnalyzer", "Label"))
        self.label_12.setText(_translate("DreamsAnalyzer", "Nombre d\'occurences"))
        self.label_3.setText(_translate("DreamsAnalyzer", "Catégories"))
        self.label_15.setText(_translate("DreamsAnalyzer", "Label"))
        self.label_14.setText(_translate("DreamsAnalyzer", "Nombre d\'occurences"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Occurences), _translate("DreamsAnalyzer", "Tags"))
        self.label_18.setText(_translate("DreamsAnalyzer", "Résolution"))
        self.updateButton2.setText(_translate("DreamsAnalyzer", "Valider"))
        self.groupBox_6.setTitle(_translate("DreamsAnalyzer", "Rêves"))
        self.groupBox_7.setTitle(_translate("DreamsAnalyzer", "Moyennes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Progression), _translate("DreamsAnalyzer", "Progression"))
        self.groupBox_9.setTitle(_translate("DreamsAnalyzer", "Type de rêves par jour"))
        self.groupBox_11.setTitle(_translate("DreamsAnalyzer", "Type de rêves par heure"))
        self.groupBox_10.setTitle(_translate("DreamsAnalyzer", "Divers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DreamsAnalyzer", "Statistiques"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DreamsAnalyzer", "Rêves"))
        self.groupBox_12.setTitle(_translate("DreamsAnalyzer", "Templates"))
        self.label_20.setText(_translate("DreamsAnalyzer", "Template séléctionné :"))
        self.loadTemplateButton.setText(_translate("DreamsAnalyzer", "Charger"))
        self.newTemplateButton.setText(_translate("DreamsAnalyzer", "Nouveau"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DreamsAnalyzer", "Attrape Songes"))
        self.addAnonymButton.setText(_translate("DreamsAnalyzer", "Ajouter"))
        self.saveAnonymsButton.setText(_translate("DreamsAnalyzer", "Sauvegarder"))
        self.label_21.setText(_translate("DreamsAnalyzer", "Réel"))
        self.label_22.setText(_translate("DreamsAnalyzer", "Anonymisé"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("DreamsAnalyzer", "Anonymisateur"))
from mplwidget import MplWidget
