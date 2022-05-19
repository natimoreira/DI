import conexion
import printer
from ventanaAgenda import *
import sys, var, eventos, contactos
from windowaviso import *


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        ''' Conexión Base de datos '''
        conexion.Conexion.db_connect(var.filebd)
        conexion.Conexion.mostrarContactos(self)
        conexion.Conexion.mostrarContactos2(self)

        ''' Barra de estado '''
        var.ui.statusbar.addPermanentWidget(var.ui.labelEstado, 1)
        var.ui.labelEstado.setText('Aplicación Agenda de contactos')

        '''Salir menú'''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)

        '''Salir toolbar'''
        #var.ui.actiontoolbarSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.actiontoolbarSalir.triggered.connect(eventos.Eventos.SalirModal)

        '''Exportar contactos toolbar'''
        var.ui.actiontoolbarGuardar.triggered.connect(eventos.Eventos.Backup)

        '''Exportar contactos menú'''
        var.ui.actionExportar_Contactos.triggered.connect(eventos.Eventos.Backup)

        '''Generar informe toolbar'''
        var.ui.actiontoolbarInforme.triggered.connect(printer.Printer.reportContact)

        '''Generar informe menú'''
        var.ui.actionGenerar_Informe.triggered.connect(printer.Printer.reportContact)

        '''Botones'''
        var.ui.btnAgregar.clicked.connect(contactos.Contactos.altaContacto)
        var.ui.btnBorrar.clicked.connect(contactos.Contactos.bajaContacto)
        var.ui.btnMod.clicked.connect(contactos.Contactos.editContacto)
        var.ui.btnLimpiar.clicked.connect(contactos.Contactos.limpiarContacto)
        var.ui.btnReiniciar.clicked.connect(conexion.Conexion.mostrarContactos2)
        var.ui.btnReiniciar_2.clicked.connect(conexion.Conexion.mostrarContactos)
        var.ui.btnBuscar.clicked.connect(conexion.Conexion.buscarContacto)


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


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    var.filedlgabrir = FileDialogAbrir()
    window.show()
    sys.exit(app.exec())
