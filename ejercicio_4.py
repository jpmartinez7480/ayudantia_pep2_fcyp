#BLOQUE DE IMPORTACION DE FUNCIONES
import numpy as np
import matplotlib.pyplot as grafico

#BLOQUE DE DEFINICION DE CONSTANTES
#no hay

#BLOQUE DE DEFINICION DE FUNCIONES

#funcion que calcula los valores de la funcion X(t)
#entrada: A como amplitud, w como periodo, dominio_t como el dominio de t
#salida: valores de la funcion X(t)
def Xt(A,w,dominio_t):
    x = A*np.sin(w*dominio_t)
    return x

#funcion que calcula los valores de la funcion v(t)
#entrada: A como amplitud, w como periodo, dominio_t como el dominio de t
#salida: valores de la funcion v(t)
def vt(A,w,dominio_t):
    v = A*w*np.cos(w*dominio_t)
    return v

#funcion que calcula los valores de la funcion a(t)
#entrada: A como amplitud, w como periodo, dominio_t como el dominio de t
#salida: valores de la funcion a(t)
def at(A,w,dominio_t):
    a = A*w*w*np.sin(w*dominio_t)
    return a

#ENTRADA
w = 2*np.pi/3
amplitud = 2
periodo = np.arange(0,21,0.1) #desde 0 al 20

#PROCESAMIENTO
funcion_Xt = Xt(amplitud,w,periodo)
funcion_vt = vt(amplitud,w,periodo)
funcion_at = at(amplitud,w,periodo)
grafico.plot(periodo,funcion_Xt,label = "X(t)",color="r")
grafico.plot(periodo,funcion_vt,label = "v(t)",color="b")
grafico.plot(periodo,funcion_at,label="a(t)",color="g")
grafico.title("Movimiento armonico simple")
grafico.xlabel("periodo")
grafico.ylabel("valor")
#SALIDA
grafico.legend()
grafico.show()
