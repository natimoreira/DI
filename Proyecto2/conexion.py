from PyQt5 import QtWidgets, QtSql

import clientes
import var

class Conexion():

    def db_connect(filename):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexión. \n' 'Haz click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión establecida')
        return True

    '''
    Módulo para cargar clientes en la BD
    '''
    def cargarCli(cliente):
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apellidos, nombre, fechalta, direccion, provincia, sexo, formapago)'
                      'values (:dni, :apellidos, :nombre, :fechalta, :direccion, :provincia, :sexo, :formapago)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':fechalta', str(cliente[3]))
        query.bindValue(':direccion', str(cliente[4]))
        query.bindValue(':provincia', str(cliente[5]))
        query.bindValue(':sexo', str(cliente[6]))
        # pagos = ''.join(cliente[7]) #si quisieramos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formapago', str(cliente[7]))
        # print(pagos)
        if query.exec_():
            print("Inserción correcta")
            var.ui.labelEstado.setText('Alta cliente con dni ' + dni)
            Conexion.mostrarClientes(self)
        else:
            print("Error: ", query.lastError().text())

    '''
    Módulo para mostrar clientes
    '''
    def mostrarClientes(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                var.ui.tablaValores.setRowCount(index+1)
                var.ui.tablaValores.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tablaValores.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaValores.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    '''Móudlo para eliminar cliente. Se llama desde fichero clientes.py'''
    def bajaCli(dni):
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            print('Baja cliente')
            var.ui.labelEstado.setText('Cliente con dni ' + dni + ' dado de baja')
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    '''Módulo para modificar cliente se llama desde fichero clientes.py'''
    def modifCli(newdata):
        query = QtSql.QSqlQuery()
        #codigo = int(codigo)
        dni = newdata[0]
        query.prepare('update clientes set apellidos=:apellidos, nombre=:nombre,'
                      'fechalta=:fechalta, direccion=:direccion, provincia=:provincia'
                      'sexo=:sexo, formapago=:formapago where dni=:dni')
        #query.bindValue(':codigo', int(codigo))
        query.bindValue(':dni', str(dni))
        query.bindValue(':apellidos', str(newdata[1]))
        query.bindValue(':nombre', str(newdata[2]))
        query.bindValue(':fechalta', str(newdata[3]))
        query.bindValue(':direccion', str(newdata[4]))
        query.bindValue(':provincia', str(newdata[5]))
        query.bindValue(':sexo', str(newdata[6]))
        query.bindValue(':formapago', str(newdata[7]))
        if query.exec_():
            print('Cliente modificado')
            var.ui.labelEstado.setText('Cliente con dni ' + str(newdata[0]) + ' modificado')
        else:
            print("Error modificar cliente: ", query.lastError().text())


    def existeCli(id):
        try:
            salida = False
            query = QtSql.QSqlQuery()
            query.prepare('select dni from clientes')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    if (dni == id):
                        salida = True
            return salida
        except Exception as error:
            print('Error no existe cliente: %s' % str(error))


    def buscarCli(self):
        global dni
        global apellidos
        global nombre
        global fechalta
        global direccion
        global provincia
        global sexo
        global formapago

        id = var.ui.lineDNI.text()

        if conexion.Conexion.existeCli(id):
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, fechalta, direccion, provincia, '
                          'sexo, formapago from clientes where dni=:dni')
            query.bindValue(':dni', id)

            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    fechalta = query.value(3)
                    direccion = query.value(4)
                    provincia = query.value(5)
                    sexo = query.value(6)
                    formapago = query.value(7)
                    var.ui.tablaValores.setRowCount(index + 1)
                    var.ui.tablaValores.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.tablaValores.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tablaValores.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    index += 1
            else:
                print('Error buscar cliente: ', query.lastError().text())

            var.ui.lineDNI.setText(dni)
            var.ui.lineApellidos.setText(apellidos)
            var.ui.lineNombre.setText(nombre)
            var.ui.lineFecha.setText(fechalta)
            var.ui.lineDireccion.setText(direccion)
            var.ui.labelValido.setText("")

            if (provincia == ""):
                var.ui.comboProv.setCurrentIndex(0)
            elif (provincia == "A Coruña"):
                var.ui.comboProv.setCurrentIndex(1)
            elif (provincia == "Lugo"):
                var.ui.comboProv.setCurrentIndex(2)
            elif (provincia == "Ourense"):
                var.ui.comboProv.setCurrentIndex(3)
            elif (provincia == "Pontevedra"):
                var.ui.comboProv.setCurrentIndex(4)

            if (sexo == "Mujer"):
                var.ui.radioFem.click()
            elif (sexo == "Hombre"):
                var.ui.radioMas.click()

            if (formapago == 'Efectivo'):
                var.ui.checkEfectivo.check()
            elif (formapago == 'Tarjeta'):
                var.ui.checkTarjeta.check()
            elif (formapago == 'Transferencia'):
                var.ui.checkTrans.check()

            var.ui.labelEstado.setText('El cliente con DNI %s fue encontrado' % id)
        else:
            clientes.Clientes.limpiarCli(self)
            var.ui.lineDNI.setText(id)
            var.ui.labelEstado.setText('Cliente con DNI %s no encontrado' % id)
            var.ui.lineDNI.setText(id)

