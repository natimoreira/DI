import var

class Eventos():
    def Saludo():
        try:
            var.ui.etiquetaBtn.setText('Has pulsado el botón')
        except Exception as error:
            print('Error: %s ' % str(error))
