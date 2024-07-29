from tkinter import *

raiz = Tk()

miFrame=Frame(raiz,width=1000,height=600)
miFrame.pack()
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1,padx=5,pady=5)#En vez place utilizamos grid

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=5,pady=5)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2,column=1,padx=5,pady=5)
cuadroPass.config(show="*")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=5,pady=5)

#Esta manera no es aconsejable si vamos a hacer un programa grande
nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=5,pady=5)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky="e",padx=5,pady=5)

passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=2,column=0,sticky="e",padx=5,pady=5)

dirLabel=Label(miFrame,text="Dirección del hogar:")
dirLabel.grid(row=3,column=0,sticky="w",padx=5,pady=5)

raiz.mainloop()