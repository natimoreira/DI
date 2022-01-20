from windowaviso import *
from ventana import *
from venCalendar import *
import sys, var, events, clientes
from datetime import *

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''Salir menú'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

        '''Salir botones'''
        var.ui.btnSalir.clicked.connect(events.Eventos.SalirModal)

        '''Botón aceptar'''
        var.ui.btnAceptar.clicked.connect(clientes.Clientes.showClients)

        '''Botones radio sexo'''
        var.radioSexo = (var.ui.radioFem, var.ui.radioMas)
        for i in var.radioSexo:
            i.toggled.connect(clientes.Clientes.selSexo)

        '''Checbox pago'''
        var.checkPago = (var.ui.checkEfectivo, var.ui.checkTarjeta, var.ui.checkTransf)
        for i in var.checkPago:
            i.stateChanged.connect(clientes.Clientes.selPago)

        '''Lista provincias'''


        '''
        Eventos de texto
        '''
        var.ui.lineDNI.editingFinished.connect(clientes.Clientes.validarDNI)

        '''
        Eventos de botón
        '''
        var.ui.botonesRadio.buttonClicked.connect(clientes.Clientes.selSexo)
        var.ui.botonesCheck.buttonClicked.connect(clientes.Clientes.selPago)

        '''
        Eventos de lista
        '''
        clientes.Clientes.cargarProv()
        var.ui.comboProv.activated[str].connect(clientes.Clientes.selProv)

        '''
        Evento calendario
        '''
        var.ui.btnCalendario.clicked.connect(clientes.Clientes.abrirCalendar)


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


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_venCalendar()
        var.dlgcalendar.setupUi(self)
        diaActual = datetime.now().day
        mesActual = datetime.now().month
        anoActual = datetime.now().year
        var.dlgcalendar.calendar.setSelectedDate((QtCore.QDate(anoActual, mesActual, diaActual)))
        var.dlgcalendar.calendar.clicked.connect(clientes.Clientes.cargarFecha)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    var.dlgcalendar = DialogCalendar()
    window.show()
    sys.exit(app.exec())
