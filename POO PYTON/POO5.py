#En esta parte vamos a aprender la encapsulacion de metodos
#En la anterior parte vimos encapsulación de variables
class Coche(): 
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 
        self.__color = "rojo"
        self.__enmarcha = False 

    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()
        if(self.__enmarcha and chequeo):
            return "El coche está encendido"
        elif(self.__enmarcha and chequeo==False):
            return "Algo esta fallando en el chequeo, porfavor verificar"
        else:
            return "El coche está parado"

    def estado(self): 
        print("El coche tiene: ", self.__ruedas," ruedas")
        print("El coche es de color: ",self.__color)
        print("El coche tiene un ancho de: ",self.__anchoChasis)
        print("El coche tiene un largo de: ",self.__largoChasis)

    def __chequeo_interno(self): #La manera de encapsular un metodo es la misma que el de las variables
        print("realizando chequeo interno")
        #Creamos nuevas variables
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if self.aceite == "ok" and self.gasolina == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

miCoche = Coche()
print(miCoche.arrancar(True)) 
miCoche.estado()
#print(miCoche.chequeo_interno()) #Esto no deberia pasar
print("--------------------------A continuación creamos el segundo objeto------------------")
miCoche2 = Coche() 
print(miCoche2.arrancar(False))
miCoche2.estado() 