import math
#                                   ¿QUÉ ES UNA EXCEPCION?
'''
La excepción es un error en tiempo de ejecución del programa. La sintaxis del codigo es correcta pero durante
la ejecución ha ocurrido algo inesperado
'''
'''
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:
        return num1/num2

    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operación erronea"
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa ")
'''
#                                               EXCEPCIONES II

#Capturar varias excepciones 
#Uso de la clausula finally
'''
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:
        return num1/num2

    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operación erronea"
while True:	
	try:
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break
	except ValueError: #Captura otro tipo de errores
		print("Los valores introducidos no son correctos. Intenta lo de nuevo")		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa ")
'''
'''
def divide():
	try:
		op1 = (float(input("Introduce el primer numero: ")))
		op2 = (float(input("Introduce el segundo numero: ")))
		print("La division es: " + str(op1/op2))
	except ValueError:
		print("El valor introducido no es correcto")
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
	finally: #Con la clausula finally el codigo dentro del mismo siempre se va a ejecutar no importa si ha 
			 # ocurrido un error o no.
		print("calculo finalizado")

divide()
'''
#										EXCEPCIONES III
'''
- Intruccion Rise
- Creacion de excepciones propias
'''
'''
def evaluaEdad(edad):
	if edad < 0:
		raise TypeError("No se permiten edades negativas") #La instrucción raise nos permite lanzar las
														   #excepciones y mensajes que queramos
	if edad < 20:
		return "Eres muy joven"
	elif edad < 40:
		return "Eres joven"
	elif edad < 65:
		return "Eres maduro"
	elif edad < 100:
		return "Cuidate...."
UserEdad = int(input("Introduce tu edad: "))
print(evaluaEdad(UserEdad))
'''
def calculaRaiz(num1):
	if num1 < 0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(num1)

op1 = int(input("Introduce un numero: "))
try:
	print(calculaRaiz(op1))
except ValueError as E:
	print(E)
print("Fin del programa")