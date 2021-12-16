from windowaviso import *
from ventana import *
import sys, var, events, clientes

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.btnSalir.clicked.connect(events.Eventos.SalirModal)
        '''
        Eventos cada de texto
        '''
        var.ui.lineDNI.editingFinished.connect(clientes.Clientes.validarDNI)

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
