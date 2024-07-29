'''
                                            TUPLAS
Las tuplas y la listas son dos cosas completamente diferentes. Las tupla son listas inmutables,es decir, no se
pueden modificar despues de su creación.
- No permieten añadir, eliminar y modificar elementos ect (no append, extend y remove)
- Si permiten extraer porciones, pero el resultado la extracción es una nueva tupla
- No permiten busquedas (no index)
- Si permiten comprobar si un elemento existe en una tupla
¿Qué utilidad o ventaja tienen respecto a las listas?
- Más rapidas
- Menos espacio(Mayor optimización)
- Formatean Strings
- Pueden utilizarse como claves en un diccionario.(Las listas no)
'''
#SINTAXIS TUPLAS
#miTupla = (elemento1,elemento2,elemento3)

mitupla = ("Juan",23,1998,True)
print(mitupla[2])