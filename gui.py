# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui',
# licensing of 'gui.ui' applies.
#
# Created: Fri Feb  1 21:45:00 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_carpeta = QtWidgets.QPushButton(self.centralwidget)
        self.input_carpeta.setEnabled(False)
        self.input_carpeta.setGeometry(QtCore.QRect(40, 190, 181, 32))
        self.input_carpeta.setObjectName("input_carpeta")
        self.facturas_path = QtWidgets.QLabel(self.centralwidget)
        self.facturas_path.setGeometry(QtCore.QRect(30, 240, 571, 31))
        self.facturas_path.setText("")
        self.facturas_path.setObjectName("facturas_path")
        self.proyecto_box = QtWidgets.QComboBox(self.centralwidget)
        self.proyecto_box.setGeometry(QtCore.QRect(120, 90, 104, 31))
        self.proyecto_box.setObjectName("proyecto_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 91, 31))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(375, 21, 491, 211))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAgregar_o_quitar_personas = QtWidgets.QAction(MainWindow)
        self.actionAgregar_o_quitar_personas.setObjectName("actionAgregar_o_quitar_personas")
        self.actionAgregar_o_quitar_proyectos = QtWidgets.QAction(MainWindow)
        self.actionAgregar_o_quitar_proyectos.setObjectName("actionAgregar_o_quitar_proyectos")
        self.menuOpciones.addAction(self.actionAgregar_o_quitar_personas)
        self.menuOpciones.addAction(self.actionAgregar_o_quitar_proyectos)
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.input_carpeta.setText(QtWidgets.QApplication.translate("MainWindow", "Carpeta Facturas", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Proyecto", None, -1))
        self.menuOpciones.setTitle(QtWidgets.QApplication.translate("MainWindow", "Opciones", None, -1))
        self.actionAgregar_o_quitar_personas.setText(QtWidgets.QApplication.translate("MainWindow", "Agregar o quitar personas", None, -1))
        self.actionAgregar_o_quitar_proyectos.setText(QtWidgets.QApplication.translate("MainWindow", "Agregar o quitar proyectos", None, -1))

