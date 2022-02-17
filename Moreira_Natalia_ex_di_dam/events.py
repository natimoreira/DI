import sys, var

class Eventos:
    '''Función para salir desde el menú'''
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