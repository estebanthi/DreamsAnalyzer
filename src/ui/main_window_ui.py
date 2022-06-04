# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Esteban\Desktop\Code\DreamsAnalyzer\src\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DreamsAnalyzer(object):
    def setupUi(self, DreamsAnalyzer):
        DreamsAnalyzer.setObjectName("DreamsAnalyzer")
        DreamsAnalyzer.resize(935, 735)
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
        self.normalDreamsCounter.setReadOnly(True)
        self.normalDreamsCounter.setObjectName("normalDreamsCounter")
        self.horizontalLayout.addWidget(self.normalDreamsCounter)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lucidDreamsCounter = QtWidgets.QSpinBox(self.groupBox_2)
        self.lucidDreamsCounter.setReadOnly(True)
        self.lucidDreamsCounter.setObjectName("lucidDreamsCounter")
        self.horizontalLayout.addWidget(self.lucidDreamsCounter)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.hhCounter = QtWidgets.QSpinBox(self.groupBox_2)
        self.hhCounter.setReadOnly(True)
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
        self.lucidDreamsRate = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.lucidDreamsRate.setReadOnly(True)
        self.lucidDreamsRate.setMaximum(100.0)
        self.lucidDreamsRate.setObjectName("lucidDreamsRate")
        self.horizontalLayout_10.addWidget(self.lucidDreamsRate)
        self.last_file_loaded_value_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_file_loaded_value_4.setFont(font)
        self.last_file_loaded_value_4.setObjectName("last_file_loaded_value_4")
        self.horizontalLayout_10.addWidget(self.last_file_loaded_value_4)
        self.averageLength = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.averageLength.setReadOnly(True)
        self.averageLength.setMinimum(0.0)
        self.averageLength.setMaximum(100000000.0)
        self.averageLength.setObjectName("averageLength")
        self.horizontalLayout_10.addWidget(self.averageLength)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.averageDreamsPerNight = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.averageDreamsPerNight.setReadOnly(True)
        self.averageDreamsPerNight.setMaximum(100000000.0)
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
        self.mostFrequentHour = QtWidgets.QTimeEdit(self.groupBox_4)
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
        self.totalWords = QtWidgets.QSpinBox(self.groupBox_5)
        self.totalWords.setReadOnly(True)
        self.totalWords.setMaximum(1000000000)
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
        self.tags.setGeometry(QtCore.QRect(0, 0, 440, 618))
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
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 439, 618))
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_6 = QtWidgets.QGroupBox(self.Progression)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.groupBox_6)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 869, 261))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.dreamsPlotLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.dreamsPlotLayout.setObjectName("dreamsPlotLayout")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea_5)
        self.horizontalLayout_8.addWidget(self.groupBox_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.groupBox_7 = QtWidgets.QGroupBox(self.Progression)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.groupBox_7)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 871, 263))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.metaPlotLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.metaPlotLayout.setObjectName("metaPlotLayout")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_17.addWidget(self.scrollArea_6)
        self.verticalLayout_4.addWidget(self.groupBox_7)
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
        self.otherPlotsLayout = QtWidgets.QGroupBox(self.tab_2)
        self.otherPlotsLayout.setObjectName("otherPlotsLayout")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.otherPlotsLayout)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.otherPlotsLayout)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 871, 506))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.otherPlotsLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.otherPlotsLayout_2.setObjectName("otherPlotsLayout_2")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_13.addWidget(self.scrollArea_7)
        self.verticalLayout_5.addWidget(self.otherPlotsLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.dreamsScrollArea = QtWidgets.QScrollArea(self.tab)
        self.dreamsScrollArea.setWidgetResizable(True)
        self.dreamsScrollArea.setObjectName("dreamsScrollArea")
        self.dreamsForm = QtWidgets.QWidget()
        self.dreamsForm.setGeometry(QtCore.QRect(0, 0, 891, 645))
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
        self.templatesComboBox = QtWidgets.QComboBox(self.groupBox_12)
        self.templatesComboBox.setObjectName("templatesComboBox")
        self.horizontalLayout_14.addWidget(self.templatesComboBox)
        self.editTemplateButton = QtWidgets.QPushButton(self.groupBox_12)
        self.editTemplateButton.setObjectName("editTemplateButton")
        self.horizontalLayout_14.addWidget(self.editTemplateButton)
        self.newTemplateButton = QtWidgets.QPushButton(self.groupBox_12)
        self.newTemplateButton.setObjectName("newTemplateButton")
        self.horizontalLayout_14.addWidget(self.newTemplateButton)
        self.verticalLayout_9.addWidget(self.groupBox_12)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 891, 573))
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.anonymLayout = QtWidgets.QWidget()
        self.anonymLayout.setGeometry(QtCore.QRect(0, 0, 891, 610))
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
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.emailDMInput = QtWidgets.QLineEdit(self.tab_6)
        self.emailDMInput.setObjectName("emailDMInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.emailDMInput)
        self.passwordDMInput = QtWidgets.QLineEdit(self.tab_6)
        self.passwordDMInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordDMInput.setObjectName("passwordDMInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordDMInput)
        self.autosyncCheckBox = QtWidgets.QCheckBox(self.tab_6)
        self.autosyncCheckBox.setObjectName("autosyncCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.autosyncCheckBox)
        self.horizontalLayout_18.addLayout(self.formLayout)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.verticalLayout_11.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        DreamsAnalyzer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DreamsAnalyzer)
        self.statusbar.setObjectName("statusbar")
        DreamsAnalyzer.setStatusBar(self.statusbar)

        self.retranslateUi(DreamsAnalyzer)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
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
        self.last_file_loaded_value_4.setText(_translate("DreamsAnalyzer", "Longueur de rêve moyenne (en mots) :"))
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
        self.groupBox_6.setTitle(_translate("DreamsAnalyzer", "Rêves"))
        self.groupBox_7.setTitle(_translate("DreamsAnalyzer", "Meta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Progression), _translate("DreamsAnalyzer", "Progression"))
        self.groupBox_9.setTitle(_translate("DreamsAnalyzer", "Type de rêves par jour"))
        self.groupBox_11.setTitle(_translate("DreamsAnalyzer", "Type de rêves par heure"))
        self.otherPlotsLayout.setTitle(_translate("DreamsAnalyzer", "Divers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DreamsAnalyzer", "Statistiques"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DreamsAnalyzer", "Rêves"))
        self.groupBox_12.setTitle(_translate("DreamsAnalyzer", "Templates"))
        self.label_20.setText(_translate("DreamsAnalyzer", "Template séléctionné :"))
        self.editTemplateButton.setText(_translate("DreamsAnalyzer", "Editer"))
        self.newTemplateButton.setText(_translate("DreamsAnalyzer", "Nouveau"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DreamsAnalyzer", "Attrape Songes"))
        self.addAnonymButton.setText(_translate("DreamsAnalyzer", "Ajouter"))
        self.label_21.setText(_translate("DreamsAnalyzer", "Réel"))
        self.label_22.setText(_translate("DreamsAnalyzer", "Anonymisé"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("DreamsAnalyzer", "Anonymisateur"))
        self.label_5.setText(_translate("DreamsAnalyzer", "Email"))
        self.label_7.setText(_translate("DreamsAnalyzer", "Mot de passe"))
        self.autosyncCheckBox.setText(_translate("DreamsAnalyzer", "Synchronisation automatique"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("DreamsAnalyzer", "Dream Manager"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("DreamsAnalyzer", "Métadonnées"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("DreamsAnalyzer", "Graphiques personnalisés"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("DreamsAnalyzer", "Paramètres"))
from mplwidget import MplWidget
