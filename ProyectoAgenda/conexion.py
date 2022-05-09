from PyQt5 import QtWidgets, QtSql

import contactos
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
    Módulo para cargar contactos en la BD
    '''

    def cargarContacto(contacto):
        query = QtSql.QSqlQuery()
        query.prepare('insert into contactos (apellidos, nombre, telefono, email)'
                      'values (:apellidos, :nombre, :telefono, :email)')
        query.bindValue(':apellidos', str(contacto[0]))
        query.bindValue(':nombre', str(contacto[1]))
        query.bindValue(':telefono', str(contacto[2]))
        query.bindValue(':email', str(contacto[3]))
        if query.exec_():
            print("Inserción correcta")
            var.ui.labelEstado.setText('Alta contacto con nombre ' + apellidos + ',' + nombre)
            Conexion.mostrarContactos(self)
        else:
            print("Error: ", query.lastError().text())

    '''
    Módulo para mostrar clientes
    '''

    def mostrarContactos(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select apellidos, nombre, telefono, email from clientes')
        if query.exec_():
            while query.next():
                apellidos = query.value(0)
                nombre = query.value(1)
                telefono = query.value(2)
                email = query.value(3)
                var.ui.tablaValores.setRowCount(index + 1)
                var.ui.tablaValores.setItem(index, 0, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaValores.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tablaValores.setItem(index, 2, QtWidgets.QTableWidgetItem(telefono))
                var.ui.tablaValores.setItem(index, 2, QtWidgets.QTableWidgetItem(email))
                index += 1
        else:
            print("Error mostrar contactos: ", query.lastError().text())

