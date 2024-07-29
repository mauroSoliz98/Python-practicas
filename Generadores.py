#                                   GENERADORES
'''
¿Qué son?
- Son estructuras que extraen valores de una función y se almacenan objetos iterables (que se pueden recorrer)
- Estos valores se almecenan de uno en uno dentro del generador
- Cada vez que un generador almacena un valor, este permanecerá en un estado pausado hasta que se solicita el
siguiente. Esta caracteristica es conocida como "suspencion de estado"

Funcion tradicional
Def generarNumero():
    return numeros

Generador
Def generarNumero():
    yield numeros

¿Qué utilidad tienen?
- Son más eficientes que la funciones tradicionales
- Muy utiles con listas de valores infinitos
- Bajo determinados escenarios, será muy util que un generador devuelva valores de uno en uno
'''
'''
def NumerosPares(limite):
    num = 1
    lista=[]
    while num < limite:
        lista.append(num*2)
        num+=1
    return lista

print(NumerosPares(10))
'''
'''
def NumerosPares(limite):
    num = 1
    lista=[]
    while num < limite:
        yield num*2
        num+=1
devuelvePares = NumerosPares(10)

for i in devuelvePares:
    print(i, end = " ")

#Ahora queremos que nos devuelva los tres primero elemetos
print(next(devuelvePares)) #De esta manera conseguimos que nos devuelva el primer valor que tiene en su interior

print("Más codigo......")
print(next(devuelvePares))

print("Más codigo......")
print(next(devuelvePares))
'''