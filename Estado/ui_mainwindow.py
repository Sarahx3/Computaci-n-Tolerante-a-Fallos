# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.textNotas = QTextEdit(self.centralwidget)
        self.textNotas.setObjectName(u"textNotas")

        self.gridLayout.addWidget(self.textNotas, 2, 0, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignRight)

        self.LEtitulo = QLineEdit(self.centralwidget)
        self.LEtitulo.setObjectName(u"LEtitulo")

        self.gridLayout.addWidget(self.LEtitulo, 1, 1, 1, 1)

        self.guardarButton = QPushButton(self.centralwidget)
        self.guardarButton.setObjectName(u"guardarButton")

        self.gridLayout.addWidget(self.guardarButton, 3, 0, 1, 2, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mis notas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo:", None))
        self.guardarButton.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
    # retranslateUi

