#Interfaz grafica principal- GUI

import tkinter as tk
from tkinter import Variable, ttk, messagebox, scrolledtext
#Librerias para graficar
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

#Crear la ventana
ventana = tk.Tk()

#Declaracion de variables
cantidadVariables=tk.StringVar(value='0')
cantidadRestricciones=tk.StringVar(value='0')
datos = ['Metodo Gráfico', 'Simplex Dos Fases']
signo=['<=','>=','=']
tipo=['Max','Min']
colores=['b','g','r','c','m','y','k','w']
vectorRestricciones=[]
metodo='';

#Variables de interface
funcionObjetivo=[]
matrixRestricciones=[[],[]]

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
comboBox=ttk.Combobox(ventana,width=15,values=datos, textvariable=metodo)
tipoEjercicio=ttk.Combobox(ventana,width=5,values=tipo)
comboBoxSigno=[]
textArea=scrolledtext.ScrolledText(ventana,width=20, height=10,wrap=tk.WORD)


#Variables para método grafico
#Declaracion de x, y e intervalos
x = np.arange(-10, 15, 5)
y = np.arange(-10, 15, 5)
funcionesDespejedas=[]
lineasIdentificador=[]
vectorInterseccion=[]
puntosX=[]
puntosY=[]
FO_puntos=[]
ZSolucion=0

#Eventos
def evento_click():
    if(min_variables_restricciones() and (metodo_usar())!=0):
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
    #Validar datos
    #Metodo
    if(metodo_usar()):
        #Solucionar metodo grafico
        despejar_ecuaciones(asignar_matriz_restricciones())
        graficar_punteada_funcion_objetivo()
        print(determinar_intersecciones())
        evaluar_puntos_funcion_objetivo()
        if(str(tipoEjercicio.get())=='Max'):
            ZSolucion=max(FO_puntos)
            #plt.fill(puntosX, puntosY, color='silver')
        elif(str(tipoEjercicio.get())=='Min'):
            ZSolucion=min(FO_puntos)
            #plt.fill(puntosX, puntosY, color='silver')
        generar_string()
        configurarGrafico()
    
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
    componente.grid_forget()


def vista_funcion_objetivo():
    columna=0
    lblFuncionObejtivo = tk.Label(ventana,text='Funcion Objetivo')
    lblFuncionObejtivo.grid(row=0,column=0)
    tipoEjercicio.grid(row=0,column=1)
    for i in range(0,int(cantidadVariables.get()),1):
        columna+=1
        funcionObjetivo.insert(i,ttk.Entry(ventana,width=8, justify=tk.LEFT))
        funcionObjetivo[i].grid(row=0,column=columna+1);
        columna+=1
        if((int(cantidadVariables.get())-1)>i):
                lblVariable=tk.Label(ventana,text='x'+str(i+1)+' +')
                lblVariable.grid(row=0,column=columna+1)
        else:
                lblVariable=tk.Label(ventana,text='x'+str(i+1))
                lblVariable.grid(row=0,column=columna+1);

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
            vectorRestricciones.insert(posicion,ttk.Entry(ventana,width=8, justify=tk.LEFT))
            vectorRestricciones[posicion].grid(row=i+2,column=columna);
            columna+=1
            if(int(cantidadVariables.get())>mas):
                lblRestricciones2=tk.Label(ventana,text='x'+str(j+1)+' +')
                lblRestricciones2.grid(row=i+2,column=columna)
            else:
                lblRestricciones2=tk.Label(ventana,text='x'+str(j+1))
                lblRestricciones2.grid(row=i+2,column=columna)
            posicion+=1
        mas=0
        comboBoxSigno.insert(i, ttk.Combobox(ventana,width=5,values=signo))
        comboBoxSigno[i].grid(row=i+2,column=columna+1)
        txtResultados.insert(i,ttk.Entry(ventana,width=10, justify=tk.LEFT))
        txtResultados[i].grid(row=i+2,column=columna+2)
        columna=0
    botonDatosFunciones.grid(row=int(cantidadRestricciones.get())+2,column=0)

#Funciones de notificación
def mensaje(i, mensaje):
    if(i==0):
        messagebox.showerror("Error",mensaje)
    else:
        messagebox.showinfo("Info",mensaje)

#Funciones de validacion
def min_variables_restricciones():
    ''' if(int(cantidadRestricciones.get())>=13 and int(cantidadVariables.get())>=10):
        return True
    else:
        mensaje(0,"No cumple con los requisitos necesarios")
        return False '''
    return True

def metodo_usar():
    if(str(comboBox.get())=='Metodo Gráfico'):
        variableMetodo=1
        return 1
    elif (str(comboBox.get())=='Simplex Dos Fases'):
        variableMetodo=2
        return 2
    else:
        mensaje(0,"No selecciono el metodo")
        return variableMetodo
    
def validar_funcion_objetivo():
    #Yojhan
    print("Falta implementar")

def validar_restricciones():
    #Yojhan
    print("Falta implementar")
    
#Funciones del metodo Graficando
def asignar_matriz_restricciones():
    posicion=0
    matrixRestricciones=np.zeros((int(cantidadRestricciones.get()),int(cantidadVariables.get())))
    for i in range(0,int(cantidadRestricciones.get()),1):
        for j in range(0,int(cantidadVariables.get()),1):
            #rint(vectorRestricciones[posicion].get())
            matrixRestricciones[i][j]=int(vectorRestricciones[posicion].get())
            posicion+=1
    return matrixRestricciones

def despejar_ecuaciones(matrizRestricciones):
    posicionColor=0
    for i in range(0,int(cantidadRestricciones.get()),1):
        if(matrizRestricciones[i][1]==0):
            funcionesDespejedas.insert(i,int(txtResultados[i].get())-matrizRestricciones[i][1]*y/matrizRestricciones[i][0])
            lineasIdentificador.insert(i,LineString(np.column_stack((funcionesDespejedas[i], y))))
            plt.plot(funcionesDespejedas[i], y, '-', linewidth=2, color=colores[posicionColor])
        else:
            funcionesDespejedas.insert(i,int(txtResultados[i].get())-matrizRestricciones[i][0]*x/matrizRestricciones[i][1])
            lineasIdentificador.insert(i,LineString(np.column_stack((x, funcionesDespejedas[i]))))
            plt.plot(x, funcionesDespejedas[i], '-', linewidth=2, color='b')
        if(posicionColor==7):
            posicionColor=0

def graficar_punteada_funcion_objetivo():
    #Despejar funcion objetivo
    z=-int(funcionObjetivo[0].get())*x/int(funcionObjetivo[1].get())
    plt.plot(x, z, ':', linewidth=1, color='k')
    

def determinar_intersecciones():
    posicion=0
    x1=0
    y1=0
    for i in range(0,int(cantidadRestricciones.get()),1):
        for j in range(0,int(cantidadRestricciones.get())-1,1):
            if(j!=i):
                if(lineasIdentificador[i].intersection(lineasIdentificador[j])!=set()):
                    vectorInterseccion.insert(posicion, lineasIdentificador[i].intersection(lineasIdentificador[j]))#GUARDAR PUNTO
                    plt.plot(*vectorInterseccion[posicion].xy, 'o', color='k') #Graficar punto
                    x1,y1=vectorInterseccion[posicion].xy#Extraer puntos
                    puntosX.insert(i,np.float64(np.array(x1)))#Cambiar formato
                    puntosY.insert(i,np.float64(np.array(y1)))
                    posicion+=1
    return vectorInterseccion

def evaluar_puntos_funcion_objetivo():
    for i in range(0,len(puntosX),1):
        resultado=int(funcionObjetivo[0].get())*(puntosX[i])+int(funcionObjetivo[1].get())*(puntosY[i])
        FO_puntos.insert(i,resultado)
    #z01=-int(funcionObjetivo[0].get())*x/int(funcionObjetivo[1].get())

def generar_string():
    texto="";
    texto+=str(tipoEjercicio.get())+" Z="+str(funcionObjetivo[0].get())+"x1+"+str(funcionObjetivo[1].get())+"x2"
    print(texto)
    
def configurarGrafico():
    plt.grid()
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Método Gráfico')
    plt.show()

#Tamaño de la ventana
ventana.geometry('400x400');
#Nombre de la ventana
ventana.title('Ejercicio Simplex');
componentes_principal()
#Boton
botonEnviar.grid(row=5,column=5)#Mostrar el boton
#Abrir la ventana
ventana.mainloop();