import var

class Clientes():
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