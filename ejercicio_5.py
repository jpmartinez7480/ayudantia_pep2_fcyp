#BLOQUE DE IMPORTACION DE FUNCIONES
import numpy as np
import matplotlib.pyplot as grafico

# BLOQUE DE DEFINICION DE CONSTANTES
#no hay

#BLOQUE DE DEFINICION DE FUNCIONES

#funcion que obtiene el valor maximo y minimo del dominio de la funcion
#entrada: radio de la circunferencia, valores de desplazamiento a y b
#salida: array que contiene el dominio de x para la circunferencia
def obtenerDominioX(r,a,b):
    valorMaximoX = r + a
    valorMinimoX = a - r
    dominioX = np.arange(valorMinimoX,valorMaximoX+1,0.01)
    return dominioX

#funcion que calcula el recorrido de la circunferencia
#entrada: radio de la circunferencia, valores de desplazamiento a y b, dominio de la circunferencia
#salida: lista que contiene un array, con los recorridos -y y +y de la circunferencia
def obtenerRecorridoY(r,a,b,vectorX):
    valorAbs = abs(r**2-((vectorX-a)**2))
    valorMinimoY = -np.sqrt(valorAbs) + b
    valorMaximoY = np.sqrt(valorAbs) + b
    return [valorMinimoY,valorMaximoY]

#ENTRADA 
radio = input("Ingrese radio de circunferencia: ")
a = input("Ingrese valor de a: ")
b = input("Ingrese valor de b: ")
color_circunferencia = raw_input("Ingrese color para graficar la circunferencia: ")

#PROCESAMIENTO
dominio = obtenerDominioX(radio,a,b)
recorrido = obtenerRecorridoY(radio,a,b,dominio)
grafico.plot(dominio,recorrido[1],color=color_circunferencia)
grafico.plot(dominio,recorrido[0],color=color_circunferencia)
grafico.title("Circunferencia")
grafico.xlabel("x")
grafico.ylabel("y")

#SALIDA
grafico.show()