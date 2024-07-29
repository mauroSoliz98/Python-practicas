#Estos es una pequeña practica basada en los cursos
#de: https://www.youtube.com/watch?v=VY448UWAQ_0&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=5
'''
                                        ¿Que es python? y ¿Para qué sirve?
Python es un leguaje de programación de proposito general, este ayuda a las buenas practicas de programación
cuenta con una basta cantidad de librerias y es un leguaje facíl de aprender
Otro beneficio de python es que este es un leguaje de tipado dinamico, lo que quiere decir que las variables
pueden ser reasignadas, por ejemplo:
book_name = "I Robot"
book_name = 1234
'''
'''
                                            CONVENCIONES
Las convenciones son las diferentes formas en la los programadores definen sus variables, por ejemplo:
book_name = "I Robot" Sanke Case
bookName = "I Robot" Camel Case
BookName = "I Robot" Pascal Case
'''
'''
def funcion_sumar(a,b):
    a = a
    b = b
    a = input("Ingrese el primer numero: ")
    b = input("Ingrese el segundo nuemro: ")
    suma = int(a) + int(b)
    return print(suma)
'''
def miLista():
    lista = ["Maria",23,True]
    print(lista[:]) #los ":" se utiliza para referirnos a todos los elementos de la lista 

def miTupla():
    tupla = () #La principal diferencia entre una lista y una tupla son los "()" aparte de otras cosas explicadas en el video

def login(log, pas):
    loginUser = "mau"
    passwordUser ="mau2398"
    if loginUser != log and passwordUser != pas:
        error()
    else:
        #funcion_sumar(a, b)
        miLista()

def error():
    return print("ERROR")


#primerNumero = ""
#segundoNumro = ""
print("|||||||MAIN MENU||||||")
logUser = input("|||| Login: ")
passUser = input("|||| Passwor: ")
login(logUser,passUser)
'''
print("hola mundo")
primerNumero = input("Ingrese el primer numero de una suma: ") # input una manera de establecer como entrada
segundoNumero = input("Ingrese el segundo nuemero de una suma: ")
#total = int(primerNumero) + int(segundoNumero) #se necesita catalogar ambas variables como int ya que para Python son objetos
#print("El resultado es: {}".format(total))
funcion_sumar(primerNumero,segundoNumero)
'''
'''
cinco = 5
type(cinco)
'''
