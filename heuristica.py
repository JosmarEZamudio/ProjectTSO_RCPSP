import csv
import serial

#***********************************************
#Cargar archivos csv
#***********************************************
#1-Cargar tiempos de actividad
with open ("actividades.csv","r",newline="") as archivo:
    lectorInicial = csv.reader(archivo)
    numeroActividades = int(next(lectorInicial)[0].split(":")[1].strip())

    lector = csv.DictReader(archivo)

    actividades = {}

    for fila in lector:
        numero = int(fila["Numero_actividad"])
        duracion = int(fila["duracion_actividad"])

        actividades[numero] = duracion
#***********************************************
#2-Cargar cantidad de recursos
with open ("recursos.csv","r",newline="") as archivo:
    lectorInicial = csv.reader(archivo)
    numeroRecursos = int(next(lectorInicial)[0].split(":")[1].strip())

    lector = csv.DictReader(archivo)
   
    recursos = {}
    
    for fila in lector:
        numero = int(fila["Numero_recurso"])
        cantidad = int(fila["cantidad_recurso"])

        recursos[numero] = cantidad
#***********************************************
#Matriz drj, crear matriz e inicializar en 0 
matrizDrj = [[0 for j in range(numeroActividades)]
        for i in range(numeroRecursos)]

#for i in range (numeroRecursos):
   # for j in range (numeroActividades):
 #       print(matrizDrj[i][j], end="")
  #  print()
#***********************************************
#3-Cargar matriz drj (actividad recursos)
with open ("actividadRecurso.csv","r",newline="") as archivo:
    lector = csv.reader(archivo)

    for i, fila in enumerate(lector):
        for j, valor in enumerate(fila):
            matrizDrj[i][j] = int(valor)
#***********************************************
#4-Cargar precedencias
with open ("precedencias.csv","r",newline="") as archivo:
    lector = csv.DictReader(archivo)

    precedencias = {}

    for fila in lector:
        actividad = int(fila["Actividad"])
        predecesora = int(fila["Precedencia"])

        if actividad not in precedencias:
            precedencias[actividad] = []

        if predecesora != 0:
            precedencias[actividad].append(predecesora)
#***********************************************
#Fin de cargas

#Llamar funcion serial que contiene la funcion greedy
inicio,fin = serial.serialSGS(precedencias,actividades,recursos,matrizDrj)

for actividad in sorted(inicio, key=lambda j: inicio[j]):
    print(
        f"Actividad {actividad}: "
        f"Inicio = {inicio[actividad]}, "
        f"Fin = {fin[actividad]}"
    )
