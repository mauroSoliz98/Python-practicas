'''
                                    MANIPULACIÓN DE ARCHIVOS EXTERNOS

Se aprenderá a como trabajar con ficheros externos de texto con modulo IO
Objetivo: la persistencia de datos
Dos alternativas
- Manejo de archivos externo
- Trabajo con BBDD
Fases necesarias para guardar la información en archivos externos
(Creación) --> (Apertura) --> (Manipulación) --> (Cierre)
'''
from io import open

archivo_texto=open("MiArchivo.txt","r")#Se puede abrir un archivo en modo lectura,escritura y append 
#para edicionar texto. w=write, r=read, a=append
#seek() sirve para especificar en que numero de caracter queremos que se situe el puntero o cursor
'''
frase = "Hola mundo, soy Python \n Soy un lenguaje de tipado dinamico"
archivo_texto.write(frase)
archivo_texto.close()
'''
'''
texto=archivo_texto.read()
archivo_texto.close()
print(texto)
'''
'''
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto[0])
'''
'''
archivo_texto.write("\nSoy que no utiliza llaves sino sangria")
archivo_texto.close()
''' 
#video Archivos externos 2
print(archivo_texto.read())
print("\n2do recorrido\n")
archivo_texto.seek(0)
print(archivo_texto.read())
#Me he saltado a interfaces pero faltaba ver serialización 1y2 y Guardado