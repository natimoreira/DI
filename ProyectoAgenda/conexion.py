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
            Conexion.mostrarContactos2(self)
        else:
            print("Error: ", query.lastError().text())

    '''
    Módulo para mostrar contactos    
    '''
    def mostrarContactos(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select apellidos, nombre, telefono, email from contactos')
        if query.exec_():
            while query.next():
                apellidos = query.value(0)
                nombre = query.value(1)
                telefono = query.value(2)
                email = query.value(3)
                var.ui.tablaValores_2.setRowCount(index + 1)
                var.ui.tablaValores_2.setItem(index, 0, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaValores_2.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tablaValores_2.setItem(index, 2, QtWidgets.QTableWidgetItem(telefono))
                var.ui.tablaValores_2.setItem(index, 3, QtWidgets.QTableWidgetItem(email))
                index += 1
        else:
            print("Error mostrar contactos: ", query.lastError().text())

    '''Módulo para mostrar contactos en la segunda pestaña'''
    def mostrarContactos2(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select apellidos, nombre, telefono, email from contactos')
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
                var.ui.tablaValores.setItem(index, 3, QtWidgets.QTableWidgetItem(email))
                index += 1
        else:
            print("Error mostrar contactos: ", query.lastError().text())


    '''Módulo para eliminar contacto. Se llama desde fichero contactos.py'''
    def borrarContacto(nombre):
        query = QtSql.QSqlQuery()
        query.prepare('delete from contactos where nombre = :nombre')
        query.bindValue(':nombre', nombre)
        if query.exec_():
            print('Baja contacto')
            var.ui.labelEstado.setText('Contacto ' + nombre + ' dado de baja')
        else:
            print("Error borrar contacto: ", query.lastError().text())


    '''Módulo para modificar contacto se llama desde fichero contactos.py'''
    def modifContacto(newdata):
        query = QtSql.QSqlQuery()
        nombre = newdata[0]
        query.prepare('update contactos set apellidos=:apellidos,'
                      'telefono=:telefono, email=:email where nombre=:nombre')
        query.bindValue(':nombre', str(nombre))
        query.bindValue(':apellidos', str(newdata[1]))
        query.bindValue(':telefono', str(newdata[2]))
        query.bindValue(':email', str(newdata[3]))
        if query.exec_():
            print('Contacto modificado')
            var.ui.labelEstado.setText('Contacto ' + str(newdata[0]) + ' modificado')
        else:
            print("Error modificar contacto: ", query.lastError().text())


    '''Módulo para comprobar si existe un contacto'''
    def existeContacto(id):
        try:
            salida = False
            query = QtSql.QSqlQuery()
            query.prepare('select nombre from contactos')
            if query.exec_():
                while query.next():
                    nombre = query.value(0)
                    if (nombre == id):
                        salida = True
            return salida
        except Exception as error:
            print('Error no existe contacto: %s' % str(error))


    '''Módulo para buscar contacto'''
    def buscarContacto(self):
        global apellidos
        global nombre
        global telefono
        global email

        id = var.ui.lineNombre.text()

        if conexion.Conexion.existeContacto(id):
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select apellidos, nombre, telefono, email from contactos where nombre=:nombre')
            query.bindValue(':nombre', id)

            if query.exec_():
                while query.next():
                    apellidos = query.value(0)
                    nombre = query.value(1)
                    telefono = query.value(2)
                    email = query.value(3)
                    var.ui.tablaValores.setRowCount(index + 1)
                    var.ui.tablaValores.setItem(index, 0, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tablaValores.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tablaValores.setItem(index, 2, QtWidgets.QTableWidgetItem(telefono))
                    var.ui.tablaValores.setItem(index, 3, QtWidgets.QTableWidgetItem(email))
                    index += 1
            else:
                print('Error buscar contacto: ', query.lastError().text())

            var.ui.lineApellidos.setText(apellidos)
            var.ui.lineNombre.setText(nombre)
            var.ui.lineTlfno.setText(telefono)
            var.ui.lineEmail.setText(email)

            var.ui.labelEstado.setText('El contacto con Nombre ' + nombre + 'fue encontrado' % id)
        else:
            contactos.Contactos.limpiarContacto(self)
            var.ui.lineNombre.setText(id)
            var.ui.labelEstado.setText('Contacto con Nombre ' + nombre + 'no encontrado' % id)
            var.ui.lineNombre.setText(id)