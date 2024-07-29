from tkinter import *

#Formato de label: variableLabel=label(contenedor, opciones)
ventana = Tk()

miFrame=Frame(ventana, width=500,height=400)
miFrame.pack()
'''
miLabel = Label(miFrame,text="Hola a todos")#Especificamos el contenedor padre que va a ser miFrame
miLabel.place(x=0,y=0)#Nos va permitir ubicar el texto en cualquier lugar dentro nuestra interfaz grafica
#se introduce coordenadas con X y Y en pixeles, partiendo desde el borde derecho en X y superior en Y
'''
miImagen = PhotoImage(file="./interfaces graficas/img/mechas.gif")
#UNA MANERA DE ABREVIAR, SI ES QUE NO LO VAMOS A UTILIZAR MÁS ADELANTE ES:
Label(miFrame,text="Hola a todos",fg="green",font=("Comic Sans MS",20)).place(x=0,y=0)
Label(miFrame,image=miImagen).place(x=0,y=50)
ventana.mainloop()