#from PyQt5.uic.properties import QtWidgets
from PyQt5 import QtWidgets, QtSql

import var
import conexion

class Clientes():
    '''Función para comprobar DNI'''
    def validarDNI():
        try:
            dni = var.ui.lineDNI.text()
            var.ui.lineDNI.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE' #letras dni
            dig_ext = 'XYZ' #digito
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper() #conver la letra mayúsculas
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.labelValido.setStyleSheet('QLabel {color: green}')
                    var.ui.labelValido.setText('V')
                else:
                    var.ui.labelValido.setStyleSheet('QLabel {color: red}')
                    var.ui.labelValido.setText('X')
            else:
                var.ui.labelValido.setStyleSheet('QLabel {color: red}')
                var.ui.labelValido.setText('X')
        except Exception as error:
            print('Error en módulo validar DNI', error)

    '''Función para cargar provincias'''
    def cargarProv():
        '''
        Esta solución es provisional, en su momento lo haremos de otra forma
        cargando los registros desde una base de datos
        '''
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.comboProv.addItems(i)
        except Exception as error:
            print('Error: %s ' % str(error))

    '''
    Abrir la ventana calendario
    '''
    def abrirCalendar():
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    '''
    Este módulo se ejecuta cuando clickamos en un día del calendario
    '''
    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.lineFecha.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error al cargar fecha: %s ' % str(error))

    '''Función para seleccionar sexo'''

    def selSexo(self):
        try:
            global sex
            if var.ui.radioFem.isChecked():
                # print('marcado femenino')
                sex = 'Mujer'
            if var.ui.radioMas.isChecked():
                # print('marcado masculino')
                sex = 'Hombre'
        except Exception as error:
            print('Error en módulo seleccionar sexo:', error)

    '''Función para seleccionar pago'''

    def selPago(self):
        try:
            var.pay = []
            '''if var.ui.checkEfectivo.isChecked():
                # print('Paga en efectivo')
                var.pay.append('Efectivo')
            if var.ui.checkTarjeta.isChecked():
                # print('Paga con tarjeta')
                var.pay.append('Tarjeta')
            if var.ui.checkTransf.isChecked():
                # print('Paga con transferencia')
                var.pay.append('Transferencia')'''
            for i, data in enumerate(var.ui.botonesCheck.buttons()):
                # agrupamos en QtDesigner los checkbox en un ButtonGroup
                if data.isChecked() and i == 0:
                    var.pay.append('Efectivo')
                if data.isChecked() and i == 1:
                    var.pay.append('Tarjeta')
                if data.isChecked() and i == 2:
                    var.pay.append('Transferencia')
            #var.pay = set(var.pay)
            print(var.pay)
            return var.pay
        except Exception as error:
            print('Error: %s ' % str(error))

    '''Función para seleccionar provincia'''

    def selProv(prov):
        try:
            global vpro
            vpro = prov
            # print('Has seleccionado la provincia de ', prov)
            # return prov
        except Exception as error:
            print('Error: %s ' % str(error))

    '''
    Módulo para mostrar los datos introducidos
    '''
    def showClients():
        try:
            #Preparamos el registro
            newcli = []
            var.pay = []
            clitab = []  #serán los datos que carguemos en la tabla
            client = [var.ui.lineDNI, var.ui.lineApellido, var.ui.lineNombre, var.ui.lineFecha, var.ui.lineDir]
            k = 0
            for i in client:
                newcli.append(i.text())
                #carguemos los valores para la tabla que solo tiene tres: DNI, Apellidos y Nombre
                if k < 3:
                    clitab.append(i.text())
                    k += 1
            newcli.append(vpro)
            var.pay2 = Clientes.selPago()
            #elimina duplicados
            '''var.pay = set(var.pay)
            for j in var.pay:
                newcli.append(j)'''
            newcli.append(sex)
            newcli.append(var.pay2)
            print(newcli)
            print(clitab)
            if client:
            #comprobamos que no esté vacío lo principal
            #aquí empieza como trabajar con la TableWidget
                row = 0  #posición de la fila, problema: coloca al último como primero en cada click
                column = 0  #posición de la columna
                var.ui.tablaValores.insertRow(row)  #insertamos una fila nueva con cada click de botón
                for registro in clitab:
                    #la celda tiene una posición fila, columna y cargamos en ella el dato
                    cell = QtWidgets.QTableWidgetItem(registro)  #carga en cell cada dato de la lista
                    var.ui.tablaValores.setItem(row, column, cell)  #lo escribe
                    column += 1

                conexion.Conexion.cargarCli(newcli)
            else:
                print('Faltan datos')
            Clientes.limpiarCli(client, var.rbtsex, var.chkpago)
        except Exception as error:
            print('Error: %s ' % str(error))

    '''Módulo para dar de baja un cliente'''
    def bajaCliente(self):
        try:
            dni = var.ui.lineDNI.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.mostrarClientes(self)
            Clientes.limpiarCli()
        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    '''Módulo para modificar datos de un cliente'''
    def modifCliente(self):
        try:
            newdata = []
            client = [var.ui.lineDNI, var.ui.lineApellido, var.ui.lineNombre, var.ui.lineFecha, var.ui.lineDir]
            for i in client:
                newdata.append(i.text()) # cargamos los valores que hay en los editline
            newdata.append(var.ui.comboProv.currentText())
            newdata.append(var.sex)
            var.pay = Clientes.selPago()
            print(var.pay)
            cod = var.ui.lblcodigo.text()
            conexion.Conexion.modifCli(cod, newdata)
            conexion.Conexion.mostrarClientes(self)
        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))
