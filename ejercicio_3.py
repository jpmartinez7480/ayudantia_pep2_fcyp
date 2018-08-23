#BLOQUE DE IMPORTACION DE FUNCIONES 
import numpy as np
import matplotlib.pyplot as grafico

#BLOQUE DE DEFINICION DE CONSTANTES 
#no hay

#BLOQUE DE DEFINICION DE FUNCIONES

#funcion que recibe el dominio de la funcion para calcular la funcion f
#entrada: array con el dominio de la funcion
#salida: vector con los valores de la funcion f
def fx(dominio_x):
    valor_absoluto = abs(-((dominio_x-2)**2) + 1) #defino el valor que va dentro de la raiz, solo porque asi se entiende mas
    f = 2 + np.sqrt(valor_absoluto) #creo que la funcion f
    return f

#funcion que recibe el dominio de la funcion para calcular la funcion g
#entrada: array con el dominio de la funcion
#salida: vector con los valores de la funcion g
def gx(dominio_x):
    valor_absoluto = abs(-((dominio_x-2)**2) + 1)
    g = 2 - valor_absoluto
    return g

#funcion que recibe el dominio de la funcion para calcular la funcion h
#entrada: array con el dominio de la funcion
#salida: vector con los valores de la funcion h
def hx(dominio_x):
    h = (3*dominio_x)-3
    return h

#funcion que recibe el dominio de la funcion para calcular la funcion i
#entrada: array con el dominio de la funcion
#salida: vector con los valores de la funcion i
def ix(dominio_x):
    i = (-3*dominio_x) + 9
    return i

#funcion que recibe el dominio de la funcion para calcular la funcion j
#entrada: array con el dominio de la funcion
#salida: vector con los valores de la funcion j
def jx(dominio_x):
    j = (0.2*dominio_x) + 1.7
    return j


#ENTRADAS
dominio = np.arange(0,4,0.01)

#PROCESAMIENTO
funcion_f = fx(dominio)
funcion_g = gx(dominio)
funcion_hi = hx(dominio)*ix(dominio)
funcion_j = jx(dominio)
grafico.plot(funcion_f,label = "f(x)") #se le da al grafico los valores de f y un label para identificar la funcion en el grafico
grafico.plot(funcion_g,label = "g(x)") #se le da al grafico los valores de g y un label para identificar la funcion en el grafico
grafico.plot(funcion_hi,label = "h(x)*i(x)") #se le da al grafico los valores de h e i y un label para identificar la funcion en el grafico
grafico.plot(funcion_j,label = "j(x)") #se le da al grafico los valores de j y un label para identificar la funcion en el grafico

#SALIDA
grafico.legend() #se habilita legend para mostrar los label definidos anteriormente
grafico.show() #se muestra el grafico


    
