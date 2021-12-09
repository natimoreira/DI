from ventana import *
import sys, var, events, clientes

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        '''
        Eventos cada de texto
        '''
        var.ui.lineDNI.editingFinished.connect(clientes.Clientes.validarDNI)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
