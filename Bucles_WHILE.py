import math
#                               BUCLE WHILE
# Este se cosidera un bucle indetermido debido a que no sabemos cuantas veces se ejecutará el codigo
# del interior

#Formato del bucle: While condicion:
#       Cuerpo del bucle
'''
i = 1
while i <= 10:
    print("la ejecución " + str(i))
    i+=1

print("Termino la ejecución")
'''
'''
edad = int(input("Introduce tu edad por favor: "))
while edad < 5 or edad > 99:
    print("Has intruducido una edad negativa o no existe")
    edad = int(input("Introduce tu edad por favor: "))

print("Gracias por participar")
print("Tu edad es " + str(edad))
'''
'''
print("Programa de calculo de raiz cuadrada")
num = int(input("Induduce un numero: "))
intentos = 0
while num < 0:
    print("No sé puede hallar la raiz de un numero negativo")
    if intentos == 2:
        print("Haz hecho más de dos intentos. Gracias por participar")
        break;
    num = int(input("Induduce un numero: "))
    if num<0:
        intentos+=1
if intentos < 2:
    solucion = math.sqrt(num)
    print("la raiz cuadrada de " + str(num) + " es: " + str(solucion))
'''
# INSTRUCCIONES CONTINUE, PASS Y ELSE
#continue los que hace es saltar a la siguiente iteración 
#pass lo que hace es devolver null en cuanto se lee en el inerior del bucle
#else funciona a como lo hace dentro de un condicional

#                   EJEMPLOS CONTINUE
'''
for letra in "Python":
    if letra == "h": #A cada vuelta del bucle va a evaluar la condición y cuando se cumple va a ignorar el 
        continue     #resto del bucle y pasar a la siguiente parte del bucle "o"
    print("viendo la letra: ", letra)
'''
'''
nombre = "Mauro Soliz"
contador = 0
for i in nombre:

    if i == " ":
        continue

    contador+=1

print(contador)
'''
#               EJEMPLOS PASS
#Se utiliza en casos muy concretos
''' 
while True: #Esto es un bucle infinito y si no queremos que se ejecute le ponemos pass
    pass
class MiClas: #Tambien se puede utilizar si es que tenemos una clase o función imcompleta
    pass #PARA IMPLEMENTAR MÁS TARDE
'''

#                   EJEMPLOS ELSE

email = input("Introduce tu email: ")

for i in email:
    if i == "@":
        arroba = True
        break;
else:
    arroba = False
print(arroba)