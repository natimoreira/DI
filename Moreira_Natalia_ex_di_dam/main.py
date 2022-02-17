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



        '''Validar dni'''
        var.ui.lineDNI.editingFinished.connect(clientes.Clientes.validarDNI)

        '''Evento calendario'''
        var.ui.btnCalendario.clicked.connect(clientes.Clientes.abrirCalendar)

        '''
        Eventos de botón
        '''
        var.ui.botonesRadio.buttonClicked.connect(clientes.Clientes.selOperacion)

        '''Botones radio'''
        var.radioOperacion = (var.ui.radioRet, var.ui.radioIng)
        for i in var.radioOperacion:
            i.toggled.connect(clientes.Clientes.selOperacion)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase que instancia la ventana de aviso salir
        '''
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_Dialog()
        var.dlgsalir.setupUi(self)

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