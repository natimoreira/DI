from PyQt5 import QtWidgets, QtSql

import var
import conexion

class Contactos():
    '''
    Módulo para dar de alta contacto
    '''
    def altaContacto(self):
        try:
            #Preparamos el registro
            newContact = []
            contactTab = []  #serán los datos que carguemos en la tabla
            contact = [var.ui.lineApellido, var.ui.lineNombre, var.ui.lineTlfno, var.ui.lineEmail]
            k = 0
            for i in contact:
                newContact.append(i.text())
                #carguemos los valores para la tabla
                if k < 4:
                    contactTab.append(i.text())
                    k += 1
            print(newContact)
            print(contactTab)
            if contact:
            #comprobamos que no esté vacío lo principal
            #aquí empieza como trabajar con la TableWidget
                row = 0  #posición de la fila, problema: coloca al último como primero en cada click
                column = 0  #posición de la columna
                var.ui.tablaValores_2.insertRow(row)  #insertamos una fila nueva con cada click de botón
                for registro in contactTab:
                    #la celda tiene una posición fila, columna y cargamos en ella el dato
                    cell = QtWidgets.QTableWidgetItem(registro)  #carga en cell cada dato de la lista
                    var.ui.tablaValores_2.setItem(row, column, cell)  #lo escribe
                    column += 1
                conexion.Conexion.cargarContacto(newContact)
            else:
                print('Faltan datos')
            Contactos.limpiarContacto(self)
        except Exception as error:
            print('Error alta contacto %s ' % str(error))


    '''Módulo para dar de baja un cliente'''
    def bajaContacto(self):
        try:
            nombre = var.ui.lineNombre.text()
            conexion.Conexion.borrarContacto(nombre)
            conexion.Conexion.mostrarContactos(self)
            Contactos.limpiarContacto()
        except Exception as error:
            print('Error borrar contacto: %s ' % str(error))


    '''Módulo para modificar datos de un contacto'''
    def editContacto(self):
        try:
            newdata = []
            contact = [var.ui.lineApellido, var.ui.lineNombre, var.ui.lineTlfno, var.ui.lineEmail]
            for i in contact:
                newdata.append(i.text())  # cargamos los valores que hay en los editline
            conexion.Conexion.modifContacto(newdata)
            conexion.Conexion.mostrarContactos(self)
        except Exception as error:
            print('Error modificar contacto: %s ' % str(error))


    '''Módulo para restaurar formulario'''
    def limpiarContacto(self):
        var.ui.lineApellido.setText("")
        var.ui.lineNombre.setText("")
        var.ui.lineTlfno.setText("")
        var.ui.lineEmail.setText("")