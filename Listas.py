'''
Las listas en Python son el equivalente a los arrays o vectores y su función es la misma, este permite alma-
senar una gran cantidad de valore
'''
# nombreLista = [elemento1, elemento2, elemento3]
miLista = ['Manzana','Uva','Pera','Naranja','Mandarina'] #He comprobado que se puede utilizar comillas simples('') y comillas dobles("")
#print(miLista[:]) #Imprime toda la lista
#print(miLista[1]) #De esta manera accedemos a un elemento en concreto, el index comienza en 0
#print(miLista[-1]) #Se cuenta en reversa
#print(miLista[0:3]) #Imprime los primeros tres elementos, iniciando desde 0
#print(miLista[:3]) #Python sobre entiende que la lista inicia en 0

#Una manera de agregar elementos al final de una lista en Python es atraves de la función "append"
'''
fruta = input("Ingrese una fruta a la lista: ")
miLista.append(fruta) #append nos sirve para agregar elementos al final de la lista lista
print(miLista)
'''
'''
miLista.insert(2,"Maracuya") #La funcion (insert) tambien se encarga de agregar elementos a una lista solo que esta función
                #nos pide dos argunmentos, primero la posición o indice y luego el elemento que queremos
                #introducir
print(miLista)
'''
#miLista.extend(["Tomate","Cebolla","Papa"]) #Lo que hace extend es concatenar otra lista a la ya existente
#print(miLista[:])
#print(miLista.index("Uva")) #Devuelve el indice en el que se encuentra el elemento
#print("Platano" in miLista)#La función sirve para saber si un elemento se encuentra en la lista(true o false)
#####
#Las listas de Python pueden almacenar distintos tipos de datos en una lista
#####
miLista2 = ["Maria", 23, 70.4, True]
#miLista.remove("Naranja") #remove nos sirve para eliminar un elemento de nuestra lista
#print(miLista2[:])
#print(miLista)
#miLista.pop() #pop nos sirve para eliminar el ultimo elemnto de una lista
#print(miLista[:])
'''
miLista3 = miLista + miLista2 #Este operador se puede hacer en Python, lo que es la suma de listas
print(miLista3[:])            #No es lo mismo que la funcion extend, ya que este funciona como concatenador
'''
miLista = miLista * 3 #Otro operador que podemos utilizar en la listas de Python es la multiplicación
print(miLista[:])