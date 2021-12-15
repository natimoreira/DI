import sys, var

class Eventos:
    def Salir():
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    def SalirModal(self):
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec():
                sys.exit()
            else:
                var.dlgsalir.hide()
        except Exception as error:
            print("Error %s: " % str(error))