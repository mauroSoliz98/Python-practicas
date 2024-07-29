'''
                        BUCLES
La funcion de los bucles es repetir codigo, y en python existe distintos tipos entre los que podemos encontrar
los determinados y los indeterminados
BUCLE FOR
DETERMINADOS
- Se ejecutan un numero determinado de veces
- Se sabe cuatas veces se va a ejecutar el bucle
INDETERMINADOS
- Se ejecutan un numero indeterminado de veces
- No se sabe cuantas veces se va a ejecutar el codigo dentro del bucle
- Las repeticiones dependeran de las circunstancias 
SINTAXIS BUCLE FOR
for variable in elemento a recorrer:
'''
from math import factorial
#for i in [1,2,3]:
    #print("HOLA")
print("|||||||||||||||||||||||||||||||||||||||||")
#for i in ["primavera","verano","otoño","invierno"]:
    #print(i)
    #print("Hola")

#for i in ["Palta","Platano","Piña"]:
    #print(i, end="")
    #print(i, end=" ")
    #print(i, end=",")

#for i in "maursosoliz@gmail.com":
    #print("hola")

#ESCALERA NUMERICA
cant = int(input("Ingrese un numero: "))

for fila in range(1, cant + 1):
    for columna in range(1, fila + 1):
        print(columna, end=" ") 
    print()

#PIRAMIDE CON ASTERISCOS
altura=5
asteriscos=1

#NOTA RANGE FUNCIONA DE LA SIGUIENTE MANERA
# range(de altura, a 0, con -1)->desde, hasta, condición 
for espacios in range(altura,0, -1):
    #e (espacio)
    for e in range(espacios): #Va hasta el numero de espacios que hay actualmente
        print("  ", end=" ") #La clave está aqui, remplaze los dos espacios

    for a in range(asteriscos):
        print("* ", end="")

    print()
    asteriscos+=2

# TRIANGULO DE PASCAL
#numero de filas a introducir
filas= int(input("Coloque la cantidad de filas: "))

for i in range(filas):
    #Con la siguiente iteración obtendremos los espacios principales
    for j in range(filas-i + 1):
        print(end=" ")
    #Obtenemos los elemnento de la fila i
    for j in range(i+1):
        #nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        #El operador "//" Realiza la división con resultado de numero entero
    
    print()
    
#                               PRACTICA
'''
email = False
miEmail = input("Introduzca una dirección de correo electronico: ")
for i in miEmail:
    if(i == "@"):
        email=True

if email==True:
    print("El email es correcto")   
else:
    print("El email no es corrcto")
'''

#EJERCICIO 1 CONTADOR DE LETRAS Y LETRAS REPETIDAS
palabra = input("Introduzca una palabra: ")
letra_cont = input("Ingrese la letra que desea contar: ")
contador_letras = 0
contador_letras_por_usuario = 0
for letra in palabra:
    contador_letras+=1

for letra in palabra:
    if(letra == letra_cont):
        contador_letras_por_usuario += 1
print("la palabra ",palabra," tiene:",contador_letras," letras")
print("la cantidad de letras", letra_cont,"'s en ",palabra," son: ",contador_letras_por_usuario)

'''
#RANGE
for i in range(5): #Un range es lo más parecido a un array
    print(f"valor de la variable: {i}") #Al poner f le decimos a python que queremos utilizar una notación especial

for i in range(5,10): #Le estamos diciendo que cuente desde el 5 hasta el 9
    print(i, end=" ")

for i in range(5,100,10):
#El tercer argumento indica de cuanto en cuanto va ir
    print(f"valor: {i}")

#PRACTICA 2 EMAIL CORRECTO
valido = False
email = input("Introduce un email: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("El email es correcto")
else:
    print("No es un email verdadero")
'''