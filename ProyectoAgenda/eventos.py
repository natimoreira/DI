import sys, var
from PyQt5 import QtWidgets

class Eventos:

    '''Función para salir'''
    def Salir():
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    '''Función para salir con el icono'''
    def SalirModal(self):
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec():
                sys.exit()
            else:
                var.dlgsalir.hide()
        except Exception as error:
            print("Error %s: " % str(error))