# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Esteban\Desktop\Code\DreamsAnalyzer\ui\post_popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.verticalLayout.addWidget(self.dateLabel)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 460))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.postEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.postEdit.setObjectName("postEdit")
        self.verticalLayout_2.addWidget(self.postEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout.addWidget(self.generateButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.copyButton = QtWidgets.QPushButton(self.centralwidget)
        self.copyButton.setObjectName("copyButton")
        self.verticalLayout.addWidget(self.copyButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dateLabel.setText(_translate("MainWindow", "TextLabel"))
        self.generateButton.setText(_translate("MainWindow", "Générer"))
        self.resetButton.setText(_translate("MainWindow", "Réinitialiser"))
        self.copyButton.setText(_translate("MainWindow", "Copier"))