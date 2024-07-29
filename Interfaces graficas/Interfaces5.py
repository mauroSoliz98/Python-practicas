#                                           Practica Calculadora
from tkinter import *

raiz = Tk()

miFrame=Frame(raiz)
miFrame.pack()

#-----------------------PANTALLA-------------------------
numeroPantalla=StringVar()
pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,columnspan=4,padx=5,pady=5,sticky=(W,E))
pantalla.config(background="black",fg="white",justify="right")
#-----------------PULSACIONES TECLADO---------------------

#------------------------FILA 1-----------------------------
boton7=Button(miFrame,text="7",width=5)
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=5)
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=5)
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="%",width=5)
botonDiv.grid(row=2,column=4)
#------------------------FILA 2-----------------------------
boton4=Button(miFrame,text="4",width=5)
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=5)
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=5)
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="X",width=5)
botonMult.grid(row=3,column=4)
#------------------------FILA 3-----------------------------
boton1=Button(miFrame,text="1",width=5)
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width=5)
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3",width=5)
boton3.grid(row=4,column=3)
botonRes=Button(miFrame,text="-",width=5)
botonRes.grid(row=4,column=4)
#------------------------FILA 4-----------------------------
botonComa=Button(miFrame,text=",",width=5)
botonComa.grid(row=5,column=1)
boton0=Button(miFrame,text="0",width=5)
boton0.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=",width=5)
botonIgual.grid(row=5,column=3)
botonSum=Button(miFrame,text="+",width=5)
botonSum.grid(row=5,column=4)

raiz.mainloop()