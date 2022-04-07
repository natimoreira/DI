import os
import shutil
import sys, var
import zipfile
from datetime import *
from PyQt5 import QtWidgets

class Eventos:
    '''Función para abrir explorador'''
    def AbrirDir(self):
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print('Error abrir explorador: %s ' % str(error))

    '''Función para salir'''
    def Salir():
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    '''Función para salir con los botones'''
    def SalirModal(self):
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec():
                sys.exit()
            else:
                var.dlgsalir.hide()
        except Exception as error:
            print("Error %s: " % str(error))

    '''Función para guardar una copia de la BD en formato zip'''
    def Backup():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y-%m-%d_%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.filedlgabrir.getSaveFileName(None,'Guardar copia',var.copia,'.zip',options=option)
            if var.filedlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filebd, os.path.basename(var.filebd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.labelEstado.setText('Base de datos creada')
                shutil.move(str(var.copia), str(directorio))
        except Exception as error:
            print('Error: %s' % str(error))
