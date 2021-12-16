from windowaviso import *
from ventana import *
import sys, var, events, clientes

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''Salir menú'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

        '''Salir botones'''
        var.ui.btnSalir.clicked.connect(events.Eventos.SalirModal)

        '''Botones radio sexo'''
        var.radioSexo = (var.ui.radioFem, var.ui.radioMas)
        for i in var.radioSexo:
            i.toggled.connect(events.Eventos.selSexo)

        '''Checbox pago'''
        var.checkPago = (var.ui.checkEfectivo, var.ui.checkTarjeta, var.ui.checkTransf)
        for i in var.checkPago:
            i.stateChanged.connect(events.Eventos.selPago)

        '''Lista provincias'''


        '''
        Eventos de texto
        '''
        var.ui.lineDNI.editingFinished.connect(clientes.Clientes.validarDNI)

        '''
        Eventos de botón
        '''
        var.ui.botonesRadio.buttonClicked.connect(events.Eventos.selSexo)
        var.ui.botonesCheck.buttonClicked.connect(events.Eventos.selPago)

        '''
        Eventos de lista
        '''
        clientes.Clientes.cargarProv()
        var.ui.comboProv.activated[str].connect(events.Eventos.selProv)


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase que instancia la ventana de aviso salir
        '''
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_Dialog()
        var.dlgsalir.setupUi(self)
        '''var.dlgsalir.btnBox.accepted.connect(self.accept)
        var.dlgsalir.btnBox.accepted.rejected(self.reject)'''


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    window.show()
    sys.exit(app.exec())
