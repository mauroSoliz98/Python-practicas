#                                               POLIMORFISMO
#Hace referencia a que un objeto puede cambiar de forma dependiendo del contexto en el que se utilice y por
#lo tanto al cambiar de forma ese objeto, tambien cambia de comportamiento, esta es una caracteristica tre-
#mendamente potente, por suerte Python es un lenguaje de tipado dinamico por ende es una caracteristica sencilla
#de utilizar, ya que no necesitamos especificar de que tipo es un objeto a la hora de utilizarlo.

class Coche:
    def desplazamiento(self):
        print("Me desplazo usando cuatro ruedas")

class Moto:
    def desplazamiento(self):
        print("Me desplazo usando dos ruedas")

class Camion:
    def desplazamiento(self):
        print("Me despalzo usando seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()#<--- este metodo desplazamiento hace referencia al metodo desplazamiento de los
    #multiples objetos que tengan un metodo con un nombre igual

miVehiculo1=Coche()
desplazamientoVehiculo(miVehiculo1)