from PyQt5 import QtWidgets, QtSql
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
        query = QtSql.QSqlQery()
        query.prepare('insert into clientes (dni, apellidos, nombre, fechalta, direccion, provincia, sexo, formapago)'
                      'values (:dni, :apellido, :nombre, :fechalta, :direccion, :provincia, :sexo, :formapago)')
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
