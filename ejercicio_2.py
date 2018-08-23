#BLOQUE DE IMPORTACION DE FUNCIONES
#NO HAY

#BLOQUE DE DEFICION DE CONSTANTES
#NO HAY

#DEFICION DE FUNCIONES

#funcion que lee un archivo y retorna una lista de listas con el contenido del archivo
#entrada: nombre del archivo en string
#salida: lista de listas con el contenido del archivo, donde cada elemento de la lista es una lista con una linea del archivo
def leerArchivo(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    contenido = []
    for linea in archivo:
        persona = linea.strip().split(",") 
        contenido.append(persona)
    return contenido

#funcion que busca a las personas que tienen edad menor a 20
#entrada: lista de listas con el contenido del archivo
#salida: lista de listas con las personas que tienen edad menor a 20
def buscarJovenes(contenido):
    lista_jovenes = []
    for persona in contenido:
        if int(persona[2]) < 20:
            lista_jovenes.append(persona)
    return lista_jovenes

#funcion que busca a las personas que cumplen con los criterios para ser considerados jubilados
#entrada: lista de listas con el contenido del archivo
#salida: lista de listas con las personas que cumplen los criteros para ser considerados jubilados
def buscarJubilados(contenido):
    lista_jubilados = []
    for persona in contenido:
        if int(persona[2]) >= 60 and persona[1] == 'F':
            lista_jubilados.append(persona)
        elif int(persona[2]) >= 65 and persona[1] == 'M':
            lista_jubilados.append(persona)
    return lista_jubilados

def escribirArchivoJovenes(lista_jovenes):
    archivo = open("empleadosJovenes.txt","w")
    for persona in lista_jovenes:
        archivo.write(persona[0]+", "+persona[1]+", "+persona[2]+"\n")
    archivo.close()
    return True #no es necesario que retorne 

def escribirArchivoJubilados(lista_jubilados):
    archivo = open("empleadosAJubilar.txt","w")
    for persona in lista_jubilados:
        archivo.write(persona[0]+"\n")
    archivo.close()
    return True #no es necesario que retorne 

#ENTRADA
nombreArchivo = "empleados.txt"

#PROCESAMIENTO
contenidoArchivo = leerArchivo(nombreArchivo)
jovenes = buscarJovenes(contenidoArchivo)
jubilados = buscarJubilados(contenidoArchivo)

#SALIDA
salida_jovenes = escribirArchivoJovenes(jovenes)
salida_jubilados = escribirArchivoJubilados(jubilados)
if(salida_jovenes and salida_jubilados):
    print "la operacion fue terminada con exito"
else:
    print "No se logro completar la operacion"