# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui',
# licensing of 'gui.ui' applies.
#
# Created: Sat Feb  2 12:36:52 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(743, 289)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(21)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setMinimumSize(QtCore.QSize(121, 0))
        self.splitter.setMaximumSize(QtCore.QSize(150, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.proyecto_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proyecto_box.sizePolicy().hasHeightForWidth())
        self.proyecto_box.setSizePolicy(sizePolicy)
        self.proyecto_box.setMinimumSize(QtCore.QSize(70, 0))
        self.proyecto_box.setObjectName("proyecto_box")
        self.horizontalLayout.addWidget(self.proyecto_box)
        self.input_carpeta = QtWidgets.QPushButton(self.splitter)
        self.input_carpeta.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.input_carpeta.sizePolicy().hasHeightForWidth())
        self.input_carpeta.setSizePolicy(sizePolicy)
        self.input_carpeta.setMinimumSize(QtCore.QSize(0, 30))
        self.input_carpeta.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_carpeta.setObjectName("input_carpeta")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.splitter)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.editFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(14)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editFrame.sizePolicy().hasHeightForWidth())
        self.editFrame.setSizePolicy(sizePolicy)
        self.editFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editFrame.setObjectName("editFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.editFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalWidget_2 = QtWidgets.QWidget(self.editFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(120, 0))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtWidgets.QTableView(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancelarButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.cancelarButton.setObjectName("cancelarButton")
        self.horizontalLayout_2.addWidget(self.cancelarButton)
        self.guardarButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.guardarButton.setObjectName("guardarButton")
        self.horizontalLayout_2.addWidget(self.guardarButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addWidget(self.verticalWidget_2)
        self.horizontalLayout_3.addWidget(self.editFrame)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(62)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout_3.setStretch(0, 23)
        self.horizontalLayout_3.setStretch(1, 13)
        self.horizontalLayout_3.setStretch(2, 65)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.facturas_path = QtWidgets.QLabel(self.centralwidget)
        self.facturas_path.setText("")
        self.facturas_path.setObjectName("facturas_path")
        self.horizontalLayout_4.addWidget(self.facturas_path)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 21))
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
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Proyecto", None, -1))
        self.input_carpeta.setText(QtWidgets.QApplication.translate("MainWindow", "Carpeta Facturas", None, -1))
        self.cancelarButton.setText(QtWidgets.QApplication.translate("MainWindow", "Cancelar", None, -1))
        self.guardarButton.setText(QtWidgets.QApplication.translate("MainWindow", "Guardar", None, -1))
        self.menuOpciones.setTitle(QtWidgets.QApplication.translate("MainWindow", "Opciones", None, -1))
        self.actionAgregar_o_quitar_personas.setText(QtWidgets.QApplication.translate("MainWindow", "Agregar o quitar personas", None, -1))
        self.actionAgregar_o_quitar_proyectos.setText(QtWidgets.QApplication.translate("MainWindow", "Agregar o quitar proyectos", None, -1))

