'''
¿QUÉ ES LA HERENCIA EN LA PROGRAMACIÓN ORIENTADA A OBJETOS?

                                            CLASE 1
                                                |
                                                |
                                            CLASE 2
                                                |
                            --------------------|------------------------
                            |                   |                       |
                          CLASE 3            CLASE 4                  CLASE 5
CLASE 1 (CLASE PADRE, SUPERCLASE)
CLASE 2 (SUBCLASE, SUPERCLASE DE LA CLASE 1,4 Y 5)

¿PARA QUÉ SIRVE LA HERENCIA?
Para reutilizar código en caso de que existan objetos similares.
Por ejemplo buses, camiones, automoviles, etc tienen algo en común, el cual es:
- Marca
- Modelo
Al igual que todos estos objetos van a tener comportamientos comunes
como son: arrancar, acelerar y frenar 
'''
#Creamos una clase padre
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ", self.modelo)
        print("En marcha: ",self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

#                                           POO 7
#Sobrescritura de metodo y herencia multiple
# Python es uno de los lenguajes de programción que admite la herencia multiple       
    
class Moto(Vehiculo): #La manera de heredar en Python es solo escribiendo el nombre de la clase que queremos 
    #heredar dentro el contructor de la clase. Al hacer la herencia, hereda todo, incluido el constructor padre
    hcaballito = "" #hacer caballito(elevar la rueda delantera)
    def caballito(self):
        self.hcaballito = "Voy haciedo el caballito"
    #A esto se le llama sobre escribir, que consiste en crear dentro la clase moto un metodo con el mismo 
    #nombre de la clase padre y ademas con el mismo numero de parametro.
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ", self.modelo)
        print("En marcha: ",self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,"\n",self.hcaballito)

class Furgoneta(Vehiculo):
    def Carga(self,cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class VElectricos(Vehiculo):
    def __init__(self, marca,modelo): #Lo que hace es iniciar una autonomia
        super().__init__(marca, modelo)
        self.autonomia = 100

    def CargarEnergia(self):
        self.cargando = True

miMoto = Moto("Honda","Hornet 750")
miMoto.caballito()
miMoto.estado()
print("||||||||||||| CLASE FURGONETA ||||||||||||||\n")
miFurgoneta = Furgoneta("Toyota","Pajero") #Al heredar de Vehiculos, necesita los parametros marca y modelo
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.Carga(True)) 

class BicicletaElectrica(VElectricos,Vehiculo):#Python nos permite heredar de dos clases diferentes
    pass
#NOTA: Al hacer herencia multiple, se da preferencia a la clase que se indique primero
#para mas info minuto 23:00 https://www.youtube.com/watch?v=jMQQN9OxwVc&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=30
miBici = BicicletaElectrica("Orbea","VHD343")
print(miBici.autonomia)