#-*- encoding: utf-8 -*-
import xml.etree.ElementTree as etree
import os
import xlsxwriter
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.input_carpeta.clicked.connect(self.cualCarpeta)

        self.proyectos = ['','Papiit', 'Consolidacion', 'Fomix', 'Binacional', 'Otros']
        self.personas = ['Daniela', 'Edith', 'Rodrigo', 'Fidel', 'Ileana', 'Luis', 'Nadia', 'Paola', 'Victor', 'Yosune']
        self.ui.proyecto_box.addItems(self.proyectos)
        self.ui.proyecto_box.currentIndexChanged.connect(self.seleccionaProyecto)

    def seleccionaProyecto(self):
        self.ui.input_carpeta.setEnabled(True)
    def cualCarpeta(self):

        esteFileChooser = QFileDialog()
        esteFileChooser.setFileMode(QFileDialog.Directory)
        if esteFileChooser.exec_():

            self.esteFolder = esteFileChooser.selectedFiles()[0] + "/"
            self.ui.facturas_path.setText(self.esteFolder)
            self.procesaCarpeta(self.esteFolder)


    def procesaCarpeta(self,path):

        xlsx_path = os.path.join(path,"resumen.xlsx")
        workbook = xlsxwriter.Workbook(xlsx_path)
        worksheet = workbook.add_worksheet("viaticos")

        worksheet.write(0, 0,     "Usuario")
        worksheet.write(0, 1,     "Proyecto")
        worksheet.write(0, 2,     "Fecha")
        worksheet.write(0, 3,     "Folio facturas")
        worksheet.write(0, 4,     "Tipo")
        worksheet.write(0, 5,     "Monto")
        worksheet.write(0, 6,     "Estatus")
        worksheet.write(0, 7,     "Factura disponible")
        worksheet.write(0, 8,     "Comentario")
        worksheet.write(0, 9,     "Descripcion")

        row = 0
        suma = 0
        arch_total=0
        dicc_users = {}
        self.ui.textBrowser.append("Carpeta: "+ path)
        for carpeta in os.listdir(path):
            if os.path.isdir(os.path.join(path,carpeta)):

                carpeta_usuario = os.path.join(path,carpeta)
                usuario = carpeta.title()
                self.ui.textBrowser.append("Procesando: "+ usuario)
                suma_user=0
                dicc_users[usuario]=0
                for archivo in os.listdir(carpeta_usuario):
                    if archivo.endswith(".xml"):
                        arch_total+=1
                        nombre = archivo.split(".")[0]
                        if len(nombre) > 5:
                            nombre = nombre[-5:]
                        row += 1
                        xml_path = os.path.join(carpeta_usuario,archivo)
                        tree = etree.parse(xml_path)

                        root = tree.getroot()
                        total = float(root.get("Total"))
                        dicc_users[usuario] += total
                        ComplementoTag = root.find("{http://www.sat.gob.mx/cfd/3}Complemento")
                        TimbreFiscalDigitalTag = ComplementoTag.find("{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital")
                        fechaTimbrado = TimbreFiscalDigitalTag.get("FechaTimbrado").split("T")[0]

                        conceptosTag = root.find("{http://www.sat.gob.mx/cfd/3}Conceptos")

                        listaconceptosTag = conceptosTag.findall ("{http://www.sat.gob.mx/cfd/3}Concepto")
                        primerConceptoTag = listaconceptosTag[0]
                        descripcion = primerConceptoTag.get("Descripcion")
                        print (xml_path, total, fechaTimbrado, descripcion, nombre)
                        worksheet.data_validation('A'+str(row+1), {'validate': 'list', 'source': self.personas})
                        worksheet.write(row, 0,     usuario)
                        worksheet.data_validation('B'+str(row+1), {'validate': 'list', 'source': self.proyectos})
                        worksheet.write(row, 1,     self.ui.proyecto_box.currentText())
                        worksheet.write(row, 2,     fechaTimbrado)
                        worksheet.write(row, 3,     nombre)

                        worksheet.data_validation('E'+str(row+1), {'validate': 'list', 'source': ['Alimentos', 'Hospedaje', 'Transportacion', 'Otros']})
                        worksheet.write(row, 5,     total)
                        suma+=total
                        worksheet.data_validation('G'+str(row+1), {'validate': 'list', 'source': ['Pendiente', 'Reembolzado']})
                        worksheet.data_validation('H'+str(row+1), {'validate': 'list', 'source': ['Si', 'No']})
                        worksheet.write(row, 7,     'Si')

                        worksheet.write(row, 9,     descripcion)

                        # Write a total using a formula.
                        # worksheet.write(row, 0, 'Total')
                        # worksheet.write(row, 1, '=SUM(B1:B4)')


        sumRow = row+1
        worksheet.write(sumRow, 4,     "Suma")
        worksheet.write(sumRow, 5,     '=SUM(F2:F'+str(sumRow)+')')
        sumas_row = sumRow + 2
        suma_total = 0
        for key, value in dicc_users.items():
            self.ui.textBrowser.append(key+": "+ str(value))
            worksheet.write(sumas_row, 4,     key)
            worksheet.write(sumas_row, 5,     value)
            suma_total += value
            sumas_row += 1

        self.ui.textBrowser.append("Total: "+str(suma_total))
        workbook.close()
        self.ui.textBrowser.append("Resumen: "+xlsx_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
