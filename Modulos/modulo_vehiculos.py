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

    
class Moto(Vehiculo): 
    hcaballito = "" 
    def caballito(self):
        self.hcaballito = "Voy haciedo el caballito"
    
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
    def __init__(self, marca,modelo): 
        super().__init__(marca, modelo)
        self.autonomia = 100

    def CargarEnergia(self):
        self.cargando = True