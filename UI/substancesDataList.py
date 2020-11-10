# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'substancesDataList.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        MainWindow.setStyleSheet("background-color: rgb(248, 248, 248)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginTitle = QtWidgets.QLabel(self.centralwidget)
        self.loginTitle.setGeometry(QtCore.QRect(30, 20, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.loginTitle.setFont(font)
        self.loginTitle.setStyleSheet("font: 57 16pt \"Montserrat Medium\";\n"
"color: rgb(50, 79, 123);")
        self.loginTitle.setObjectName("loginTitle")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(430, 420, 321, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";\n"
"background-color: rgb(134, 166, 223);\n"
"color: rgb(248, 248, 248);")
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.comLabel = QtWidgets.QLabel(self.centralwidget)
        self.comLabel.setGeometry(QtCore.QRect(30, 270, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.comLabel.setFont(font)
        self.comLabel.setObjectName("comLabel")
        self.subsLine = QtWidgets.QLineEdit(self.centralwidget)
        self.subsLine.setGeometry(QtCore.QRect(30, 300, 721, 101))
        self.subsLine.setObjectName("subsLine")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 721, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Naval: SS Grupo 10"))
        self.loginTitle.setText(_translate("MainWindow", "Substâncias:"))
        self.backButton.setText(_translate("MainWindow", "Voltar"))
        self.comLabel.setText(_translate("MainWindow", "Comentários / Ocorrências: "))
