#                               WIGETS TEXT AND BUTTON

from tkinter import *

raiz = Tk()

minombre = StringVar()
def codigoBoton():
    minombre.set("Mauro")

miFrame=Frame(raiz,width=1000,height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=5,pady=5)#En vez place utilizamos grid

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=5,pady=5)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2,column=1,padx=5,pady=5)
cuadroPass.config(show="*")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=5,pady=5)

comentarioTexto=Text(miFrame,width=16, height=5) 
comentarioTexto.grid(row=4,column=1,padx=5,pady=5)
scrollY=Scrollbar(miFrame,command=comentarioTexto.yview)#Le estamos agregando a Text un scrollbar vertical
scrollY.grid(row=4, column=1, pady=5, sticky="nse")#Para que el scrollbar se incorpore en el cuadro de texto
comentarioTexto.config(yscrollcommand=scrollY.set)#inabilita el scrollbar mientras no sea necesario 

#Esta manera no es aconsejable si vamos a hacer un programa grande
nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=5,pady=5)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky="e",padx=5,pady=5)

passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=2,column=0,sticky="e",padx=5,pady=5)

dirLabel=Label(miFrame,text="Dirección:")
dirLabel.grid(row=3,column=0,sticky="w",padx=5,pady=5)

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=4,column=0,sticky="w",padx=5,pady=5)

enviarBtn=Button(miFrame,text="Enviar",command=codigoBoton)
enviarBtn.grid(row=5,column=1,padx=5,pady=5)

raiz.mainloop()