import sys

class Eventos:
    def Salir():
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))