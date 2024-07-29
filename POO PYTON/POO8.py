'''
HERENCIA
- super() este llama al metodo de la clase padre allá donde este
- instance()
- isintance() se encarga de informarnos si un objeto es intancia de una clase determinada
este devuelve True si pertenece a una clase en concreto y devuelve False si no lo es
'''
class Persona:
    def __init__(self, nombre, edad, Lugar_residencia):

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = Lugar_residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre,
        "\nEdad: ",self.edad,
        "\nLugar de residencia: ", self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, lugarRes_empleado):#cramos nuestro
        #constructor de Empleado
        
        super().__init__(nombre_empleado,edad_empleado,lugarRes_empleado)#Con super() le estamos agregando los
        #valore de nuestro constructor Empleado y tambien hacemos uso de los valores que hay en el constructor
        #de Persona
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion_empleado(self):
        super().descripcion()#Lo que hace la clase super() es ir al metodo de la clase padre, ejecutarlo en 
        #su totalidad y luego se ejecuta la siguiente linea
        print("Salario: ",self.salario,"\nAntiguedad: ", self.antiguedad," años")

p1 = Persona("Mauro Soliz",32,"Cochabamba")
p1.descripcion()

print("\nDESCRIPCIÓN DE EMPLEADO")
e1 = Empleado(2500,10,"Mateo Vera",34,"La Paz")
e1.descripcion_empleado()

print("\nEs una instancia")
print(isinstance(p1,Empleado))