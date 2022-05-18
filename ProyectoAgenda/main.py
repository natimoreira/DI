import conexion
from ventanaAgenda import *
import sys, var, eventos, contactos

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        ''' Conexión Base de datos '''
        conexion.Conexion.db_connect(var.filebd)
        conexion.Conexion.mostrarContactos(self)
        conexion.Conexion.mostrarContactos2(self)

        '''Salir menú'''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)

        '''Salir toolbar'''
        var.ui.actiontoolbarSalir.triggered.connect(eventos.Eventos.Salir)

        '''Botones'''
        var.ui.btnAgregar.clicked.connect(contactos.Contactos.altaContacto)
        var.ui.btnBorrar.clicked.connect(contactos.Contactos.bajaContacto)
        var.ui.btnMod.clicked.connect(contactos.Contactos.editContacto)
        var.ui.btnLimpiar.clicked.connect(contactos.Contactos.limpiarContacto)
        var.ui.btnReiniciar.clicked.connect(conexion.Conexion.mostrarContactos)
        var.ui.btnBuscar.clicked.connect(conexion.Conexion.buscarContacto)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())