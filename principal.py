#Interfaz grafica principal- GUI

import tkinter as tk
from tkinter import Variable, ttk


#Crear la ventana
ventana = tk.Tk()

#Declaracion de variables
cantidadVariables=tk.StringVar(value='0')
cantidadRestricciones=tk.StringVar(value='0')
datos = ['Metodo Gráfico', 'Simplex Dos Fases']
signo=['<=','>=','=']
vectorRestricciones=[]

#Variables de interface
funcionObjetivo=[]
matrixRestricciones=[]

#Componentes vista
lblMetodo1=tk.Label(ventana,text='')
lblMetodo2=tk.Label(ventana,text='Planteamiento del problema')
lblVaribles=tk.Label(ventana,text='Cantidad de variables')
lblRestricciones=tk.Label(ventana,text='Cantidad de restricciones')
lblMetodo=tk.Label(ventana,text='Metodo a utilizar')
#Cajas de texto
txtVariables=ttk.Entry(ventana,width=10, justify=tk.LEFT, textvariable=cantidadVariables)
txtRestricciones=ttk.Entry(ventana,width=10, justify=tk.LEFT, textvariable=cantidadRestricciones)
txtResultados=[]
#ComboBox
comboBox=ttk.Combobox(ventana,width=15,values=datos)
comboBoxSigno=[]


#Eventos
def evento_click():
    #Eliminar componentes de la vista
    eliminar_componente(lblMetodo1)
    eliminar_componente(lblMetodo2)
    eliminar_componente(lblMetodo)
    eliminar_componente(lblRestricciones)
    eliminar_componente(lblVaribles)
    eliminar_componente(txtRestricciones)
    eliminar_componente(txtVariables)
    eliminar_componente(comboBox)
    eliminar_componente(botonEnviar)

    #Generar la nueva vista de las restriciones
    vista_funcion_objetivo()
    vista_restricciones()

def obtener_datos():
    print('Despejar ecuaciones')
    print('Guardar en el nuevo')
    print(funcionObjetivo[0].get())
    
#Botonoes
botonEnviar = ttk.Button(ventana,text='Aceptar',command=evento_click);
botonDatosFunciones=ttk.Button(ventana,text='Enviar Datos',command=obtener_datos)


#Funciones de componentes de interface 
def componentes_principal():
    #Labels
    lblMetodo1.grid(row=0,column=3)
    lblMetodo2.grid(row=0,column=4)
    lblVaribles.grid(row=2,column=4)
    lblRestricciones.grid(row=3,column=4)
    lblMetodo.grid(row=1,column=4)
    
    #entrada1=ttk.Entry(ventana,width=10, justify=tk.LEFT, state=tk.DISABLED)
    txtVariables.grid(row=2,column=5)
    txtRestricciones.grid(row=3,column=5)

    comboBox.grid(row=1,column=5)


def eliminar_componente(componente):
    componente.destroy()


def vista_funcion_objetivo():
    columna=0
    lblFuncionObejtivo = tk.Label(ventana,text='Funcion Objetivo')
    lblFuncionObejtivo.grid(row=0,column=0)
    for i in range(0,int(cantidadVariables.get()),1):
        columna+=1
        funcionObjetivo.insert(i,ttk.Entry(ventana,width=10, justify=tk.LEFT))
        funcionObjetivo[i].grid(row=0,column=columna);
        columna+=1
        if((int(cantidadVariables.get())-1)>i):
                lblVariable=tk.Label(ventana,text='x'+str(i+1)+' +')
                lblVariable.grid(row=0,column=columna)
        else:
                lblVariable=tk.Label(ventana,text='x'+str(i+1))
                lblVariable.grid(row=0,column=columna);

def vista_restricciones():
    columna=0
    posicion=0
    mas=0
    lblSubjetoA=tk.Label(ventana,text='S.A')
    lblSubjetoA.grid(row=1,column=0);
    for i in range(0,int(cantidadRestricciones.get())):
        lblTitleRestricciones=tk.Label(ventana,text='Restriccion '+str(i+1))
        lblTitleRestricciones.grid(row=i+2,column=columna);
        for j in range(0,int(cantidadVariables.get()),1):
            mas+=1
            columna+=1
            vectorRestricciones.insert(posicion,ttk.Entry(ventana,width=10, justify=tk.LEFT))
            vectorRestricciones[posicion].grid(row=i+2,column=columna);
            columna+=1
            print(mas)
            if(int(cantidadVariables.get())>mas):
                lblRestricciones2=tk.Label(ventana,text='x'+str(j+1)+' +')
                lblRestricciones2.grid(row=i+2,column=columna)
                print('entro +')
            else:
                lblRestricciones2=tk.Label(ventana,text='x'+str(j+1))
                lblRestricciones2.grid(row=i+2,column=columna)
                print('no entro')
            posicion+=1
        mas=0
        comboBoxSigno.insert(i, ttk.Combobox(ventana,width=5,values=signo))
        comboBoxSigno[i].grid(row=i+2,column=columna+1)
        txtResultados.insert(i,ttk.Entry(ventana,width=10, justify=tk.LEFT))
        txtResultados[i].grid(row=i+2,column=columna+2)
        columna=0
    botonDatosFunciones.grid(row=int(cantidadRestricciones.get())+2,column=0)


#Tamaño de la ventana
ventana.geometry('400x400');
#Nombre de la ventana
ventana.title('Ejercicio Simplex');

componentes_principal()
#Boton
botonEnviar.grid(row=5,column=5)#Mostrar el boton

#Abrir la ventana
ventana.mainloop();



