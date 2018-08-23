#BLOQUE DE IMPORTACION DE FUNCIONES
import numpy as np

# BLOQUE DE DEFINICION DE CONSTANTES
#no hay

#BLOQUE DE DEFINICION DE FUNCIONES

def leerArchivo_notas(nombreArchivo):
    archivo = open(nombreArchivo,"r")
    contenido = []
    for linea in archivo:
        alumno = linea.strip().split(",")
        contenido.append(alumno)
    archivo.close()
    return contenido

def leerArchivo_alumnos(nombreArchivo):
    archivo = open(nombreArchivo,"r")
    for linea in archivo:
        nombres = linea.strip().split(",")
    archivo.close()
    return nombres

def obtenerPromedios_forma1(contenido):
    lista_promedios = []
    for alumno in contenido:
        notas = np.array(alumno,dtype=float)
        promedio = sum(notas)/len(notas)
        lista_promedios.append(promedio)
    return lista_promedios

def obtenerPromedios_forma2(contenido):
    lista_promedios = []
    acumulador = 0
    for alumno in contenido:
        for nota in alumno:
            acumulador+=float(nota)
        promedio = acumulador/len(alumno)
        lista_promedios.append(promedio)
        acumulador = 0
    return lista_promedios

def escribirPromedio_Nombres(promedios,nombres):
    archivo = open("promedios.txt","w")
    i = 0
    while i < len(promedios):
        archivo.write(nombres[i] + " tiene promedio " + str(promedios[i])+"\n")
        i+=1
    archivo.close()
    return True

#ENTRADA
notas = "notas.txt"
nombres = "alumnos.txt"

#PROCESAMIENTO
contenido = leerArchivo_notas(notas)
nombres = leerArchivo_alumnos(nombres)
promedios = obtenerPromedios_forma1(contenido)

#SALIDA
salida = escribirPromedio_Nombres(promedios,nombres)
if salida:
    print "archivo listo para revisar"
else:
    print "no se pudo completar la operacion"