from datetime import datetime

import canvas as canvas
import os

import self as self
from PyQt5 import QtSql
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import var

class Printer():
    def cabecera(self):
        try:
            #logo = '.\\img\logo.png'
            var.rep.setTitle('INFORME')
            var.rep.setAuthor('Administración')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 745, 525, 745)
            # textcif = 'A0000000H'
            # textnom = 'IMPORTACIÓN Y EXPORTACIÓN TEIS, S.L.'
            # textdir = 'Av de Galicia, 101 - Vigo'
            # texttlfo = '886 12 04 64'
            # var.rep.drawString(50, 805, textcif)
            # var.rep.drawString(50, 790, textnom)
            # var.rep.drawString(50, 775, textdir)
            # var.rep.drawString(50, 760, texttlfo)
            # var.rep.drawString(logo, 450, 752)
        except Exception as error:
            print('Error en la cabecera: %s' % str(error))

    def pie(textListado):
        try:
            var.rep.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460, 40, str(fecha))
            var.rep.drawString(275, 40, str('Página %s' % var.rep.getPageNumber()))
            var.rep.drawString(50, 40, str(textListado))
        except Exception as error:
            print('Error en el pie de informe: %s' % str(error))

    def reportContact():
        try:
            var.rep = canvas.Canvas('informes/listadoContactos.pdf', pagesize=A4)
            #Printer.cabecera(self)
            var.rep.setFont('Helvetica-Bold', size=9)
            textListado = 'LISTADO DE CONTACTOS'
            var.rep.drawString(255, 735, textListado)
            var.rep.line(45, 730, 525, 730)
            itemcontact = ['APELLIDOS','NOMBRE','TELÉFONO', 'EMAIL']
            var.rep.drawString(50, 710, itemcontact[0])
            var.rep.drawString(130, 710, itemcontact[1])
            var.rep.drawString(230, 710, itemcontact[2])
            var.rep.drawString(330, 710, itemcontact[3])
            var.rep.line(45, 703, 525, 703)
            query = QtSql.QSqlQuery()
            query.prepare('select apellidos, nombre, telefono, email from contactos order by apellidos, nombre')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                i = 50
                j = 690
                while query.next():
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i+80, j, str(query.value(1)))
                    var.rep.drawString(i+180, j, str(query.value(2)))
                    var.rep.drawString(i+280, j, str(query.value(3)))
                    j=j-30
            Printer.pie(textListado)
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error reportContact %s' % str(error))