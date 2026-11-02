import csv 
import os
import random

print ("Ingrese el numero de actividades: ")
numeroActividades = int(input())

print ("Ingrese el numero de los recursos: ")
numeroRecursos = int(input())

print ("Ingrese la duracion minima: ")
duracionMinima = int(input())

print ("Ingrese la duracion maxina: ")
duracionMaxima = int(input())

print ("Ingrese la capacidad minima de los recursos: ")
capacidadMinima = int(input())

print ("Ingrese la capacidad maxima de los recursos: ")
capacidadMaxima = int(input())

print ("Numero de actividades: ",numeroActividades)
print ("Numero de recursos: ",numeroRecursos)
print ("Duracion minima: ",duracionMinima, 
       "Duracion maxima", duracionMaxima)
print ("Capacidad minima: ",capacidadMinima,
       "Capacidad maxima: ",capacidadMaxima) 

listaActividades = []
listaRecursos = []

#Crear lista de actividades
for i in range (numeroActividades):
    listaActividades.append(i)

#Crear lista recursos
for i in range (numeroRecursos):
    listaRecursos.append(i)

print ("Lista de actividades: ")
print (listaActividades)
print ("Lista de recursos: ")
print (listaRecursos)

#Inicializar todos los elementos de la matriz en 0
matriz = [[0 for j in range(numeroActividades)]
        for i in range(numeroActividades)]

#Asignar valores randoms para las precendensias
for i in range(1,numeroActividades):
    for j in range(1,numeroActividades):
        if (i!=j and j<i):
            matriz[i][j] = random.randint(0,1)

#Inicializar lista
lista = []

#Obtener precedencias (encontrar de la matriz asignada)
print("Imprimir lista de precendecias")
for i in range (numeroActividades):
    lista = [i]
    for j in range (numeroActividades):
        if(matriz[i][j]==1):
            lista.append(j)
    print (lista)
    lista = []

#Inicializar listas
listaTiempos = []
listaCapacidad = []

#Asignar valores randoms para los tiempos de actividades
for i in range (numeroActividades):
    duracion = random.randint(duracionMinima,duracionMaxima)
    listaTiempos.append(duracion)

#Asignar valores randoms para el numero de cada recurso
for i in range (numeroRecursos):
    cantidad = random.randint(capacidadMinima,capacidadMaxima)
    listaCapacidad.append(cantidad)

#Imprimir instancias de ejemplo
print ("Lista de los tiempos:")
print (listaTiempos)
print ("Lista de los numeros de los recursos: ")
print (listaCapacidad)

#Crear matriz para asignar recursos a actividades
matrizDRJ = [
        [random.randint(0,listaCapacidad[i])
        for j in range (numeroActividades)]
        for i in range (numeroRecursos) 
    ]

#*******************************************************************
#Exportar datos a csv (actividades y tiempo)
with open ("actividades.csv", "w",newline = "") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(["Numero_actividad","duracion_actividad"])

    for i in range (numeroActividades):
        escritor.writerow([i+1,listaTiempos[i]])

#*******************************************************************
#Exportar datos csv (recursos y cantidad)
with open ("recursos.csv","w",newline = "") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(["Numero_recurso","cantidad_recurso"])

    for i in range (numeroRecursos):
        escritor.writerow([i+1,listaCapacidad[i]])

#*******************************************************************
#Exportar precedencias csv
with open ("predencias.csv","w",newline="") as archivo: 
    escritor = csv.writer(archivo)

    escritor.writerow(["Actividad","Precedencia"])

    for i in range (numeroActividades):
        lista = [i]
        for j in range (numeroActividades):
            if(matriz[i][j]==1):
                lista.append(j)
                escritor.writerow([i+1,j+1])
        if len(lista) == 1: #Comprobar tamaño de la lista
            escritor.writerow([i+1,0])
    lista = []

#*******************************************************************  
#Exportar asignacion de recursos
with open ("actividadRecurso.csv","w",newline="") as archivo:
    escritor = csv.writer(archivo)

    for i in matrizDRJ:
        escritor.writerow(i)

print("Archivo de actividades,recursos,precedencias y matriz drj creados con exito")
