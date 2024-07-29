from tkinter import *

raiz=Tk()

raiz.title("Mi primera ventana con Tk")
#raiz.resizable(0,0)#este metodo sirve para que no se pueda cambiar el tamaño de la ventana,recibe valores bool
#recibe 2 parametros lo cuales son width y height
raiz.iconbitmap("./interfaces graficas/img/favicon.ico") #cambia el icono de la ventana
#raiz.geometry("650x350")#cambia el tamaño de la ventana ancho x alto
raiz.config(bg="black")#Color de fondo de la ventana
raiz.config(bd="45")#bd border
raiz.config(cursor="pirate")
raiz.config(relief="sunken")

miFrame = Frame()#Creación de nuestro Frame (no está dentro la raiz)
#La propiedad anchor utiliza los puntos cardinales en ingles N=north, S=soud, W=west, E=east
#miFrame.pack(side="right", anchor="s" )#empaquetamos nuestro frame dentro la raiz
#miFrame.pack(fill="x")#Rellena de manera horizontal la raíz
#miFrame.pack(fill="y",expand="True")#Si no colocamos el atributo expand fill no va a hacer nada, solo quedarse en medio
#miFrame.pack(fill="both",expand="True")#Se expande en toda la raíz
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="300", height="300")
miFrame.config(bd="35")#bd border
miFrame.config(cursor="hand2")
miFrame.config(relief="groove")#Estilo del borde

raiz.mainloop() #Este metodo debe estar siempre al final del codigo