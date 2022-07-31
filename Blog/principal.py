#Interfaz grafica principal- GUI

import tkinter as tk
from tkinter import Variable, ttk

from numpy import delete #Componentes de tkinter

#Crear la ventana
ventana = tk.Tk()

#Declaracion de variables
cantidadVariables=tk.StringVar(value='0')
cantidadRestricciones=tk.StringVar(value='0')
misObjetos=[

]
matrixRestricciones=[]

#Funciones de impresion de componentes.
def componentes_principal():
    #Labels
    lblMetodo=tk.Label(ventana,text='')
    lblMetodo.grid(row=0,column=3)
    lblMetodo=tk.Label(ventana,text='Planteamiento del problema')
    lblMetodo.grid(row=0,column=4)
    lblVaribles=tk.Label(ventana,text='Cantidad de variables')
    lblVaribles.grid(row=2,column=4)
    lblRestricciones=tk.Label(ventana,text='Cantidad de restricciones')
    lblRestricciones.grid(row=3,column=4)
    lblMetodo=tk.Label(ventana,text='Metodo a utilizar')
    lblMetodo.grid(row=1,column=4)

    #Cajas de texto
    txtVariables=ttk.Entry(ventana,width=10, justify=tk.LEFT, textvariable=cantidadVariables)
    #entrada1=ttk.Entry(ventana,width=10, justify=tk.LEFT, state=tk.DISABLED)
    txtVariables.grid(row=2,column=5)
    txtRestricciones=ttk.Entry(ventana,width=10, justify=tk.LEFT, textvariable=cantidadRestricciones)
    txtRestricciones.grid(row=3,column=5)

    #ComboBox
    datos = ['Metodo Gráfico', 'Simplex Dos Fases']
    comboBox=ttk.Combobox(ventana,width=15,values=datos)
    comboBox.grid(row=1,column=5)

#Metodos
def evento_click():
    print(cantidadRestricciones.get())
    print(cantidadVariables.get())
    #Generar la nueva vista de las restriciones
    vista_restricciones();

def vista_restricciones():
    numero=int(cantidadRestricciones.get())
    #for i in range(0,numero,1):
            
    print('entro');



#Tamaño de la ventana
ventana.geometry('400x400');
#Nombre de la ventana
ventana.title('Ejercicio Simplex');

componentes_principal()
#Boton
botonEnviar = ttk.Button(ventana,text='Enviar datos',command=evento_click);
botonEnviar.grid(row=5,column=5)#Mostrar el boton

#Abrir la ventana
ventana.mainloop();



