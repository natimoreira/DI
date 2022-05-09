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

        '''Salir menú'''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)

        '''Salir toolbar'''
        var.ui.actiontoolbarSalir.triggered.connect(eventos.Eventos.Salir)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())