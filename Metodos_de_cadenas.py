#                                               METODOS DE CADENAS
#Python al ser un leguanjo orientado 100% a objeto, este tambien cosidera a las cadeanas caracteres(palabras)
#objetos String. Ahora vamos a aprender todos los metodos que manipulan cadenas en Python
'''
upper(): convierte en mayusculas todas las letras de un string.
lower(): convierte en minusculas todas las letras de un string.
capitalize(): en un string pone la primera letra en mayuscula.
count(): cuenta cuantas veces aparece una letra o una cadena de caracteres dentro de un texto o dentro de una
frace.
find(): reprenta el indice o pocisión en la cual aparece un caracter o un grupo de caracteres dentro de un texto.
isdigit(): devuelve un booleano True o False. Lo que hace es decirnos si lo que a sido introducido es un valor.
numérico o no lo es.
isalum(): Comprueba si son alfanuméricos. 
isalpha(): Comprueba si hay solo letras los espacios no cuentan.
split(): Separa por palabras utilizando espacios.
strip(): Borra los espacios sobrante al principio y al final.
replace(): Cambia una palabra o una letra por otra dentro de un string.
rfind(): hace lo mismo que find() pero contando desde atras.
'''
'''
nombreUsuario = input("Introduzca su nombre de usuario: ")
print("Mi nombre es: ", nombreUsuario.upper())
print("Mi nombre es: ", nombreUsuario.capitalize())

print("------------EJERCICIO DE EDAD--------------")
edad = input("Introduce una edad: ")

while edad.isdigit() == False:
    print("Porfavor introduce un valor numerico")
    edad = input("Introduce una edad: ")

if int(edad) < 18:
    print("No puede pasar")
else:
    print("Puede pasar")
'''
email = input("Introduzca su email: ")
while email.count("@")==0:
    print("NO INGRESO UN EMAIL REAL,INTENTE OTRA VEZ")
    email = input("Introduzca su email: ")

if email.count("@") > 0 and email.count("@") < 2:
    print("Es un email")
else:
    print("No es un email")