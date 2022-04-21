import conexion
import printer
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

        ''' Conexión Base de datos '''
        conexion.Conexion.db_connect(var.filebd)
        conexion.Conexion.mostrarClientes(self)

        '''Abrir menú'''
        var.ui.actionAbrir.triggered.connect(events.Eventos.AbrirDir)

        '''Abrir toolbar'''
        var.ui.actiontoolbarAbrir.triggered.connect(events.Eventos.AbrirDir)

        '''Salir menú'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

        '''Salir toolbar'''
        var.ui.actiontoolbarSalir.triggered.connect(events.Eventos.Salir)

        '''Guardar zip toolbar'''
        var.ui.actiontoolbarGuardar.triggered.connect(events.Eventos.Backup)

        '''Generar informe'''
        var.ui.actiontoolbarInforme.triggered.connect(printer.Printer.reportCli)

        '''Botón aceptar (se cambió por Grabar)'''
        var.ui.btnAceptar.clicked.connect(clientes.Clientes.showClients)

        '''Botones eliminar, modificar y limpiar'''
        var.ui.btnEliminar.clicked.connect(clientes.Clientes.bajaCliente)
        var.ui.btnModificar.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnLimpiar.clicked.connect(clientes.Clientes.limpiarCli)

        '''Botones de arriba Buscar y Refrescar'''
        var.ui.btnReiniciar.clicked.connect(conexion.Conexion.mostrarClientes)
        var.ui.btnBuscar.clicked.connect(conexion.Conexion.buscarCli)

        '''Botones radio sexo'''
        var.radioSexo = (var.ui.radioFem, var.ui.radioMas)
        for i in var.radioSexo:
            i.toggled.connect(clientes.Clientes.selSexo)

        '''Checbox pago'''
        var.checkPago = (var.ui.checkEfectivo, var.ui.checkTarjeta, var.ui.checkTransf)
        for i in var.checkPago:
            i.stateChanged.connect(clientes.Clientes.selPago)

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
        #clientes.Clientes.cargarProv()
        var.ui.comboProv.activated[str].connect(clientes.Clientes.selProv)

        '''
        Evento calendario
        '''
        var.ui.btnCalendario.clicked.connect(clientes.Clientes.abrirCalendar)

        ''' Barra de estado '''
        var.ui.statusbar.addPermanentWidget(var.ui.labelEstado, 1)
        var.ui.labelEstado.setText('Bienvenido')


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase que instancia la ventana de aviso salir
        '''
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_Dialog()
        var.dlgsalir.setupUi(self)
        '''Salir boton'''
        var.ui.btnSalir.clicked.connect(events.Eventos.SalirModal)

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
    var.filedlgabrir = FileDialogAbrir()
    var.dlgsalir = DialogSalir()
    var.dlgcalendar = DialogCalendar()
    window.show()
    sys.exit(app.exec())
