#Se crae la clase
'''
                                        NOTA
A la hora de querer definir un metodo usamos la siguiente sintaxis:
    def nombre_funcion (self):
        pass
el 'self' hace referencia al objeto perteneciente a la clase, este es el equibalente al 'this' que nos
encontramos en C#.
'pass' sirve para ignorar la funcion si es que la dejamos vacía(Esto en Sublime Text)
esto se debe a que es una funcion pertenesiente a la clase.
'''
class Coche: #El nombre de la clase siempre va en mayusculas
    #Creamos un METODO constructor de la siguiente manera y metemos las propiedades presediadas de la palabra
    #Self
    #En Java, C++ o C# El metodo constructor tiene el mismo nombre de la clase, en Python NO
    #Este tiene que tener __init__
    #La manera de encapsular en Python es poner la variable presedida de __(dos guiones bajos)
    def __init__(self):
#PROPIEDADES 
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #Ya está encapsulada ahora no se puede modificar desde el exterior de la clase
        self.__color = "rojo"
        self.__enmarcha = False #<----Esto es un constructor debido a que especificamos el estado inicial de los objetos

#EL COMPORTAMIENTO DEL OBJETOS ES DETERMINADO POR LOS METODOS DEL OBJETO
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if(self.__enmarcha):
            return "El coche está encendido"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene: ", self.__ruedas," ruedas")#Una vez encapsulada la variable ruedas debemos 
        #utilizarla con sus __(dos guiones bajos) que la precede
        print("El coche es de color: ",self.__color)
        print("El coche tiene un ancho de: ",self.__anchoChasis)
        print("El coche tiene un largo de: ",self.__largoChasis)
        

#¿COMO INSTANCIAMOS UN OBJETO?
#Primero se crea una variable
miCoche = Coche()#<---------Instanciar un clase
print(miCoche.arrancar(True)) 
miCoche.estado()
#NOTA: Lo que resive 'self' como parametro es el propio objeto, osea miCoche
#                                       POO 4
print("--------------------------A continuación creamos el segundo objeto------------------")
miCoche2 = Coche()
miCoche2.ruedas = 2 #Esto no debería pasar,pero igual va a funcionar, para que ocurra esto usamos la encapsulación   
print(miCoche2.arrancar(False))
miCoche2.estado() 
