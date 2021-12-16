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

    '''Función para seleccionar sexo'''
    def selSexo(self):
        try:
            if var.ui.radioFem.isChecked():
                print('marcado femenino')
            if var.ui.radioMas.isChecked():
                print('marcado masculino')
        except Exception as error:
            print('Error en módulo seleccionar sexo:', error)

    '''Función para seleccionar pago'''
    def selPago(self):
        try:
            if var.ui.checkEfectivo.isChecked():
                print('Paga en efectivo')
            if var.ui.checkTarjeta.isChecked():
                print('Paga con tarjeta')
            if var.ui.checkTransf.isChecked():
                print('Paga con transferencia')
        except Exception as error:
            print('Error: %s ' % str(error))

    '''Función para seleccionar provincia'''
    def selProv(prov):
        try:
            print('Has seleccionado la provincia de ', prov)
            return prov
        except Exception as error:
            print('Error: %s ' % str(error))
